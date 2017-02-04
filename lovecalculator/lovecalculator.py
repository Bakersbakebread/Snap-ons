import discord
from discord.ext import commands
try: # check if BeautifulSoup4 is installed
    from bs4 import BeautifulSoup
    soupAvailable = True
except:
    soupAvailable = False
import urllib.request

class LoveCalculator:
    """Calculate the love percentage for two users!"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['lovecalc'])
    async def lovecalculator(self, user1: discord.Member, user2: discord.Member):
        """Calculate the love percentage!"""

        x = user1.name
        y = user2.name
        if user1.nick:
            x = user1.nick
        if user2.nick:
            y = user2.nick
        name1 = x.replace(" ", "+")
        name2 = y.replace(" ", "+")

        url = 'https://www.lovecalculator.com/love.php?name1={}&name2={}'.format(name1, name2)
        soupObject = BeautifulSoup(urllib.request.urlopen(url).read(), 'html.parser')
        description = soupObject.find('div', attrs={'class': 'result score'}).get_text().strip()

        z = description[:3]
        z = int(z)
        if z > 50:
            emoji = '❤'
        else:
            emoji = '💔'
        title = 'Dr. Love says that the love percentage for {} and {} is:'.format(x, y)
        description = emoji + ' ' + description + ' ' + emoji
        em = discord.Embed(title=title, description=description, color=discord.Color.red())
        await self.bot.say(embed=em)

def setup(bot):
    if soupAvailable:
        bot.add_cog(LoveCalculator(bot))
    else:
        raise RuntimeError("You need to run `pip3 install beautifulsoup4`")
