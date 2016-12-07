import discord
from discord.ext import commands
import random

class MadLibs:
    """Check if a website is down for everyone or just for you or check about a website's safety."""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def madlibs(self, name : str, verb_past : str, adjective : str, profession : str, food : str, location : str, number : int, thing_plural : str, body_part : str, famous_person : str):
        """Play the old school book game, Mad Libs, now on discord!. Use "" to enter stuff that is two words or longer."""

        #Data input reference:
        # {0} = 'name'
        # {1} = 'verb_past'
        # {2} = 'adjective'
        # {3} = 'profession'
        # {4} = 'food'
        # {5} = 'location'
        # {6} = 'number'
        # {7} = 'thing_plural'
        # {8} = 'body_part'
        # {9} = 'famous_person'

        lib = {}
        lib['1'] = '{0} is our {3}. He {1} us once for throwing his {4} at {9}\'s {8} when we met them at the {2} {5}. They also threw {6} {7} at us for that.'
        lib['2'] = 'While I was at {5} with {0} {6} days ago, I met the famous {3}, {9}. But while I was trying to get an autograph on my {8}, we spilt {2} {7} and {4} on them. They {1} us for that.'
        lib['3'] = '{0} {1} {3} {9}, who was eating {4}, with their {6} {7} at {5}. They got their {2} {8} cut off for that. I guess, R.I.P.?'
        lib['4'] = '{0} {1} {9} because they were given a dare while playing Truth or Dare at {5} with the {3} and {9}. They had to do {6} {2} dares including {7} and {4}.'
        lib['5'] = '{9} held a halloween party at {5}. It was {2} and they invited me and {3} {0}. They served {6} {7} and {4} which had to be {1} using one\'s {8}.'
        lib['6'] = '{0} and {9} went on an easter egg hunt at the {3}\'s {5}. They {1} {2} {4}, {8} and {7} from the eggs.'
        lib['7'] = '{0} became a {2} {3} after they were {2} by {9}. They now work at {8} {5} and have {4} with {6} {7} for lunch.'
        lib['8'] = '{0} and Luigi {1} Bowser\'s {2} {8} to save {3} {9} from Bowser\'s {5}, which was actually made from {6} {7}. The gang had {4} after their win!'
        lib['9'] = 'I once visited {3} {8} {9}\'s {2} concert at {5}. I had to send {6} entries to get my tickets and I {1} my best friend, {0}. We had {4} and we were also given {7]!'
        lib['10'] = 'I {1} {9} in {5} and after {6} weeks, they sold them. Their {8} was missing after they were fed {4} and {2}  {7}! Of course the buyer, {3} {0} was ripped off!'
        
        usedlib = random.choice([lib[i] for i in lib])
        madlib = usedlib.format(name, verb_past, adjective, profession, food, location, number, thing_plural, body_part, famous_person)

        await self.bot.say('``{0}``'.format(madlib))
def setup(bot):
    bot.add_cog(MadLibs(bot))
