import discord
from discord.ext import commands

class Saitama:
    """Defeat anyone with the power of One Punch Man!"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def onepunch(self, context, user : discord.Member):
        """Punch!"""

        if user.id == self.bot.user.id:
            await self.bot.say(context.message.author.mention + "**, how dare you try to punch me? **" + context.message.author.mention + "** has been KO\'d with the power of One Punch Man!**")
        else:
            await self.bot.say("ONE PUNCH! " + user.mention + " has been KO'd with power of One-Punch Man!")
    @commands.command(pass_context=True)
    async def oneslap(self, context, user : discord.Member):
        """Slap!"""

        if user.id == self.bot.user.id:
            await self.bot.say(context.message.author.mention + "**, how dare you try to slap me? **" + context.message.author.mention + "** has been KO\'d with the power of One Punch Man!**")
        else:
            await self.bot.say("ONE SLAP! " + user.mention + " has been KO'd with power of One-Punch Man!")
    @commands.command(pass_context=True)
    async def onekick(self, context, user : discord.Member):
        """Kick!"""

        if user.id == self.bot.user.id:
            await self.bot.say(context.message.author.mention + "**, how dare you try to kick me? **" + context.message.author.mention + "** has been KO\'d with the power of One Punch Man!**")
        else:
            await self.bot.say("ONE KICK! " + user.mention + " has been KO'd with power of One-Punch Man!")
def setup(bot):
    bot.add_cog(Saitama(bot))
