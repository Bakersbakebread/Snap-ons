import discord
from discord.ext import commands
import random
import asyncio

class FNAF:
    """Play as a night guard at Freddy Fazbear's Pizzeria."""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def fnaf(self, context):
        """Play as a night guard at Freddy Fazbear's Pizzera. Type exit to quit."""
        user = context.message.author
        entry = [
            'left hallway'
            'vents'
            'right hallway'
            ]
        events = [
            {
                'animatronic' : 'Freddy',
                'location' : 'On the Stage',
                'kill' : 'drains all your power'
            },
            {
                'animatronic' : 'Bonnie',
                'location' : 'On the Stage',
                'kill' : 'smashes your head with his guitar'
            },
            {
                'animatronic' : 'Chica',
                'location' : 'on the Stage',
                'kill' : 'throws her chomping cupcake on you'
            },
            {
                'animatronic' : 'Foxy',
                'location' : 'at the Pirate Cove',
                'kill' : 'hits you with his hook'
            }
            ]
        loop = 0

        await self.bot.say('Welcome to Freddy Fazbear\'s Pizzeria, ' + user.name)
        await asyncio.sleep(2)
        await self.bot.say('You have to survive, I mean work, as a night guard at the pizzeria.')
        
        while loop in range(0, 6):
            wait1 = random.randint(15, 30)
            wait2 = random.randint(15, 30)
            print('Time = ' + loop + ':00 AM')
            loop  = loop + 1
            if loop < 6:
                await asyncio.sleep(wait1)
                encounter = random.choice(events)
                chosen_entry = random.choice(entry)
                await self.bot.say('You see ' + encounter['animatronic'] + ' ' + encounter['location'])
                await asyncio.sleep(1)
                await self.bot.say('You hear footsteps coming from the ' + chosen_entry)
                await self.bot.say('What would you like to do? Enter the number corresponding to the option.')
                await self.bot.say('```1. Shine the torch in the vents and close the vent \n2. Close the left door \n3. Close the right door \n4. Watch Hotel Transylvania 2 \n5. Quit```')
                if chosen_entry == entry[0]:
                    ans = 2
                elif chosen_entry == entry[1]:
                    ans = 1
                else:
                    ans = 3
                await asyncio.sleep(wait2)
                answer = await self.bot.wait_for_message(timeout=10,
                                                         author=context.message.author)
                if answer is None:
                    await self.bot.say(encounter['animatronic'] + " " + encounter["kill"])
                    break
                elif answer.content.lower().strip() == ans:
                    await self.bot.say("You shut out" + encounter['animatronic'] + "successfully.")
                elif answer.content.lower().strip() == "quit":
                    break
                else:
                    await self.bot.say(encounter['animatronic'] + " " + encounter["kill"])
                    break
            elif loop = 6:
                bank = self.bot.get_cog('Economy').bank
                bank.deposit_credits(context.message.author, 120)
                await self.bot.say('Congratulations! You have completed your shift. Enjoy some time at your home!')
                await self.bot.say('```Paycheck: 120$ recieved.```')
            else:
                break
def setup(bot):
    bot.add_cog(FNAF(bot))
