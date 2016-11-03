from discord.ext import commands
import random
import discord

class MartialArts:
    """Perform Martial Arts with this cog! Challenge someone for a karate fight or attack them!"""
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
    @commands.command(pass_context=True)
    async def onepunch(self, context, user : discord.Member):
        """Punch!"""

        if user.id == self.bot.user.id:
            await self.bot.say(context.message.author.mention + "**, how dare you try to punch me? **" + context.message.author.mention + "** has been knocked out by the virtue of Martial Arts!**")
        else:
            await self.bot.say("ONE PUNCH! " + user.mention + " has been knocked out by the virtue of Martial Arts!")
    @commands.command(pass_context=True)
    async def oneslap(self, context, user : discord.Member):
        """Slap!"""

        if user.id == self.bot.user.id:
            await self.bot.say(context.message.author.mention + "**, how dare you try to slap me? **" + context.message.author.mention + "** has been knocked out by the virtue of Martial Arts!**")
        else:
            await self.bot.say("ONE SLAP! " + user.mention + " has been knocked out by the virtue of Martial Arts!")
    @commands.command(pass_context=True)
    async def onekick(self, context, user : discord.Member):
        """Kick!"""

        if user.id == self.bot.user.id:
            await self.bot.say(context.message.author.mention + "**, how dare you try to kick me? **" + context.message.author.mention + "** has been knocked out by the virtue of Martial Arts!**")
        else:
            await self.bot.say("ONE KICK! " + user.mention + " has been knocked out by the virtue of Martial Arts!")
    @commands.command(pass_context=True)
    async def onechop(self, context, user : discord.Member):
        """Chop!"""

        if user.id == self.bot.user.id:
            await self.bot.say(context.message.author.mention + "**, how dare you try to chop me? **" + context.message.author.mention + "** has been knocked out by the virtue of Martial Arts!**")
        else:
            await self.bot.say("ONE CHOP! " + user.mention + " has been knocked out by the virtue of Martial Arts!")
def setup(bot):
    bot.add_cog(MartialArts(bot))
