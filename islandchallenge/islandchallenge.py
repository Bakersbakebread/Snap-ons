import discord
from discord.ext import commands
import random
import asyncio

class IslandChallenge:
    """Complete the 7 island trials!"""
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def verdantcavern(self, context):
        """Go on Trial Captain Illima's trial!"""
        bank = self.bot.get_cog('Economy').bank
        await self.bot.say('**Illima**: Hello trainer, it seems you come to face me, Illima, the normal-type trial captain.')
        await asyncio.sleep(2)
        await self.bot.say('**Illima**: For my trial, you have to find and defeat 3 pokemon, 2 **yungoos** and a **gumshoos**. There is a pedestal with the thing you need to retrieve at the end...')

        timechart = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
        reward = 250

        await asyncio.sleep(2)
        await self.bot.say('You venture through the cavern...')
        await asyncio.sleep(random.choice(timechart))
        await self.bot.say('AHH! It\'s a wild **yungoos**! What will {0} do? (battle/run)'.format(context.message.author.mention))
        answer = await self.bot.wait_for_message(timeout=30,
                                                 author=context.message.author)
        if answer is None:
            await self.bot.say('The wild yungoos attacked you but you managed to escape... (**-50**)')
            reward = reward - 50
        elif answer.content.lower().strip() == 'battle':
            await self.bot.say('You defeated the wild yungoos! (**+50**)')
            reward = reward + 50
        else:
            await self.bot.say('The wild yungoos attacked you but you managed to escape... (**-50**)')
            reward = reward - 50
        await self.bot.say('You start venturing through the cavern again...')
        await asyncio.sleep(random.choice(timechart))
        await self.bot.say('AHH! It\'s a wild **yungoos**! What will {0} do? (battle/run)'.format(context.message.author.mention))
        answer = await self.bot.wait_for_message(timeout=30,
                                                 author=context.message.author)
        if answer is None:
            await self.bot.say('The wild yungoos attacked you but you managed to escape... (**-50**)')
            reward = reward - 50
        elif answer.content.lower().strip() == 'battle':
            await self.bot.say('You defeated the wild yungoos! (**+50**)')
            reward = reward + 50
        else:
            await self.bot.say('The wild yungoos attacked you but you managed to escape... (**-50**)')
            reward = reward - 50
        await self.bot.say('You start venturing through the cavern again...')
        await asyncio.sleep(random.choice(timechart))
        await self.bot.say('AHH! It\'s a wild **gumshoos**! What will {0} do? (battle/run)'.format(context.message.author.mention))
        answer = await self.bot.wait_for_message(timeout=30,
                                                 author=context.message.author)
        if answer is None:
            await self.bot.say('The wild gumshoos attacked you but you managed to escape... (**-100**)')
            reward = reward - 100
        elif answer.content.lower().strip() == 'battle':
            await self.bot.say('You defeated the wild gumshoos! (**+100**)')
            reward = reward + 100
        else:
            await self.bot.say('The wild gumshoos attacked you but you managed to escape... (**-100**)')
            reward = reward - 100
        await asyncio.sleep(2)
        await self.bot.say('You spot a pedestal.')
        await asyncio.sleep(2)
        await self.bot.say('You go up to it and grab the Z Crystal, Normalium-Z and go back to Illima.')
        await asyncio.sleep(2)

        #Reward Check
        if reward == 300:
            await self.bot.say('**Illima**: You have done excellent on your trial... Congratulations! Here\'s your reward!')
            await self.bot.say('*You got a **Verdant Cave Trial Completion Stamp**!*')
            await asyncio.sleep(2)
            await self.bot.say('You recieved {0}$!'.format(reward))
            bank.deposit_credits(context.message.author, reward)
        elif reward > 150 and reward != 300:
            await self.bot.say('**Illima**: You have done moderately on your trial... Here\'s what you get for that.')
            await asyncio.sleep(2)
            await self.bot.say('You recieved {0}$!'.format(reward))
            bank.deposit_credits(context.message.author, reward)
        else:
            await self.bot.say('**Illima**: You haven\'t done well on your trial. You get nothing!')
    @commands.command(pass_context=True)
    async def brooklethill(self, context):
        """Go on Trial Captain Lana's trial!"""
        bank = self.bot.get_cog('Economy').bank
        await self.bot.say('**Lana**: Hello trainer, it seems you come to face me, Lana, the water-type trial captain.')
        await asyncio.sleep(2)
        await self.bot.say('**Lana**: For my trial, you have to investigate the disturbance in these lakes and pools. You\'ll have to navigate through them using the Lapras Ride.')

        x = 0
        reward = 0
        paths = [
            {'direction' : 'right', 'map': '*> <'},
            {'direction' : 'left', 'map' : '> <*'}
            ]

        for x in range(0, 10):
            await asyncio.sleep(2)
            await self.bot.say('You hear a sound...')
            path = random.choice(paths)
            await asyncio.sleep(2)
            await self.bot.say('{0} You see this in front of you: ``{1}``, Where would you go? (right/left)'.format(context.message.author.mention, path['map']))
            answer = await self.bot.wait_for_message(timeout=30,
                                                     author=context.message.author)
            if answer is None:
                await self.bot.say('This doesn\'t seem to be the correct way... *You turn back.* (**-50**)')
                if reward > 0:
                    reward = reward - 50
                else:
                    reward = reward - 0
            elif answer.content.lower().strip() == path['direction']:
                await self.bot.say('It seems you\'re going in the right direction! (**+50**)')
                reward = reward + 50
                x += 1
            else:
                await self.bot.say('This doesn\'t seem to be the correct way... *You turn back.* (**-50**)')
                if reward > 0:
                    reward = reward - 50
                else:
                    reward = reward - 0
        await self.bot.say('{0} You find the source of the disturbance... It\'s just a **wishiwashi**?! Would you like to fight it? (yes/no)'.format(context.message.author.mention))
        answer = await self.bot.wait_for_message(timeout=30,
                                                 author=context.message.author)
        if answer is None:
            await self.bot.say('You try to observe it from afar...')
        elif answer.content.lower().strip() == 'yes':
            await self.bot.say('You prepare for your battle...')
        else:
            await self.bot.say('You try to observe it from afar...')
        await asyncio.sleep(2)
        await self.bot.say('Something is happening! ***Wishiwashi** used Schooling!*')
        await asyncio.sleep(2)
        await self.bot.say('{0} Will you atack it? (yes/no)'.format(context.message.author.mention))
        answer = await self.bot.wait_for_message(timeout=30,
                                                 author=context.message.author)
        if answer is None:
            await self.bot.say('You don\'t attack but rather observe it...')
            await asyncio.sleep(2)
            await self.bot.say('It tries to attack you, but you manage to escape. (**-100**)')
            if reward > 0:
                reward = reward - 100
            else:
                reward = reward - 0
        elif answer.content.lower().strip() == 'yes':
            await self.bot.say('**Lapras**\' Ice Beam attack defeated the **wishiwashi**! (**+100**')
            await asyncio.sleep(2)
            await self.bot.say('You recieved the Z crystal, Waterium-Z!')
            reward = reward + 100
        else:
            await self.bot.say('You don\'t attack but rather observe it...')
            await asyncio.sleep(2)
            await self.bot.say('It tries to attack you, but you manage to escape. (**-100**)')
            if reward > 0:
                reward = reward - 100
            else:
                reward = reward - 0
        await asyncio.sleep(2)
        await self.bot.say('You head back to Lana...')
        await asyncio.sleep(2)
        #Reward Check
        if reward == 600:
            await self.bot.say('**Lana**: You have done excellent on your trial... Congratulations! Here\'s your reward!')
            await self.bot.say('*You got a **Brooklet Hill Trial Completion Stamp**!*')
            await asyncio.sleep(2)
            await self.bot.say('You recieved {0}$!'.format(reward))
            bank.deposit_credits(context.message.author, reward)
        elif reward > 300 and reward != 600:
            await self.bot.say('**Lana**: You have done moderately on your trial... Here\'s what you get for that.')
            await asyncio.sleep(2)
            await self.bot.say('You recieved {0}$!'.format(reward))
            bank.deposit_credits(context.message.author, reward)
        else:
            await self.bot.say('**Lana**: You haven\'t done well on your trial. You get nothing!')
    @commands.command(pass_context=True)
    async def welavolcanopark(self, context):
        """Go on Trial Captain Kiawe's trial!"""
        bank = self.bot.get_cog('Economy').bank
        await self.bot.say('**Kiawe**: Hello trainer, it seems you come to face me, Kiawe, the fire-type trial captain.')
        await asyncio.sleep(2)
        await self.bot.say('**Kiawe**: For my trial, you have to differentiate the dances performed by my team of **marowak**.')

        x = 0
        reward = 250
        dances = [
            {'identifier' : '1', 'before' : 'http://image.prntscr.com/image/84f404fb91514022b7be114f90188bf2.png', 'after' : 'http://image.prntscr.com/image/c47c21fbf3714bd8810cce8c8a744eac.png', 'options' : '1. The Right Marowak \n2. The Middle Marowak \n3. The Left Marowak', 'answer' : 'the middle marowak', 'answerno' : '2'},
            {'identifier' : '2', 'before' : 'http://image.prntscr.com/image/be35dcfb65034fd29b90bf33f63df11e.png', 'after' : 'http://image.prntscr.com/image/dffd69a94a5d4c1d8bff5074dff03494.png', 'options' : '1. The Right Marowak \n2. The Middle Marowak \n3. The Left Marowak \n4. The Hiker', 'answer' : 'the hiker', 'answerno' : '4'},
            {'identifier' : '3', 'before' : 'http://image.prntscr.com/image/3599826aab4e48ceaf1fce241be2e6bd.png', 'after' : 'http://image.prntscr.com/image/5dec40f62716423da2c68e3257503ec8.png', 'options' : '1. The totem pokemon \n2. The black pokemon \n3. The new pokemon \n4. The suspicious pokemon', 'answer' : 'the new pokemon', 'answerno' : '3'}
             ]

        for x in range(0, 3):
            dance = random.choice(dances)
            await asyncio.sleep(2)
            await self.bot.say('**Kiawe**: Let the dance commence!')
            await asyncio.sleep(2)
            await self.bot.say(dance['before'], delete_after=5)
            await self.bot.say('**Kiawe**: {0} Watch carefully and memorize this dance.'.format(context.message.author.mention), delete_after=5)
            await asyncio.sleep(5)
            await self.bot.say(dance['after'])
            await self.bot.say('**Kiawe**: {0} What seems different? \n{1}'.format(context.message.author.mention, dance['options']))
            answer = await self.bot.wait_for_message(timeout=30,
                                                     author=context.message.author)
            if answer is None:
                await self.bot.say('That\'s not correct {0}... (-100)'.format(context.message.author.mention))
                reward = reward - 100
            elif answer.content.lower().strip() == dance['answer'] or dance['answerno']:
                x += 1
                await self.bot.say('**Kiawe**: B-but how?!')
                await asyncio.sleep(2)
                await self.bot.say('**Kiawe**: {0} That was truly spectacular. (**+100**)'.format(context.message.author.mention))
                reward = reward + 100
                await asyncio.sleep(2)
                await self.bot.say('**Kiawe**: And to add to the spectacule...')
                await asyncio.sleep(2)
                if dance['identifier'] == 1:
                    foe = '**marowak**'
                elif dance['identifier'] == 2:
                    foe = '**hiker**'
                else:
                    foe = '**salazzle**'
                await self.bot.say('**Kiawe**: Come {0}!'.format(foe))
                await asyncio.sleep(2)
                await self.bot.say('{0} What would you like to do? (battle/run)'.format(context.message.author.mention))
                answer = await self.bot.wait_for_message(timeout=30,
                                                         author=context.message.author)
                if answer is None:
                    await self.bot.say('You try to run away while {0} attacks but you get away safely... (**-150**)'.format(foe))
                    reward = reward - 150
                elif answer.content.lower().strip() == 'battle':
                    await self.bot.say('You prepare for your battle...')
                    await asyncio.sleep(2)
                    await self.bot.say('Your pokemon\'s attack defeats the enemy {0}! (**+150**)'.format(foe))
                    reward = reward + 150
                else:
                    await self.bot.say('You try to run away while {0} attacks but you get away safely... (**-150**)'.format(foe))
                    reward = reward - 150
                await self.bot.say('**Kiawe**: My fellow {0} was so impressed with your answer that it had to attack you...'.format(foe))
            else:
                await self.bot.say('That\'s not correct... (-100)')
                reward = reward - 100
        await asyncio.sleep(2)
        if x >= 550:
            await self.bot.say('You recieved the Z Crystal, Firium-Z!')
        await asyncio.sleep(2)
        #Reward Check
        if reward == 1000:
            await self.bot.say('**Kiawe**: You have done excellent on your trial... Congratulations! Here\'s your reward!')
            await self.bot.say('*You got a **Wela Volcano Park Trial Completion Stamp**!*')
            await asyncio.sleep(2)
            await self.bot.say('You recieved {0}$!'.format(reward))
            bank.deposit_credits(context.message.author, reward)
        elif reward > 500 and reward != 1000:
            await self.bot.say('**Kiawe**: You have done moderately on your trial... Here\'s what you get for that.')
            await asyncio.sleep(2)
            await self.bot.say('You recieved {0}$!'.format(reward))
            bank.deposit_credits(context.message.author, reward)
        else:
            await self.bot.say('**Kiawe**: You haven\'t done well on your trial. You get nothing!')
    @commands.command(pass_context=True)
    async def lushjungle(self, context):
        """Go on Trial Captain Mallow's trial!"""
        bank = self.bot.get_cog('Economy').bank
        await self.bot.say('**Mallow**: Hello trainer, it seems you come to face me, Mallow, the grass-type trial captain.')
        await asyncio.sleep(2)
        await self.bot.say('**Mallow**: For my trial, you have find 4 ingredients for my stew. Hurry up, my friends\'ll be coming with the other ingredients.')
        await asyncio.sleep(2)
        await self.bot.say('**Mallow**: Find these ingredients: Mago Berry, Tiny Mushroom, Revival Herb, Miracle Seed. Quick, use your Ride Stoutland!')
        await asyncio.sleep(2)

        ing1loop = 0
        ing2loop = 0
        ing3loop = 0
        ing4loop = 0
        reward = 1000
        ing1set = [
            {'name' : 'Liechi Berry', 'answer' : 'no'},
            {'name' : 'Big Root', 'answer' : 'no'},
            {'name' : 'Potion', 'answer' : 'no'},
            {'name' : 'Razz Berry', 'answer' : 'no'},
            {'name' : 'Pokeball', 'answer' : 'no'},
            {'name' : 'Repel', 'answer' : 'no'},
            {'name' : 'Mago Berry', 'answer' : 'yes'},
            {'name' : 'Oran Berry', 'answer' : 'no'},
            {'name' : 'Jaboca Berry', 'answer' : 'no'},
            {'name' : 'Lucky Egg', 'answer' : 'no'}
            ]
        ing2set = [
            {'name' : 'Liechi Berry', 'answer' : 'no'},
            {'name' : 'Big Mushroom', 'answer' : 'no'},
            {'name' : 'Awakening', 'answer' : 'no'},
            {'name' : 'Passho Berry', 'answer' : 'no'},
            {'name' : 'Pokeball', 'answer' : 'no'},
            {'name' : 'Repel', 'answer' : 'no'},
            {'name' : 'Tiny Mushroom', 'answer' : 'yes'},
            {'name' : 'Oran Berry', 'answer' : 'no'},
            {'name' : 'Payapa Berry', 'answer' : 'no'},
            {'name' : 'Lucky Egg', 'answer' : 'no'}
            ]
        ing3set = [
            {'name' : 'Vitamin', 'answer' : 'no'},
            {'name' : 'Big Root', 'answer' : 'no'},
            {'name' : 'Potion', 'answer' : 'no'},
            {'name' : 'Level Ball', 'answer' : 'no'},
            {'name' : 'Pokeball', 'answer' : 'no'},
            {'name' : 'Repel', 'answer' : 'no'},
            {'name' : 'Revival Herb', 'answer' : 'yes'},
            {'name' : 'Pamtre Berry', 'answer' : 'no'},
            {'name' : 'Nomel Berry', 'answer' : 'no'},
            {'name' : 'Lucky Egg', 'answer' : 'no'}
            ]
        ing4set = [
            {'name' : 'Liechi Berry', 'answer' : 'no'},
            {'name' : 'Big Root', 'answer' : 'no'},
            {'name' : 'Pokedoll', 'answer' : 'no'},
            {'name' : 'Razz Berry', 'answer' : 'no'},
            {'name' : 'Great ball', 'answer' : 'no'},
            {'name' : 'Max Revive', 'answer' : 'no'},
            {'name' : 'Miracle Seed', 'answer' : 'yes'},
            {'name' : 'Protein', 'answer' : 'no'},
            {'name' : 'Jaboca Berry', 'answer' : 'no'},
            {'name' : 'Lucky Egg', 'answer' : 'no'}
            ]

        await self.bot.say('First Ingredient: ``Mago Berry``')
        while ing1loop in range(0, 1):
            item = random.choice(ing1set)
            await self.bot.say('{0} You found a ``{1}``, Do you need it? (yes/no)'.format(context.message.author.mention, item['name']))
            if item['answer'] == 'yes':
                oppans = 'no'
            else:
                oppans = 'yes'
            answer = await self.bot.wait_for_message(timeout=30,
                                                     author=context.message.author)
            if answer is None:
                if item['answer'] == 'yes':
                    await self.bot.say('You needed that but **stoutland** threw it away because you said nothing!... (**-250**)')
                    if reward > 0:
                        reward = reward - 250
                    else:
                        reward = reward - 0
                else:
                    await self.bot.say('**Stoutland** threw it away because you said nothing!')
            elif answer.content.lower().strip() == item['answer']:
                if item['answer'] == 'yes':
                    await self.bot.say('You found the ``Mago Berry``! (**+250**)')
                    ing1loop = 1
                    reward = reward + 250
                else:
                    await self.bot.say('Of course you don\'t need that! You need the ``Mago Berry``!')
            elif answer.content.lower().strip() == oppans:
                if item['answer'] == 'yes':
                    await self.bot.say('You needed that but **stoutland** threw it away because you said so!... (**-250**)')
                    if reward > 0:
                        reward = reward - 250
                    else:
                        reward = reward - 0
                else:
                    await self.bot.say('You don\'t need that... (**-250**)')
            else:
                if item['answer'] == 'yes':
                    await self.bot.say('You needed that but **stoutland** threw it away because you said nothing!... (**-250**)')
                    if reward > 0:
                        reward = reward - 250
                    else:
                        reward = reward - 0
                else:
                    await self.bot.say('**Stoutland** threw it away because you said nothing!')
        await self.bot.say('Second Ingredient: ``Tiny Mushroom``')
        while ing2loop in range(0, 1):
            item = random.choice(ing2set)
            await self.bot.say('{0} You found a ``{1}``, Do you need it? (yes/no)'.format(context.message.author.mention, item['name']))
            if item['answer'] == 'yes':
                oppans = 'no'
            else:
                oppans = 'yes'
            answer = await self.bot.wait_for_message(timeout=30,
                                                     author=context.message.author)
            if answer is None:
                if item['answer'] == 'yes':
                    await self.bot.say('You needed that but **stoutland** threw it away because you said nothing!... (**-250**)')
                    if reward > 0:
                        reward = reward - 250
                    else:
                        reward = reward - 0
                else:
                    await self.bot.say('**Stoutland** threw it away because you said nothing!')
            elif answer.content.lower().strip() == item['answer']:
                if item['answer'] == 'yes':
                    await self.bot.say('You found the ``Tiny Mushroom``! (**+250**)')
                    ing2loop = 1
                    reward = reward + 250
                else:
                    await self.bot.say('Of course you don\'t need that! You need the ``Tiny Mushroom``!')
            elif answer.content.lower().strip() == oppans:
                if item['answer'] == 'yes':
                    await self.bot.say('You needed that but **stoutland** threw it away because you said so!... (**-250**)')
                    if reward > 0:
                        reward = reward - 250
                    else:
                        reward = reward - 0
                else:
                    await self.bot.say('You don\'t need that... (**-250**)')
            else:
                if item['answer'] == 'yes':
                    await self.bot.say('You needed that but **stoutland** threw it away because you said nothing!... (**-250**)')
                    if reward > 0:
                        reward = reward - 250
                    else:
                        reward = reward - 0
                else:
                    await self.bot.say('**Stoutland** threw it away because you said nothing!')
        await self.bot.say('Third Ingredient: ``Revival Herb``')
        while ing3loop in range(0, 1):
            item = random.choice(ing3set)
            await self.bot.say('{0} You found a ``{1}``, Do you need it? (yes/no)'.format(context.message.author.mention, item['name']))
            if item['answer'] == 'yes':
                oppans = 'no'
            else:
                oppans = 'yes'
            answer = await self.bot.wait_for_message(timeout=30,
                                                     author=context.message.author)
            if answer is None:
                if item['answer'] == 'yes':
                    await self.bot.say('You needed that but **stoutland** threw it away because you said nothing!... (**-250**)')
                    if reward > 0:
                        reward = reward - 250
                    else:
                        reward = reward - 0
                else:
                    await self.bot.say('**Stoutland** threw it away because you said nothing!')
            elif answer.content.lower().strip() == item['answer']:
                if item['answer'] == 'yes':
                    await self.bot.say('You found the ``Revival Herb``! (**+250**)')
                    ing3loop = 1
                    reward = reward + 250
                else:
                    await self.bot.say('Of course you don\'t need that! You need the ``Revival Herb``!')
            elif answer.content.lower().strip() == oppans:
                if item['answer'] == 'yes':
                    await self.bot.say('You needed that but **stoutland** threw it away because you said so!... (**-250**)')
                    if reward > 0:
                        reward = reward - 250
                    else:
                        reward = reward - 0
                else:
                    await self.bot.say('You don\'t need that... (**-250**)')
                    if reward > 0:
                        reward = reward - 250
                    else:
                        reward = reward - 0
            else:
                if item['answer'] == 'yes':
                    await self.bot.say('You needed that but **stoutland** threw it away because you said nothing!... (**-250**)')
                else:
                    await self.bot.say('**Stoutland** threw it away because you said nothing!')
        await self.bot.say('Fourth Ingredient: ``Miracle Seed``')
        while ing4loop in range(0, 1):
            item = random.choice(ing4set)
            await self.bot.say('{0} You found a ``{1}``, Do you need it? (yes/no)'.format(context.message.author.mention, item['name']))
            if item['answer'] == 'yes':
                oppans = 'no'
            else:
                oppans = 'yes'
            answer = await self.bot.wait_for_message(timeout=30,
                                                     author=context.message.author)
            if answer is None:
                if item['answer'] == 'yes':
                    await self.bot.say('You needed that but **stoutland** threw it away because you said nothing!... (**-250**)')
                    if reward > 0:
                        reward = reward - 250
                    else:
                        reward = reward - 0
                else:
                    await self.bot.say('**Stoutland** threw it away because you said nothing!')
            elif answer.content.lower().strip() == item['answer']:
                if item['answer'] == 'yes':
                    await self.bot.say('You found the ``Miracle Seed``! (**+250**)')
                    ing4loop = 1
                    reward = reward + 250
                else:
                    await self.bot.say('Of course you don\'t need that! You need the ``Miracle Seed``!')
            elif answer.content.lower().strip() == oppans:
                if item['answer'] == 'yes':
                    await self.bot.say('You needed that but **stoutland** threw it away because you said so!... (**-250**)')
                    if reward > 0:
                        reward = reward - 250
                    else:
                        reward = reward - 0
                else:
                    await self.bot.say('You don\'t need that... (**-250**)')
                    if reward > 0:
                        reward = reward - 250
                    else:
                        reward = reward - 0
            else:
                if item['answer'] == 'yes':
                    await self.bot.say('You needed that but **stoutland** threw it away because you said nothing!... (**-250**)')
                    if reward > 0:
                        reward = reward - 250
                    else:
                        reward = reward - 0
                else:
                    await self.bot.say('**Stoutland** threw it away because you said nothing!')
        await self.bot.say('You head back to Mallow after gathering the four ingredients...')
        await asyncio.sleep(2)
        await self.bot.say('*Kiawe and Lana come...*')
        await asyncio.sleep(2)
        await self.bot.say('**Kiawe & Lana**: We brought the ingredients you asked us for!')
        await asyncio.sleep(2)
        await self.bot.say('**Mallow**: Ah, thank you the three of you!')
        await asyncio.sleep(2)
        await self.bot.say('**Mallow**: It\'s time for me to make my stew')
        await asyncio.sleep(2)
        await self.bot.say('*Mallow makes the stew and the smell of it draws out a pokemon!*')
        await asyncio.sleep(2)
        await self.bot.say('**Mallow**: **Lurantis**!')
        await asyncio.sleep(2)
        await self.bot.say('**Lurantis** wants to fight! What will you do? (battle/run)')
        answer = await self.bot.wait_for_message(timeout=30,
                                                 author=context.message.author)
        if answer is None:
            await self.bot.say('You try to run away while **lurantis** attacks but you get away safely... (**-500**)')
            reward = reward - 500
        elif answer.content.lower().strip() == 'battle':
            await self.bot.say('You prepare for your battle...')
            await asyncio.sleep(2)
            await self.bot.say('Your **stoutland**\'s bite defeats the enemy **lurantis**! (**+500**)')
            await asyncio.sleep(2)
            await self.bot.say('You recieved the Z Crystal, Grassium-Z!')
            reward = reward + 500
        else:
             await self.bot.say('You try to run away while **lurantis** attacks but you get away safely... (**-500**)')
             reward = reward - 500
        await asyncio.sleep(2)

        #Reward Check
        if reward == 2500:
            await self.bot.say('**Mallow**: You have done excellent on your trial... Congratulations! Here\'s your reward!')
            await self.bot.say('*You got a **Lush Jungle Trial Completion Stamp**!*')
            await asyncio.sleep(2)
            await self.bot.say('You recieved {0}$!'.format(reward))
            bank.deposit_credits(context.message.author, reward)
        elif reward > 1500 and reward != 2500:
            await self.bot.say('**Mallow**: You have done moderately on your trial... Here\'s what you get for that.')
            await asyncio.sleep(2)
            await self.bot.say('You recieved {0}$!'.format(reward))
            bank.deposit_credits(context.message.author, reward)
        else:
            await self.bot.say('**Mallow**: You haven\'t done well on your trial. You get nothing!')
def setup(bot):
    bot.add_cog(IslandChallenge(bot))
