from discord.ext import commands
import random
import discord

class Karate:
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def karate(self, context, user : discord.Member):
        """Fight someone using one of the twenty epic karate moves!"""
        
        outcome = [context.message.author.mention, user.mention]
        move = ['Pork Chop', 'The Punisher', 'Roundhouse Kick', 'Cereal Kill', 'Gummy Bash', 'The Whip', 'Dragon Warrior','Bacon Bonanza', 'Naughty Nunchucks', 'Microwave Munch', 'Maniac Monkey', 'Punch For Brunch', 'Stun Fun', 'Cranial Crane', 'Mega Mantis', 'Thumping Tiger', 'Legendary Linger', 'Radiant Sun', 'Cookie Crumble', 'Meat Beat']

        if user.id == self.bot.user.id:
            await self.bot.say(context.message.author.mention + "**, You tryna challenge me for a karate match? **" + context.message.author.mention + "** has been defeated with the legendary move, Bot Bash!**")
        else:
            await self.bot.say('**{0} won the karate match with their glorious {1}!**'.format(random.choice(outcome), random.choice(move)))
def setup(bot):
    bot.add_cog(Karate(bot))
