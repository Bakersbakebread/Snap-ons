from discord.ext import commands
import random
import discord

class CornyJokes:
    """Do ``[p]cjoke`` to get a corny joke!"""
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def cjoke(self, context):
        """Laugh at corny jokes with this command!"""
        joke = {}
        joke['1'] = '"There\'s a leek in the boat!"'
        joke['2'] = '"I went to buy some camouflage trousers but I could not find any."'
        joke['3'] = '"No one has really good science jokes anymore because all the good ones argon."'
        joke['4'] = '"You know my father threw a camera at me once, I still have flashbacks."'
        joke['5'] = 'The digital clock looked at his analog mom and said: "Look mom, no hands!"'
        joke['6'] = 'Alcohol is a perfect solvent: It dissolves marriages, families and careers.'
        joke['7'] = '"I\'m like a really down to earth guy because you know... gravity."'
        joke['8'] = '"Standing in the park, I was wondering why a Frisbee gets larger the closer it gets. Then it hit me."'
        joke['9'] = '"I needed a password eight characters long so I picked Snow White and the Seven Dwarfs."'
        joke['10'] = 'The early bird gets the worm but the late worm gets to live.'
        joke['11'] = 'I\'m on a whiskey diet. I\'ve lost three days already.'
        joke['12'] = 'Two fish were in a tank. One said "You man the guns, I\'ll drive!"'
        joke['13'] = 'Two peanuts were walking down the street. One was a salted.'
        joke['14'] = '"I quit my job at the helium factory today because I refuse to be spoken to in that tone of voice."'
        joke['15'] = '"So, I thought about going as a ghost for Halloween, but I figured meh, I\'ll kill myself next year."'
        joke['16'] = '"Did you hear about the restaurant on the moon? Great food but no atmosphere."'
        joke['17'] = '"I tried to take a picture of some fog. I mist."'
        joke['18'] = 'Two antennas got married. The ceremony wasn\'t much but the reception was excellent.'
        joke['19'] = '"I have a lot of jokes about unemployed people, but none of them work."'
        joke['20'] = '"An old lady at the bank asked me if I could help her check her balance. So I pushed her over."'
        joke['21'] = '"We don\'t have any vegetable jokes, if you get one lettuce know."'

        await self.bot.say('**{0}**'.format(random.choice([joke[i] for i in joke])))

def setup(bot):
    bot.add_cog(CornyJokes(bot))
