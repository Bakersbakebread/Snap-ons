import discord
from discord.ext import commands

class SCP:
    """Look up SPC articles. Warning: Some of them may be too creepy or gruesome."""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def scp(self, num : int):
        """Look up SPC articles. Warning: Some of them may be too creepy or gruesome. Reminder: You must specify a number between 1 and 2999"""

        #Thanks Shigbeard and Redjumpman for helping me!

        if (num > 0 and num <= 2999):
             msg = "http://www.scp-wiki.net/scp-{0:03}".format(num)
        else:
             msg = "You must specify a number between 1 and 2999"

        await self.bot.say(msg)
def setup(bot):
    bot.add_cog(SCP(bot))
