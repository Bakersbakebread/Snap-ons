import discord
from discord.ext import commands

class FictionalCurrency:
    """Convert Real Life currencies into Victional Currencies and Vice Versa! Supported Currencies: ``pound (uk), dollar (us)"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def wizconvert(self, src : str, fnl : str, amt : float):
        """ʛ: Convert Real Life currencies into Galleons and Vice Versa!"""
        if (src == 'galleon' and fnl == 'pound'):
            ans = amt*4.93
        elif (src == 'pound' and fnl == 'galleon'):
            ans = amt/4.93
        elif (src == 'galleon' and fnl == 'dollar'):
            ans = amt*7.35
        elif (src == 'dollar' and fnl == 'galleon'):
            ans = amt/7.35
        else:
            ans = "Source currency and Final currency can only be one of the following: ``galleon, pound (uk), dollar (us)``"
        await self.bot.say(ans)
    @commands.command()
    async def galconvert(self, src : str, fnl : str, amt : float):
        """Convert Real Life currencies into Galactic Credits Standard and Vice Versa!"""
        if (src == 'galacticcredit' and fnl == 'pound'):
            ans = amt*0.64
        elif (src == 'pound' and fnl == 'galacticcredit'):
            ans = amt/0.64
        elif (src == 'galacticcredit' and fnl == 'dollar'):
            ans = amt*1.01
        elif (src == 'dollar' and fnl == 'galacticcredit'):
            ans = amt/1.01
        else:
            ans = "Source currency and Final currency can only be one of the following: ``galacticcredit, pound (uk), dollar (us)``"
        await self.bot.say(ans)
    @commands.command()
    async def flintconvert(self, src : str, fnl : str, amt : float):
        """Convert Real Life currencies into Clams and Vice Versa!"""
        if (src == 'clam' and fnl == 'pound'):
            ans = amt*2.06
        elif (src == 'pound' and fnl == 'clam'):
            ans = amt/2.06
        elif (src == 'clam' and fnl == 'dollar'):
            ans = amt*3.2
        elif (src == 'dollar' and fnl == 'clam'):
            ans = amt/3.2
        else:
            ans = "Source currency and Final currency can only be one of the following: ``clam, pound (uk), dollar (us)``"
        await self.bot.say(ans)
    @commands.command()
    async def nukaconvert(self, src : str, fnl : str, amt : float):
        """Convert Real Life currencies into Bottle caps and Vice Versa!"""
        if (src == 'bottlecap' and fnl == 'pound'):
            ans = amt*4.93
        elif (src == 'pound' and fnl == 'bottlecap'):
            ans = amt/4.93
        elif (src == 'bottlecap' and fnl == 'dollar'):
            ans = amt*7.35
        elif (src == 'dollar' and fnl == 'bottlecap'):
            ans = amt/7.35
        else:
            ans = "Source currency and Final currency can only be one of the following: ``bottlecap, pound (uk), dollar (us)``"
        await self.bot.say(ans)
    @commands.command()
    async def zeldaconvert(self, src : str, fnl : str, amt : float):
        """Convert Real Life currencies into Rupees and Vice Versa!"""
        if (src == 'rupee' and fnl == 'pound'):
            ans = amt*0.03
        elif (src == 'pound' and fnl == 'rupee'):
            ans = amt/0.03
        elif (src == 'rupee' and fnl == 'dollar'):
            ans = amt*0.04
        elif (src == 'dollar' and fnl == 'rupee'):
            ans = amt/0.04
        else:
            ans = "Source currency and Final currency can only be one of the following: ``rupee, pound (uk), dollar (us)``"
        await self.bot.say(ans)
def setup(bot):
    bot.add_cog(FictionalCurrency(bot))
