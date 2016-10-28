from discord.ext import commands
import random
import discord

class GGEZ:
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def ggez(self, context):
        """Get one of the 10 random gg ez filter messages from Overwatch!"""
        troll = context.message.author.mention
        message = {}
        message['1'] = 'I feel very, very small... please hold me...'
        message['2'] = 'It\'s past my bedtime. Please don\'t tell my mommy.'
        message['3'] = 'I\'m wrestling with some insecurity issues in my life but thank you for playing with me.'
        message['4'] = 'I\'m trying to be a nicer person. It\'s hard, but I\'m trying, guys.'
        message['5'] = 'Gee whiz! That was fun. Good playing!'
        message['6'] = 'For glory and honor! Huzzah comrades!'
        message['7'] = 'Well played. I salute you all.'
        message['8'] = 'Aw shucks... You guys are the best!'
        message['9'] = 'Mommy says people my age shouldn\'t suck their thumbs.'
        message['10'] = 'Wishing you all the best.'


        await self.bot.say('{0}: *{1}*'.format(troll, random.choice([message[i] for i in message])))

def setup(bot):
    n = GGEZ(bot)
    bot.add_cog(n)
