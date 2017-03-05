from discord.ext import commands
import random


class MadLibs:
    """Play the old school book game, Mad Libs, now on discord!"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def madlibs(self, name : str, verb_past : str, adjective : str, profession : str, food : str, location : str, number : int, thing_plural : str, body_part : str, famous_person : str):
        """Play the old school book game, Mad Libs, now on discord! Use "" to enter stuff that is two words or longer."""

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

        lib = [
            "{0} was slapped by their mom because they were running around showing their {8}",
            "{4} was the only thing that the {3} {1} in 2015.",
            "{0} met {9} at {5}.",
            "{0} threw {6} {7} at {9}.",
            "{0} told his friend that he liked her {8}.",
            "{9} is on an extreme diet of {7} and {4}.",
            "{0} said that green is not a {2} color.",
            "{6} is my favourite number.",
            "{0} said that {5} is haunted by the ghost of {9}.",
            "{9} had a party at {5}. {0} was invited but not me."
        ]
        
        madlib = random.choice(lib).format(name, verb_past, adjective, profession, food, location, number, thing_plural, body_part, famous_person)
        await self.bot.say('``{0}``'.format(madlib))
        
        
def setup(bot):
    bot.add_cog(MadLibs(bot))
