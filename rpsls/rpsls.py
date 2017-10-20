from cogs.utils.dataIO import dataIO
from discord.ext import commands
import discord
import os
import random
import asyncio


class RPSLS:
    """Play Rock Paper Scissors Lizard Spock."""

    def __init__(self, bot):
        self.bot = bot
        self.weaknesses = dataIO.load_json('data/rpsls/weaknesses.json')

    @commands.command()
    async def rpsls(self, choice: str):
        """Play Rock Paper Scissors Lizard Spock by Sam Kass in Discord! Rules:\nScissors cuts Paper\nPaper covers Rock\nRock crushes Lizard\nLizard poisons Spock\nSpock smashes Scissors\nScissors decapitates Lizard\nLizard eats Paper\nPaper disproves Spock\nSpock vaporizes Rock\nAnd as it has always Rock crushes Scissors"""
        check = True
        playerchoice = choice.lower()
        if playerchoice == 'rock':
            playeremote = ':moyai:'
        elif playerchoice == 'spock':
            playeremote = ':vulcan:'
        elif playerchoice == 'paper':
            playeremote = ':page_facing_up:'
        elif playerchoice in ['scissors', 'lizard']:
            playeremote = ':{}:'.format(playerchoice)
        else:
            message = 'Invalid choice.'
            em = discord.Embed(description=message, color=discord.Color.red())
            await self.bot.say(embed=em)
            check = False
        if check:
            botchoice = random.choice(['rock', 'paper', 'scissors', 'lizard', 'spock'])
            if botchoice == 'rock':
                botemote = ':moyai:'
            elif botchoice == 'spock':
                botemote = ':vulcan:'
            elif botchoice == 'paper':
                botemote = ':page_facing_up:'
            else:
                botemote = ':{}:'.format(botchoice)
            message = '{} vs. {}, who will win?'.format(playeremote, botemote)
            em = discord.Embed(description=message, color=discord.Color.blue())
            await self.bot.say(embed=em)
            await asyncio.sleep(2)
            if playerchoice in self.weaknesses[botchoice]:
                message = 'You win! :sob:'
                emcolor = discord.Color.green()
            elif botchoice in self.weaknesses[playerchoice]:
                message = 'I win! :smile:'
                emcolor = discord.Color.red()
            else:
                message = 'It\'s a draw! :neutral_face:'
                emcolor = discord.Color.blue()
            em = discord.Embed(description=message, color=emcolor)
            await self.bot.say(embed=em)


def check_folder():
    if not os.path.exists('data/rpsls'):
        print('Creating data/rpsls folder...')
        os.makedirs('data/rpsls')


def setup(bot):
    check_folder()
    bot.add_cog(RPSLS(bot))
