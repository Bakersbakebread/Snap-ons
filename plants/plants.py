from discord.ext import commands
from cogs.utils.dataIO import dataIO
from random import choice
import asyncio
import time
import discord
import os


class Plants:
    def __init__(self, bot):
        self.bot = bot
        self.gardeners = dataIO.load_json('data/plants/gardeners.json')
        self.plants = dataIO.load_json('data/plants/plants.json')
        self.products = dataIO.load_json('data/plants/products.json')
        self.defaults = dataIO.load_json('data/plants/defaults.json')
        self.badges = dataIO.load_json('data/plants/badges.json')
        self.bank = self.bot.get_cog('Economy').bank

    @commands.group(pass_context=True, name='plant')
    async def _plant(self, context):
        if context.invoked_subcommand is None:
            author = context.message.author
            if author.id not in self.gardeners or not self.gardeners[author.id]['current']:
                message = 'You\'re currently not growing a plant.'
            else:
                plant = self.gardeners[author.id]['current']
                now = int(time.time())
                then = self.gardeners[author.id]['current']['timestamp']
                to_grow = (self.gardeners[author.id]['current']['time'] - (now - then)) / 60
                message = 'You\'re growing {0} **{1}**. Its health is **{2:.2f}%** and still has to grow for **{3:.1f}** minutes.'.format(plant['article'], plant['name'], plant['health'], to_grow)
            await self.bot.say(message)

    @_plant.command(pass_context=True, name='me')
    async def _me(self, context):
        author = context.message.author
        if author.id in self.gardeners:
            gardener = self.gardeners[author.id]
            em = discord.Embed(color=discord.Color.green(), description='\a\n')
            avatar = author.avatar_url if author.avatar else author.default_avatar_url
            em.set_author(name='Gardening profile of {}'.format(author.name), icon_url=avatar)
            em.add_field(name='**Points**', value=gardener['points'])
            if not gardener['current']:
                em.add_field(name='**Currently growing**', value='None')
            else:
                em.set_thumbnail(url=gardener['current']['image'])
                em.add_field(name='**Currently growing**', value='{0} ({1:.2f}%)'.format(gardener['current']['name'], gardener['current']['health']))
            if not gardener['badges']:
                em.add_field(name='**Badges**', value='None')
            else:
                badges = ''
                for badge in gardener['badges']:
                    badges += '{} {}\n'.format(badge.capitalize(), self.badges['badges'][badge]['modifier'])
                em.add_field(name='**Badges**', value=badges)
            if not gardener['products']:
                em.add_field(name='**Products**', value='None')
            else:
                products = ''
                for product in gardener['products']:
                    products += '{} ({}) {}\n'.format(product.capitalize(), gardener['products'][product], [0 if gardener['products'][product] < 1 else self.products[product]['modifier']][0])
                em.add_field(name='**Products**', value=products)
            if gardener['current']:
                modifiers = sum([self.products[product]['modifier'] for product in gardener['products'] if gardener['products'][product] > 0] + [self.badges['badges'][badge]['modifier'] for badge in gardener['badges']])
                degradation = (100 / (gardener['current']['time'] / 60) * (self.defaults['points']['base_degradation'] + gardener['current']['degradation'])) + modifiers
                die_in = int(gardener['current']['health'] / degradation)
                now = int(time.time())
                then = self.gardeners[author.id]['current']['timestamp']
                to_grow = (self.gardeners[author.id]['current']['time'] - (now - then)) / 60
                em.set_footer(text='Total degradation: {0:.2f}% / {1} min (100 / ({2} / 60) * (BaseDegr {3:.2f} + PlantDegr {4:.2f})) + ModDegr {5:.2f}) Your plant will die in {6} minutes and {7:.1f} minutes to go for flowering.'.format(degradation, self.defaults['timers']['degradation'], gardener['current']['time'], self.defaults['points']['base_degradation'], gardener['current']['degradation'], modifiers, die_in, to_grow))
            await self.bot.say(embed=em)
        else:
            await self.bot.say('You haven\'t grown any plants yet.')

    @commands.command(pass_context=True, name='buy')
    async def _buy(self, context, product, amount: int):
        author = context.message.author
        if author.id not in self.gardeners:
            message = 'You\'re currently not growing a plant.'
        else:
            if product.lower() in self.products:
                try:
                    if product.lower() not in self.gardeners[author.id]['products']:
                        self.gardeners[author.id]['products'][product.lower()] = 0
                    self.gardeners[author.id]['products'][product.lower()] += amount
                    self.bank.withdraw_credits(author, self.products[product.lower()]['cost'] * amount)
                    self.gardeners[author.id]['points'] += self.defaults['points']['buy']
                    await self.save_gardeners()
                    message = 'You bought some {}'.format(product.lower())
                except:
                    message = 'You don\'t have enough money to buy {} {}!'.format(amount, product.lower())
            else:
                message = 'I don\'t have this product.'
        await self.bot.say(message)

    @commands.command(pass_context=True, name='poison')
    async def _poison(self, context):
        author = context.message.author
        if author.id not in self.gardeners or not self.gardeners[author.id]['current']:
            message = 'You\'re currently not growing a plant.'
        else:
            self.gardeners[author.id]['current'] = False
            message = 'You poisoned your plant! Why?'
            self.gardeners[author.id]['points'] -= self.defaults['points']['poison']
            if self.gardeners[author.id]['points'] < 0:
                self.gardeners[author.id]['points'] = 0
            await self.save_gardeners()
        await self.bot.say(message)

    @commands.command(pass_context=True, name='water')
    async def _water(self, context):
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
                    await self.save_gardeners()
                else:
                    message = 'You have no water. Go buy some!'
            else:
                message = 'You have no water. Go buy some!'
        await self.bot.say(message)

    @commands.command(pass_context=True, name='grow')
    async def _grow(self, context):
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

            self.gardeners[author.id]['current'] = plant
            await self.save_gardeners()

            await self.bot.say(message)
        else:
            plant = self.gardeners[author.id]['current']
            await self.bot.say('You\'re already growing {} **{}**, silly.'.format(plant['article'], plant['name']))

    async def save_gardeners(self):
        dataIO.save_json('data/plants/gardeners.json', self.gardeners)

    async def check_degration(self):
        while 'Plants' in self.bot.cogs:
            for gardener in self.gardeners:
                if self.gardeners[gardener]['current']:
                    modifiers = sum([self.products[product]['modifier'] for product in self.gardeners[gardener]['products'] if self.gardeners[gardener]['products'][product] > 0] + [self.badges['badges'][badge]['modifier'] for badge in self.gardeners[gardener]['badges']])
                    degradation = (100 / (self.gardeners[gardener]['current']['time'] / 60) * (self.defaults['points']['base_degradation'] + self.gardeners[gardener]['current']['degradation'])) + modifiers
                    self.gardeners[gardener]['current']['health'] -= degradation
                    self.gardeners[gardener]['points'] += self.defaults['points']['growing']
                    await self.save_gardeners()
                    if self.gardeners[gardener]['current']['health'] < 5:
                        message = 'Your plant is looking a bit droopy. I would give it some water if I were you.'
                        await self.bot.send_message(discord.User(id=str(gardener)), message)
            await asyncio.sleep(self.defaults['timers']['degradation'] * 60)

    async def check_completion(self):
        while 'Plants' in self.bot.cogs:
            now = int(time.time())
            delete = False
            for gardener in self.gardeners:
                if self.gardeners[gardener]['current']:
                    then = self.gardeners[gardener]['current']['timestamp']
                    health = self.gardeners[gardener]['current']['health']
                    grow_time = self.gardeners[gardener]['current']['time']
                    badge = self.gardeners[gardener]['current']['badge']
                    reward = self.gardeners[gardener]['current']['reward']
                    if (now - then) > grow_time:
                        self.gardeners[gardener]['points'] += self.defaults['points']['complete']
                        self.gardeners[gardener]['badges'].append(badge)
                        # self.bank.deposit_credits(discord.User(id=str(gardener)), reward)
                        message = 'Your plant made it! You are rewarded with the **{}** badge and **{}** is added to your bank account!'.format(badge, reward)
                        delete = True
                    elif health < 0:
                        message = 'Your plant died!'
                        delete = True
                if delete:
                    await self.bot.send_message(discord.User(id=str(gardener)), message)
                    self.gardeners[gardener]['current'] = False
                    await self.save_gardeners()
            await asyncio.sleep(self.defaults['timers']['completion'] * 60)


def check_folder():
    if not os.path.exists('data/plants'):
        print('Creating data/plants folder...')
        os.makedirs('data/plants')


def check_file():
    if not dataIO.is_valid_json('data/plants/gardeners.json'):
        print('Creating default gardeners.json...')
        dataIO.save_json('data/plants/gardeners.json', {})


def setup(bot):
    check_folder()
    check_file
    cog = Plants(bot)
    loop = asyncio.get_event_loop()
    loop.create_task(cog.check_degration())
    loop.create_task(cog.check_completion())
    bot.add_cog(cog)
