from discord.ext import commands
import random
import discord

class Interactions:
    def __init__(self, bot):
        self.bot = bot

        #SFW version of kill commond by PaddoCogs. Thanks Kowlin, Twentysix, Redjumpman, and Ruby.

    @commands.command(pass_context=True)
    async def kill(self, context, user : discord.Member):
        """Wanna kill someone? Wanna be the troll kind? You've got the perfect cog for the lulz! 25 unique and funny kill commands!"""
        killer = context.message.author.mention
        victim = user.mention
        technique = []
        technique[0] = '{0} shoots  in {1}\'s mouth with rainbow laser, causing {1}\'s head to explode with rainbows and {1} is reborn as unicorn. :unicorn:'.format(killer, victim)
        technique[1] = '{0} ate a piece of exotic butter. It was so amazing that it killed them.'.format(victim)
        technique[2] = '{0} is stuffed into a suit by Freddy on their night guard duty. Oh, not those animatronics again!'.format(victim)
        technique[3] = '{0} grabs {1} and shoves them into an auto-freeze machine with some juice and sets the temperature to 100 Kelvin, creating human ice pops.'.format(killer, victim)
        technique[4] = '{0} drowns {1} in a tub of hot chocolate. *"How was your last drink?"*'.format(killer, victim)
        technique[5] = '{0} screams in terror as they accidentally spawn in the cthulhu while uttering random latin words. Cthulhu grabs {0} by the right leg and takes them to his dimension yelling,"Honey, Dinner\'s ready!"'.format(victim)
        technique[6] = '{0} feeds toothpaste-filled oreos to {1}, who were apparently allergic to fluorine. GGWP.'.format(killer, victim)
        technique[7] = '{0} forgot to zombie-proof {1}\'s lawn... Looks like zombies had a feast last night.'.format(killer, victim)
        technique[8] = '{0} cranks up the music system only to realize the volume was at max and the song playing was Baby by Justin Beiber...'.format(victim)
        technique[9] = '{0} presses a random button and is teleported to the height of 100m, allowing them to fall to their inevitable death. Moral of the story: Don\'t go around pressing random buttons.'.format(victim)
        technique[10] = '{0} is injected with chocolate syrup, which mutates them into a person made out of chocolate. While doing a part-time job at the Daycare, they are devoured by the hungry babies. :chocolate_bar:'.format(victim)
        technique[11] = '{0} is sucked into Minecraft. {0}, being a noob at the so called "Real-Life Minecraft" faces the Game Over screen.'.format(victim)
        technique[12] = '{0} turns on Goosebumps(2015 film) on the TV. {1} being a scaredy-cat, dies of an heart attack.'.format(killer, victim)
        technique[13] = '{0} after a long day, plops down on the couch with {1} and turns on The Big Bang Theory. After a Sheldon Cooper joke, {1} laughs uncontrollably as they die.'.format(killer, victim)
        technique[14] = '{0} was given a chance to synthesize element 119 (Ununennium) and have it named after them, but they messed up. R.I.P.'.format(victim)
        technique[15] = '{0} gets {1} to watch anime with them. {1} couldn\'t handle it.'.format(killer, victim)
        technique[16] = '{0} tried to get crafty, but they accidentally cut themselves with the scissors.:scissors:'.format(victim)
        technique[17] = '{0} goes genocide and Sans totally dunks {0}!'.format(victim)
        technique[18] = '{0} was so swag that {1} died due to it. #Swag'.format(killer, victim)
        technique[19] = '{0} has been found guilty, time for their execution!'.format(victim)
        technique[20] = '{0} fell down a cliff while playing Pokemon Go. Good job on keeping your nose in that puny phone. :iphone:'.format(victim)
        technique[21] = '{0} strikes {1} with the killing curse... *"Avada Kedavra!"*'.format(killer, victim)
        technique[22] = '{0} ate an apple and turned out it was made out of wax. Someone died from wax poisoning later that day.'.format(victim)
        technique[23] = '{0} was teleported to the timeline where Jurassic World was real and they were eaten alive by the Indominus Rex.'.format(victim)
        technique[24] = '{0} was charging their Samsung Galaxy Note 7...'.format(victim)
        technique[25] = '{0} shot {1} using the Starkiller Base!'.format(killer, victim)
        technique[26] = '{0} was a resident of Alderaan before Darth Vader destroyed the planet...'.format(victim)
        technique[27] = '{0} was scooped by {1} and their innards are now Ennard.'.format(victim, killer)
        technique[28] = '{0} Alt+F4\'d {1}.exe!'.format(killer, victim)
        technique[29] = '{0} was accused of stealing Neptune\'s crown...'.format(victim)

        if user.id == self.bot.user.id:
            await self.bot.say('**{0}, how dare you try to kill me? DIE!**'.format(killer))
        else:
            await self.bot.say('**{0}**'.format(random.choice(technique)))
    @commands.command(pass_context=True)
    async def interact(self, context, user : discord.Member):
        """Interact with the user you mention."""
        executer = context.message.author.mention
        victim = user.mention
        
        interaction = []
        interaction[0] = '{0} winks at {1}.'.format(executer, victim)
        interaction[1] = '{0} hugs {1}.'.format(executer, victim)
        interaction[2] = '{0} shakes hands with {1}.'.format(executer, victim)
        interaction[3] = '{0} bows down to {1}.'.format(executer, victim)
        interaction[4] = '{0} pokes {1}.'.format(executer, victim)
        interaction[5] = '{0} tickles {1}.'.format(executer, victim)
        interaction[6] = '{0} slaps {1}.'.format(executer, victim)
        interaction[7] = '{0} scratches {1}.'.format(executer, victim)
        interaction[8] = '{0} bites {1}.'.format(executer, victim)
        interaction[9] = '{0} sells {1} for a dime.'.format(executer, victim)
        interaction[10] = '{0} canes {1}.'.format(executer, victim)
        interaction[11] = '{0} whips {1}.'.format(executer, victim)
        interaction[12] = '{0} restrains {1}'.format(executer, victim)
        interaction[13] = '{0} kneels down to {1}.'.format(executer, victim)
        interaction[14] = '{0} gets the box of toys out from {1}.'.format(executer, victim)
        interaction[15] = '{0} ties up {1}.'.format(executer, victim)
        interaction[16] = '{0} ties up and tickles {1}.'.format(executer, victim)
        interaction[17] = '{0} kisses {1}.'.format(executer, victim)
        interaction[18] = '{0} meows at {1}.'.format(executer, victim)
        interaction[19] = '{0} maow meeeeeeoooooows at {1}.'.format(executer, victim)
        interaction[20] = '{0} purrs at {1}.'.format(executer, victim)
        interaction[21] = '{0} wuffs at {1}.'.format(executer, victim)
        interaction[22] = '{0} wwwwuuuuuuuuuffff wwwwuuuuffffs at {1}.'.format(executer, victim)
        interaction[23] = '{0} sniffs {1}.'.format(executer, victim)
        interaction[24] = '{0} crawls on all fours to {1}.'.format(executer, victim)
        interaction[25] = '{0} stands wearing a latex maid uniform, offering a glass of wine to {1}.'.format(executer, victim)
        interaction[26] = '{0} waves their feet in the face of {1}.'.format(executer, victim)
        interaction[27] = '{0} gives a candy bar to {1}.'.format(executer, victim)
        interaction[28] = '{0} throws a rock at {1}.'.format(executer, victim)
        interaction[29] = '{0} licks {1}.'.format(executer, victim)
        
        if user.id == self.bot.user.id:
            await self.bot.say('**Error: Could not interact. Get cleverbot.py from 26-cogs to interact with bot!**')
        else:
            await self.bot.say('**{0}**'.format(random.choice(interaction)))
    @commands.command(pass_context=True)
    async def poke(self, context, user : discord.Member):
        """Poke peeps! :3"""
        pokedoer = context.message.author.mention
        victim = user.mention

        poke = []
        poke[0] = '{0} pokes {1}\'s eye.'.format(pokedoer, victim)
        poke[1] = '{0} boops {1}\'s snoot.'.format(pokedoer, victim)
        poke[2] = '{0} pokes {1} with a stick.'.format(pokedoer, victim)
        poke[3] = '{0} pokes {1} with a pin.'.format(pokedoer, victim)
        poke[4] = '{0} pokes {1} on facebook.'.format(pokedoer, victim)

        if user.id == self.bot.user.id:
            await self.bot.say('**Awww, Don\'t poke me! It makes me laugh!**')
        else:
            await self.bot.say('**{0}**'.format(random.choice(poke)))
    @commands.command(pass_context=True)
    async def throw(self, context, user : discord.Member, *, item : str):

        """Throw stuff at people!"""
        thrower = context.message.author.mention
        victim = user.mention
        b0t = self.bot.user.mention

        if user.id == self.bot.user.id:
            await self.bot.say('**You\'re throwing stuff at me! {0} threw {1} at {2}!**'.format(b0t, item, thrower))
        else:
            await self.bot.say('**{0} threw {1} at {2}!**'.format(thrower, item, victim))
def setup(bot):
    bot.add_cog(Interactions(bot))
