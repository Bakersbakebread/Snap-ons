from discord.ext import commands
from cogs.utils.dataIO import dataIO
from random import choice
import asyncio
import time
import discord
import os
import collections


class Gardening:
    """Grow your own plants!"""
    def __init__(self, bot):
        self.bot = bot
        self.gardeners = dataIO.load_json('data/gardening/gardeners.json')
        self.plants = dataIO.load_json('data/gardening/plants.json')
        self.products = dataIO.load_json('data/gardening/products.json')
        self.defaults = dataIO.load_json('data/gardening/defaults.json')
        self.badges = dataIO.load_json('data/gardening/badges.json')

        self.completion_task = bot.loop.create_task(self.check_completion())
        self.degradation_task = bot.loop.create_task(self.check_degradation())

    async def _save_gardeners(self):
        dataIO.save_json('data/gardening/gardeners.json', self.gardeners)

    async def _gardener(self, id):
        g = self.gardeners[id]
        gardener = collections.namedtuple('gardener', 'badges points products current')
        return gardener(badges=g['badges'], points=g['points'], products=g['products'], current=g['current'])

    async def _grow_time(self, gardener):
        now = int(time.time())
        then = gardener.current['timestamp']
        return (gardener.current['time'] - (now - then)) / 60

    async def _degradation(self, gardener):
        modifiers = sum([self.products[product]['modifier'] for product in gardener.products if gardener.products[product] > 0] + [self.badges['badges'][badge]['modifier'] for badge in gardener.badges])
        degradation = (100 / (gardener.current['time'] / 60) * (self.defaults['points']['base_degradation'] + gardener.current['degradation'])) + modifiers
        d = collections.namedtuple('degradation', 'degradation time modifiers')
        return d(degradation=degradation, time=gardener.current['time'], modifiers=modifiers)

    async def _die_in(self, gardener, degradation):
        return int(gardener.current['health'] / degradation.degradation)

    async def _withdraw_points(self, id, amount):
        points = self.gardeners[id]['points']
        if (points - amount) < 0:
            return False
        else:
            self.gardeners[id]['points'] -= amount
            return True

    @commands.group(pass_context=True, name='gardening')
    async def _gardening(self, context):
        """Gardening commands."""
        if context.invoked_subcommand is None:
            description = '**Gardening!**\nHere be help and description soon'
            em = discord.Embed(description=description, color=discord.Color.green())
            await self.bot.say(embed=em)

    @_gardening.command(pass_context=True, name='seed')
    async def _seed(self, context):
        """Sow the seed to grow the plant."""
        author = context.message.author
        if author.id not in self.gardeners:
            self.gardeners[author.id] = {}
            self.gardeners[author.id]['current'] = False
            self.gardeners[author.id]['points'] = 0
            self.gardeners[author.id]['badges'] = []
            self.gardeners[author.id]['products'] = {}
        if not self.gardeners[author.id]['current']:
            plant = choice(self.plants['plants'])
            plant['timestamp'] = int(time.time())
            message = 'During one of your many heroic adventures, you came across a mysterious bag that said "pick one". '
            message += 'To your surprise it had all kinds of different seeds in them. And now that you\'re home, you want to plant it. '
            message += 'You went to a local farmer to identify the seed, and the farmer said it was {} **{} ({})** seed.\n\n'.format(plant['article'], plant['name'], plant['rarity'])
            message += 'Take good care of your seed and water it frequently. Once it blooms, something nice might come from it. If it dies, however, you will get nothing.'
            if 'water' not in self.gardeners[author.id]['products']:
                self.gardeners[author.id]['products']['water'] = 0
            self.gardeners[author.id]['products']['water'] += 5
            self.gardeners[author.id]['current'] = plant
            await self._save_gardeners()

            await self.bot.say(message)
        else:
            plant = self.gardeners[author.id]['current']
            await self.bot.say('You\'re already growing {} **{}**, silly.'.format(plant['article'], plant['name']))

    @_gardening.command(pass_context=True, name='profile')
    async def _profile(self, context, *, member: discord.Member=None):
        """Check your gardening profile."""
        if member:
            author = member
        else:
            author = context.message.author
        if author.id in self.gardeners:
            gardener = await self._gardener(author.id)
            em = discord.Embed(color=discord.Color.green(), description='\a\n')
            avatar = author.avatar_url if author.avatar else author.default_avatar_url
            em.set_author(name='Gardening profile of {}'.format(author.name), icon_url=avatar)
            em.add_field(name='**Points**', value=gardener.points)
            if not gardener.current:
                em.add_field(name='**Currently growing**', value='None')
            else:
                em.set_thumbnail(url=gardener.current['image'])
                em.add_field(name='**Currently growing**', value='{0} ({1:.2f}%)'.format(gardener.current['name'], gardener.current['health']))
            if not gardener.badges:
                em.add_field(name='**Badges**', value='None')
            else:
                badges = ''
                for badge in gardener.badges:
                    badges += '{} {}\n'.format(badge.capitalize(), self.badges['badges'][badge]['modifier'])
                em.add_field(name='**Badges**', value=badges)
            if not gardener.products:
                em.add_field(name='**Products**', value='None')
            else:
                products = ''
                for product in gardener.products:
                    products += '{} ({}) {}\n'.format(product.capitalize(), gardener.products[product], [0 if gardener.products[product] < 1 else self.products[product]['modifier']][0])
                em.add_field(name='**Products**', value=products)
            if gardener.current:
                degradation = await self._degradation(gardener)
                die_in = await self._die_in(gardener, degradation)
                to_grow = await self._grow_time(gardener)
                em.set_footer(text='Total degradation: {0:.2f}% / {1} min (100 / ({2} / 60) * (BaseDegr {3:.2f} + PlantDegr {4:.2f})) + ModDegr {5:.2f}) Your plant will die in {6} minutes and {7:.1f} minutes to go for flowering.'.format(degradation.degradation, self.defaults['timers']['degradation'], degradation.time, self.defaults['points']['base_degradation'], gardener.current['degradation'], degradation.modifiers, die_in, to_grow))
            await self.bot.say(embed=em)
        else:
            await self.bot.say('Who?')

    @_gardening.command(pass_context=True, name='plants')
    async def _plants(self, context):
        """Look at the list of the available plants."""
        tick = ''
        tock = ''
        tick_tock = 0
        for plant in self.plants['plants']:
            if tick_tock == 0:
                tick += '**{}**\n'.format(plant['name'])
                tick_tock = 1
            else:
                tock += '**{}**\n'.format(plant['name'])
                tick_tock = 0
        em = discord.Embed(title='All plants that are growable', color=discord.Color.green())
        em.add_field(name='\a', value=tick)
        em.add_field(name='\a', value='\a')
        em.add_field(name='\a', value=tock)
        await self.bot.say(embed=em)

    @_gardening.command(pass_context=True, name='plant')
    async def _plant(self, context, *plant):
        plant = ' '.join(plant)
        for p in self.plants['plants']:
            if p['name'].lower() == plant.lower():
                plant = p
                t = True
                break
            t = False
        if t:
            em = discord.Embed(title='Plant statistics of {}'.format(plant['name']), color=discord.Color.green(), description='\a\n')
            em.set_thumbnail(url=plant['image'])
            em.add_field(name='**Name**', value=plant['name'])
            em.add_field(name='**Rarity**', value=plant['rarity'].capitalize())
            em.add_field(name='**Grow Time**', value='{0:.1f} minutes'.format(plant['time'] / 60))
            em.add_field(name='**Damage Threshold**', value='{}%'.format(plant['threshold']))
            em.add_field(name='**Badge**', value=plant['badge'])
            em.add_field(name='**Reward**', value=plant['reward'])
            await self.bot.say(embed=em)
        else:
            await self.bot.say('What plant?')

    @_gardening.command(pass_context=True, name='state')
    async def _state(self, context):
        """Check the state of your plant."""
        author = context.message.author
        gardener = await self._gardener(author.id)
        if author.id not in self.gardeners or not gardener.current:
            message = 'You\'re currently not growing a plant.'
        else:
            plant = gardener.current
            degradation = await self._degradation(gardener)
            die_in = await self._die_in(gardener, degradation)
            to_grow = await self._grow_time(gardener)
            message = 'You\'re growing {0} **{1}**. Its health is **{2:.2f}%** and still has to grow for **{3:.1f}** minutes. It is losing **{4:.2f}%** per minute and will die in **{5:.1f}** minutes.'.format(plant['article'], plant['name'], plant['health'], to_grow, degradation.degradation, die_in)
        await self.bot.say(message)

    @_gardening.command(pass_context=True, name='products')
    async def _products(self, context):
        """Look at the list of the available gardening supplies."""
        em = discord.Embed(title='All gardening supplies you can buy', description='\a\n', color=discord.Color.green())
        for product in self.products:
                em.add_field(name='**{}**'.format(product.capitalize()), value='Cost: {} pts\n+{} health\n-{}% damage'.format(self.products[product]['cost'], self.products[product]['health'], self.products[product]['damage']))
        await self.bot.say(embed=em)

    @_gardening.command(pass_context=True, name='buy')
    async def _buy(self, context, product, amount: int):
        """Buy gardening supplies."""
        author = context.message.author
        if author.id not in self.gardeners:
            message = 'You\'re currently not growing a plant.'
        else:
            if product.lower() in self.products:
                withdraw_points = await self._withdraw_points(author.id, self.products[product.lower()]['cost'] * amount)
                if withdraw_points:
                    if product.lower() not in self.gardeners[author.id]['products']:
                        self.gardeners[author.id]['products'][product.lower()] = 0
                    self.gardeners[author.id]['products'][product.lower()] += amount
                    self.gardeners[author.id]['points'] += self.defaults['points']['buy']
                    await self._save_gardeners()
                    message = 'You bought some {}'.format(product.lower())
                else:
                    message = 'You don\'t have enough points. You have {}, but need {}.'.format(self.gardeners[author.id]['points'], self.products[product.lower()]['cost'] * amount)

            else:
                message = 'I don\'t have this product.'
        await self.bot.say(message)

    @commands.command(pass_context=True, name='poison')
    async def _poison(self, context):
        """Kill your plant by poisoning it."""
        author = context.message.author
        if author.id not in self.gardeners or not self.gardeners[author.id]['current']:
            message = 'You\'re currently not growing a plant.'
        else:
            self.gardeners[author.id]['current'] = False
            message = 'You poisoned your plant! Why?'
            self.gardeners[author.id]['points'] -= self.defaults['points']['poison']
            if self.gardeners[author.id]['points'] < 0:
                self.gardeners[author.id]['points'] = 0
            await self._save_gardeners()
        await self.bot.say(message)

    @commands.command(pass_context=True, name='water')
    async def _water(self, context):
        """Water your plant."""
        author = context.message.author
        if author.id not in self.gardeners or not self.gardeners[author.id]['current']:
            message = 'You\'re currently not growing a plant.'
        else:
            if 'water' in self.gardeners[author.id]['products']:
                if self.gardeners[author.id]['products']['water'] > 0:
                    self.gardeners[author.id]['current']['health'] += self.products['water']['health']
                    self.gardeners[author.id]['products']['water'] -= 1
                    message = 'Your plant got some health back!'
                    if self.gardeners[author.id]['current']['health'] > self.gardeners[author.id]['current']['threshold']:
                        self.gardeners[author.id]['current']['health'] -= self.products['water']['damage']
                        message = 'You gave too much water! Your plant lost some health. :wilted_rose:'
                    self.gardeners[author.id]['points'] += self.defaults['points']['water']
                    await self._save_gardeners()
                else:
                    message = 'You have no water. Go buy some!'
            else:
                message = 'You have no water. Go buy some!'
        await self.bot.say(message)

    @commands.command(pass_context=True, name='fertilize')
    async def _fertilize(self, context, fertilizer):
        """Fertilize the soil."""
        author = context.message.author
        if author.id not in self.gardeners or not self.gardeners[author.id]['current']:
            message = 'You\'re currently not growing a plant.'
        else:
            if fertilizer.lower() in self.products and fertilizer.lower() != 'water':
                if fertilizer.lower() in self.gardeners[author.id]['products']:
                    if self.gardeners[author.id]['products'][fertilizer] > 0:
                        self.gardeners[author.id]['current']['health'] += self.products['water']['health']
                        self.gardeners[author.id]['products'][fertilizer] -= 1
                        message = 'Your plant got some health back!'
                        if self.gardeners[author.id]['current']['health'] > self.gardeners[author.id]['current']['threshold']:
                            self.gardeners[author.id]['current']['health'] -= self.products['water']['damage']
                            message = 'You gave too much fertilizer! Your plant lost some health. :wilted_rose:'
                        self.gardeners[author.id]['points'] += self.defaults['points']['fertilize']
                        await self._save_gardeners()
                    else:
                        message = 'You have no {} left. Go buy some!'.format(fertilizer.capitalize())
                else:
                    message = 'You have no {}. Go buy some!'.format(fertilizer.capitalize())
            else:
                message = 'There is no {}.'.format(fertilizer.capitalize())
        await self.bot.say(message)

    async def check_degradation(self):
        while 'Gardening' in self.bot.cogs:
            for id in self.gardeners:
                gardener = await self._gardener(id)
                if gardener.current:
                    degradation = await self._degradation(gardener)
                    self.gardeners[id]['current']['health'] -= degradation.degradation
                    self.gardeners[id]['points'] += self.defaults['points']['growing']
                    await self._save_gardeners()
            await asyncio.sleep(self.defaults['timers']['degradation'] * 60)

    async def check_completion(self):
        while 'Gardening' in self.bot.cogs:
            now = int(time.time())
            delete = False
            for id in self.gardeners:
                gardener = await self._gardener(id)
                if gardener.current:
                    then = gardener.current['timestamp']
                    health = gardener.current['health']
                    grow_time = gardener.current['time']
                    badge = gardener.current['badge']
                    reward = gardener.current['reward']
                    if (now - then) > grow_time:
                        self.gardeners[id]['points'] += self.defaults['points']['complete']
                        if badge not in self.gardeners[id]['badges']:
                            self.gardeners[id]['badges'].append(badge)
                        message = 'Your plant made it! You are rewarded with the **{}** badge and you have recieved **{}** points.'.format(badge, reward)
                        delete = True
                    elif health < 0:
                        message = 'Your plant died!'
                        delete = True
                if delete:
                    await self.bot.send_message(discord.User(id=str(id)), message)
                    self.gardeners[id]['current'] = False
                    await self._save_gardeners()
            await asyncio.sleep(self.defaults['timers']['completion'] * 60)

    async def __unload(self):
        self.completion_task.cancel()
        self.degradation_task.cancel()
        await self._save_gardeners()


def check_folder():
    if not os.path.exists('data/gardening'):
        print('Creating data/gardening folder...')
        os.makedirs('data/gardening')


def check_file():
    if not dataIO.is_valid_json('data/gardening/gardeners.json'):
        print('Creating default gardeners.json...')
        dataIO.save_json('data/gardening/gardeners.json', {})


def setup(bot):
    check_folder()
    check_file()
    cog = Gardening(bot)
    bot.add_cog(cog)
