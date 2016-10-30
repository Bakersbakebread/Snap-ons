import discord
from discord.ext import commands

class Saitama:
    """Defeat anyone with the power of One Punch Man!"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def onepunch(self, user : discord.Member):
        """Punch!"""

        await self.bot.say("ONE PUNCH!" + user.mention + " has been KO'd with power of One-Punch Man!")
    @commands.command()
    async def oneslap(self, user : discord.Member):
        """Slap!"""

        await self.bot.say("ONE SLAP!" + user.mention + " has been KO'd with power of One-Punch Man!")
    @commands.command()
    async def onekick(self, user : discord.Member):
        """Kick!"""

        await self.bot.say("ONE KICK!" + user.mention + " has been KO'd with power of One-Punch Man!")

def setup(bot):
    bot.add_cog(Saitama(bot))
