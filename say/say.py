import discord
from discord.ext import commands

class Say:
    """Make Red say stuff!"""

    def __init__(self, bot):
        self.bot = bot
        
    @commands.command()
    async def say(self, msg : str):
        """Make Red say stuff!"""

        await self.bot.say(("{0}").format(msg))
def setup(bot):
    bot.add_cog(Say(bot))
