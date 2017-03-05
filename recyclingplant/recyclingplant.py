from discord.ext import commands
import random


class RecyclingPlant:
    """Apply for a job at the recycling plant!"""
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def recyclingplant(self, context):
        """Apply for a job at the recycling plant!"""
        x = 0
        can = [
            {'object': 'Apple Core', 'action': 'trash'},
            {'object': 'Paper Cup', 'action': 'recycle'},
            {'object': 'Banana Peel', 'action': 'trash'},
            {'object': 'Paper Bag', 'action': 'recycle'},
            {'object': 'Old Taco', 'action': 'trash'},
            {'object': 'Newspaper', 'action': 'recycle'},
            {'object': 'Chewed Gum', 'action': 'trash'},
            {'object': 'Polythene Bag', 'action': 'recycle'},
            {'object': 'Rotten Eggs', 'action': 'trash'},
            {'object': 'Outdated Telephone Directory', 'action': 'recycle'},
            {'object': 'Stale Bread', 'action': 'trash'},
            {'object': 'Used Notebook', 'action': 'recycle'},
            {'object': 'Sour Milk', 'action': 'trash'},
            {'object': 'Old Textbook', 'action': 'recycle'},
            {'object': 'Week-Old Sandwich', 'action': 'trash'},
            {'object': 'Paper Ball', 'action': 'recycle'},
            {'object': 'Leftovers', 'action': 'trash'},
            {'object': 'Toy Car', 'action': 'recycle'},
            {'object': 'Fish Bones', 'action': 'trash'},
            {'object': 'Superhero Costume', 'action': 'recycle'},
            {'object': 'Dirty Diaper', 'action': 'trash'},
            {'object': 'Silcone Mould', 'action': 'recycle'},
            {'object': 'Mouldy Broccoli', 'action': 'trash'},
            {'object': 'TV Remote', 'action': 'recycle'},
            {'object': 'Withered Rose Bouquet', 'action': 'trash'},
            {'object': 'Paper Plate', 'action': 'recycle'},
            {'object': 'Slimy Bacon', 'action': 'trash'},
            {'object': 'Folders', 'action': 'recycle'},
            {'object': 'Fly Agaric Mushrooms', 'action': 'trash'},
            {'object': 'Phone case', 'action': 'recycle'},
            {'object': 'Napkins', 'action': 'trash'},
            {'object': 'Broken Dualshock 4 Controller', 'action': 'recycle'},
            {'object': 'Wax Paper', 'action': 'trash'},
            {'object': 'iPad', 'action': 'recycle'},
            {'object': 'Paint Can', 'action': 'trash'},
            {'object': 'Glass Bottle', 'action': 'recycle'},
            {'object': 'Light Bulb', 'action': 'trash'},
            {'object': 'Nintendo 3DS', 'action': 'recycle'},
            {'object': 'Styrofoam Container', 'action': 'trash'},
            {'object': 'Flash Cards', 'action': 'recycle'},
            {'object': 'Motor Oil Can', 'action': 'trash'},
            {'object': 'Candy Wrapper', 'action': 'recycle'},
            {'object': 'Waxed Cardboard', 'action': 'trash'},
            {'object': 'Empty Bottle', 'action': 'recycle'},
            {'object': 'Used Toilet Paper', 'action': 'trash'},
            {'object': 'Outdated Calendar', 'action': 'recycle'},
            {'object': 'Ceramic Mug', 'action': 'trash'},
            {'object': 'Plastic Cup', 'action': 'recycle'},
            {'object': 'Gift Wrapping', 'action': 'trash'},
            {'object': 'Soda Bottle', 'action': 'recycle'}
              ]
        await self.bot.say('{0} has signed up for a shift at the Recycling Plant! Type ``exit`` to terminate it early.'.format(context.message.author.mention))
        while x in range(0, 10):
            used = random.choice(can)
            reward = 0
            if used['action'] == 'trash':
                opp = 'recycle'
            else:
                opp = 'trash'
            await self.bot.say('``{0}``! Will {1} ``trash`` it or ``recycle`` it?'.format(used['object'], context.message.author.mention))
            answer = await self.bot.wait_for_message(timeout=10,
                                                     author=context.message.author)
            if answer is None:
                await self.bot.say('``{0}`` fell down the conveyor belt to be sorted again!'.format(used['object']))
            elif answer.content.lower().strip() == used['action']:
                await self.bot.say('Congratulations! You put ``{0}`` down the correct chute! (**+50**)'.format(used['object']))
                reward = reward + 50
                x += 1
            elif answer.content.lower().strip() == opp:
                await self.bot.say('{0}, you little brute, you put it down the wrong chute! (**-50**)'.format(context.message.author.mention))
                reward = reward - reward
            elif answer.content.lower().strip() == 'exit':
                await self.bot.say('{0} has been relived of their duty.'.format(context.message.author.mention))
                break
            else:
                await self.bot.say('``{0}`` fell down the conveyor belt to be sorted again!'.format(used['object']))
        else:
            bank = self.bot.get_cog('Economy').bank
            if reward < 0:
                bank.deposit_credits(context.message.author, 0)
            else:
                bank.deposit_credits(context.message.author, reward)
            await self.bot.say('You have been given **{0}$** for your services.'.format(reward))


def setup(bot):
    bot.add_cog(RecyclingPlant(bot))
