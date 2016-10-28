import discord
from discord.ext import commands

class Say:
    """Make Red say stuff! Remember, enclose the sentence you want Red to say in double quotes."""

    def __init__(self, bot):
        self.bot = bot
        
    @commands.command()
    async def say(self, msg : str):
        """Make Red say stuff! Remember, enclose the sentence you want Red to say in double quotes."""

        await self.bot.say(("{0}").format(msg))
def setup(bot):
    bot.add_cog(Say(bot))