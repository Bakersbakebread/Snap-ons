import discord
from discord.ext import commands

class SCP:
    """Look up SCP articles. Warning: Some of them may be too creepy or gruesome."""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def scp(self, num : int):
        """Look up SCP articles. Warning: Some of them may be too creepy or gruesome. Reminder: You must specify a number between 1 and 3999."""

        #Thanks Shigbeard and Redjumpman for helping me!

        if (num > 0 and num <= 3999):
             msg = "http://www.scp-wiki.net/scp-{:03}".format(num)
        else:
             msg = "You must specify a number between 1 and 3999"

        await self.bot.say(msg)

    @commands.command()
    async def scpj(self, joke : str):
        """Look up SCP-Js. Reminder: Enter the correct name or else the resultant page will be invalid. (Use 001, etc. in case of numbers less than 100.)"""

        await self.bot.say(("http://www.scp-wiki.net/scp-{}-j").format(joke))

    @commands.command()
    async def scparc(self, num : int):
        """Look up SCP archives. Warning: Some of them may be too creepy or gruesome. Reminder: You must specify a valid archive number. (13, 48, 51, 89, 91, 112, 132, 138, 157, 186, 232, 234, 244, 252, 257, 338, 356, 361, 400, 406, 503, 515, 517, 578, 728, 744, 776, 784, 837, 922, 987, 1023)"""

        if num in (13, 48, 51, 89, 91, 112, 132, 138, 157, 186, 232, 234, 244, 252, 257, 338, 356, 361, 400, 406, 503, 515, 517, 578, 728, 744, 776, 784, 837, 922, 987, 1023):
             msg = "http://www.scp-wiki.net/scp-{:03}-arc".format(num)
        else:
             msg = "You must specify a valid archive number."

        await self.bot.say(msg)

    @commands.command()
    async def scpex(self, num : int):
        """Look up explained SCP articles. Warning: Some of them may be too creepy or gruesome. Reminder: You must specify a valid archive number. (711, 920, 1841, 1851, 1974, 2600, 4023, 8900)"""

        if num in (711, 920, 1841, 1851, 1974, 2600, 4023, 8900):
             msg = "http://www.scp-wiki.net/scp-{:03}-ex".format(num)
        else:
             msg = "You must specify a valid article number."

        await self.bot.say(msg)

    @commands.command()
    async def anomalousitems(self):
        """Look through the log of anomalous items."""

        await self.bot.say("""http://www.scp-wiki.net/log-of-anomalous-items""")

    @commands.command()
    async def extranormalevents(self):
        """Look through the log of extranormal events."""

        await self.bot.say("""http://www.scp-wiki.net/log-of-extranormal-events""")

    @commands.command()
    async def unexplainedlocations(self):
        """Look through the log of unexplained locations."""

        await self.bot.say("""http://www.scp-wiki.net/log-of-unexplained-locations""")


def setup(bot):
    bot.add_cog(SCP(bot))
