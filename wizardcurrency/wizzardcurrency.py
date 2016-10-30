import discord
from discord.ext import commands

class WizardCurrency:
    """ʛ: Convert Real Life currencies into Galleons and Vice Versa! To get started, use ``[p]wizconvert``"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def wizconvert(self, src : str, fnl : str, amt : float):
        """ʛ: Convert Real Life currencies into Galleons and Vice Versa! Supported Currencies: ``galleon, pound (uk), dollar (us), yen, rupee (in), euro (eu), ruble (ru), real (br), peso (ph)``"""
        if (src == 'galleon' and fnl == 'pound'):
            ans = amt*4.93
        elif (src == 'pound' and fnl == 'galleon'):
            ans = amt/4.93
        elif (src == 'galleon' and fnl == 'dollar'):
            ans = amt*7.35
        elif (src == 'dollar' and fnl == 'galleon'):
            ans = amt/7.35
        elif (src == 'galleon' and fnl == 'yen'):
            ans = amt*653.66
        elif (src == 'yen' and fnl == 'galleon'):
            ans = amt/653.66
        elif (src == 'galleon' and fnl == 'rupee'):
            ans = amt*354.67
        elif (src == 'rupee' and fnl == 'galleon'):
            ans = amt/354.67
        elif (src == 'galleon' and fnl == 'euro'):
            ans = amt*5.90
        elif (src == 'euro' and fnl == 'galleon'):
            ans = amt/5.90
        elif (src == 'galleon' and fnl == 'ruble'):
            ans = amt*436,27
        elif (src == 'ruble' and fnl == 'galleon'):
            ans = amt/436,27
        elif (src == 'galleon' and fnl == 'real'):
            ans = amt*19.87
        elif (src == 'real' and fnl == 'galleon'):
            ans = amt/19.87
        elif (src == 'galleon' and fnl == 'peso'):
            ans = amt*342.24
        elif (src == 'peso' and fnl == 'galleon'):
            ans = amt/342.24
        else:
            ans = "Source currency and Final currency can only be one of the following: ``galleon, pound (uk), dollar (us), yen, rupee (in), euro (eu), ruble (ru), real (br), peso (ph)``"
        await self.bot.say(ans)

def setup(bot):
    bot.add_cog(WizardCurrency(bot))
