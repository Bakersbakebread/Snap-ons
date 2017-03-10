from discord.ext import commands
from cogs.utils.dataIO import dataIO
from cogs.utils import checks
import random
import os


class MadLibs:
    """Play the old school book game, Mad Libs, now on discord!"""

    def __init__(self, bot):
        self.bot = bot
        self.madlibs = dataIO.load_json('data/madlibs/madlibs.json')

    @commands.command()
    async def madlibs(self, name : str, verb_past : str, adjective : str, profession : str, food : str, location : str, number : int, thing_plural : str, body_part : str, famous_person : str):
        """Play the old school book game, Mad Libs, now on discord! Use "" to enter stuff that is two words or longer."""
        
        if self.madlibs == []:
            await self.bot.say('``Error: No libs found.``')
        else:
            madlib = random.choice(self.madlibs).format(name, verb_past, adjective, profession, food, location, number, thing_plural, body_part, famous_person)
            await self.bot.say('``{0}``'.format(madlib))

    @commands.command(pass_context=True)
    @checks.is_owner()
    async def addlib(self, context, *, lib : str):
        """Add your madlib. Data input reference (Using all of them is not required.):
        {0} = 'name'
        {1} = 'verb_past'
        {2} = 'adjective'
        {3} = 'profession'
        {4} = 'food'
        {5} = 'location'
        {6} = 'number'
        {7} = 'thing_plural'
        {8} = 'body_part'
        {9} = 'famous_person'"""
        self.kills.append(lib)
        dataIO.save_json('data/madlibs/madlibs.json', self.madlibs)


def check_folder():
    if not os.path.exists('data/madlibs'):
        print('Creating data/madlibs folder...')
        os.makedirs('data/madlibs')


def check_file():
    if not dataIO.is_valid_json('data/madlibs/madlibs.json'):
        print('Creating default kill.json...')
        dataIO.save_json('data/madlibs/madlibs.json', [])
        
        
def setup(bot):
    bot.add_cog(MadLibs(bot))
