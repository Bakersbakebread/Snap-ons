from discord.ext import commands
import random
import discord

class Interactions:
    def __init__(self, bot):
        self.bot = bot

        #SFW version of kill commond by PaddoCogs. Thanks Kowlin, Twentysix, and Redjumpman for line 43.

    @commands.command(pass_context=True)
    async def kill(self, context, member : discord.Member):
        """Wanna kill someone? Wanna be the troll kind? You've got the perfect cog for the lulz! 25 unique and funny kill commands!"""
        killer = context.message.author.mention
        victim = member.mention
        technique = {}
        technique['1'] = '{0} shoots  in {1}\'s mouth with rainbow laser, causing {1}\'s head to explode with rainbows and {1} is reborn as unicorn. :unicorn:'.format(killer, victim)
        technique['2'] = '{0} ate a piece of exotic butter. It was so amazing that it killed him.'.format(victim)
        technique['3'] = '{0} is stuffed into a suit by Freddy on their night guard duty. Oh, not those animatronics again!'.format(victim)
        technique['4'] = '{0} grabs {1} and shoves them into an auto-freeze machine with some juice and sets the temperature to 100 Kelvin, creating human ice pops.'.format(killer, victim)
        technique['5'] = '{0} drowns {1} in a tub of hot chocolate. *"How was your last drink?"*'.format(killer, victim)
        technique['6'] = '{0} screams in terror as they accidentally spawn in the cthulhu while uttering random latin words. Cthulhu grabs {0} by the right leg and takes them to his dimension yelling,"Honey, Dinner\'s ready!"'.format(victim)
        technique['7'] = '{0} feeds toothpaste-filled oreos to {1}, who were apparently allergic to fluorine. GGWP.'.format(killer, victim)
        technique['8'] = '{0} forgot to zombie-proof {1}\'s lawn... Looks like zombies had a feast last night.'.format(killer, victim)
        technique['9'] = '{0} cranks up the music system only to realize the volume was at max and the song playing was Baby by Justin Beiber...'.format(victim)
        technique['10'] = '{0} presses a random button and is teleported to the height of 100m, allowing them to fall to their inevitable death. Moral of the story: Don\'t go around pressing random buttons.'.format(victim)
        technique['11'] = '{0} is injected with chocolate syrup, which mutates them into a person made out of chocolate. While doing a part-time job at the Daycare, they are devoured by the hungry babies. :chocolate_bar:'.format(victim)
        technique['12'] = '{0} is sucked into Minecraft. {0}, being a noob at the so called "Real-Life Minecraft" faces the Game Over screen.'.format(victim)
        technique['13'] = '{0} turns on Goosebumps(2015 film) on the TV. {1} being a scaredy-cat, dies of an heart attack.'.format(killer, victim)
        technique['14'] = '{0} after a long day, plops down on the couch with {1} and turns on The Big Bang Theory. After a Sheldon Cooper joke, {1} laughs uncontrollably as they die.'.format(killer, victim)
        technique['15'] = '{0} was given a chance to synthesize element 119 (Ununennium) and have it named after them, but they messed up. R.I.P.'.format(victim)
        technique['16'] = '{0} gets {1} to watch anime with them. {1} couldn\'t handle it.'.format(killer, victim)
        technique['17'] = '{0} tried to get crafty, but they accidentally cut themselves with the scissors.:scissors:'.format(victim)
        technique['18'] = '{0} goes genocide and Sans totally dunks {0}!'.format(victim)
        technique['19'] = '{0} was so swag that {1} died due to it. #Swag'.format(killer, victim)
        technique['20'] = '{0} has been found guilty, time for their execution!'.format(victim)
        technique['21'] = '{0} fell down a cliff while playing Pokemon Go. Good job on keeping your nose in that puny phone. :iphone:'.format(victim)
        technique['22'] = '{0} strikes {1} with the killing curse... *"Avada Kedavra!"*'.format(killer, victim)
        technique['23'] = '{0} ate an apple and turned out it was made out of wax. Someone died from wax poisoning later that day.'.format(victim)
        technique['24'] = '{0} was teleported to the timeline where Jurassic World was real and they were eaten alive by the Indominus Rex.'.format(victim)
        technique['25'] = '{0} was charging their Samsung Galaxy Note 7...'.format(victim)

        if member.id == self.bot.user.id:
            await self.bot.say('**{0}, how dare you try to kill me? DIE!**'.format(killer))
        else:
            await self.bot.say('**{0}**'.format(random.choice([technique[i] for i in technique])))
    @commands.command(pass_context=True)
    async def interact(self, context, member : discord.Member):
        """Interact with the user you mention."""
        executer = context.message.author.mention
        user = member.mention
        
        interaction = {}
        interaction['1'] = '{0} winks at {1}.'.format(executer, user)
        interaction['2'] = '{0} hugs {1}.'.format(executer, user)
        interaction['3'] = '{0} shakes hands with {1}.'.format(executer, user)
        interaction['4'] = '{0} bows down to {1}.'.format(executer, user)
        interaction['5'] = '{0} pokes {1}.'.format(executer, user)
        interaction['6'] = '{0} tickles {1}.'.format(executer, user)
        interaction['7'] = '{0} slaps {1}.'.format(executer, user)
        interaction['8'] = '{0} scratches {1}.'.format(executer, user)
        interaction['9'] = '{0} bites {1}.'.format(executer, user)
        interaction['10'] = '{0} sells {1} for a dime.'.format(executer, user)
        interaction['11'] = '{0} canes {1}.'.format(executer, user)
        interaction['12'] = '{0} whips {1}.'.format(executer, user)
        interaction['13'] = '{0} restrains {1}'.format(executer, user)
        interaction['14'] = '{0} kneels down to {1}.'.format(executer, user)
        interaction['15'] = '{0} gets the box of toys out from {1}.'.format(executer, user)
        interaction['16'] = '{0} ties up {1}.'.format(executer, user)
        interaction['17'] = '{0} ties up and tickles {1}.'.format(executer, user)
        interaction['18'] = '{0} kisses {1}.'.format(executer, user)
        interaction['19'] = '{0} meows at {1}.'.format(executer, user)
        interaction['20'] = '{0} maow meeeeeeoooooows at {1}.'.format(executer, user)
        interaction['21'] = '{0} purrs at {1}.'.format(executer, user)
        interaction['22'] = '{0} wuffs at {1}.'.format(executer, user)
        interaction['23'] = '{0} wwwwuuuuuuuuuffff wwwwuuuuffffs at {1}.'.format(executer, user)
        interaction['24'] = '{0} sniffs {1}.'.format(executer, user)
        interaction['25'] = '{0} crawls on all fours to {1}.'.format(executer, user)
        interaction['26'] = '{0} stands wearing a latex maid uniform, offering a glass of wine to {1}.'.format(executer, user)
        interaction['27'] = '{0} waves their feet in the face of {1}.'.format(executer, user)
        interaction['28'] = '{0} gives a candy bar to {1}.'.format(executer, user)
        interaction['29'] = '{0} throws a rock at {1}.'.format(executer, user)
        interaction['30'] = '{0} licks {1}.'.format(executer, user)

        if member.id == self.bot.user.id:
            await self.bot.say('**Error: Could not interact.**')
        else:
            await self.bot.say('**{0}**'.format(random.choice([interaction[i] for i in interaction])))

def setup(bot):
    bot.add_cog(Interactions(bot))
