from discord.ext import commands
import random
import discord

class Interactions:
    def __init__(self, bot):
        self.bot = bot

        #SFW version of kill command by PaddoCogs. Thanks Kowlin, Twentysix, Redjumpman, and Ruby.

    @commands.command(pass_context=True)
    async def kill(self, context, user : discord.Member):
        """Wanna kill someone? Wanna be the troll kind? You've got the perfect cog for the lulz! 30 unique and funny kill messages!"""
        killer = context.message.author.display_name
        victim = user.display_name
        technique = [
            '{1} shoots  in {0}\'s mouth with rainbow laser, causing {0}\'s head to explode with rainbows and {0} is reborn as unicorn. :unicorn:',
            '{0} ate a piece of exotic butter. It was so amazing that it killed them.',
            '{0} is stuffed into a suit by Freddy on their night guard duty. Oh, not those animatronics again!',
            '{1} grabs {0} and shoves them into an auto-freeze machine with some juice and sets the temperature to 100 Kelvin, creating human ice pops.',
            '{1} drowns {0} in a tub of hot chocolate. *"How was your last drink?"*',
            '{0} screams in terror as they accidentally spawn in the cthulhu while uttering random latin words. Cthulhu grabs {0} by the right leg and takes them to his dimension yelling, "Honey, Dinner\'s ready!"',
            '{1} feeds toothpaste-filled oreos to {0}, who were apparently allergic to fluorine. GGWP.',
            '{1} forgot to zombie-proof {0}\'s lawn... Looks like zombies had a feast last night.',
            '{0} cranks up the music system only to realize the volume was at max and the song playing was Baby by Justin Beiber...',
            '{0} presses a random button and is teleported to the height of 100m, allowing them to fall to their inevitable death. Moral of the story: Don\'t go around pressing random buttons.',
            '{0} is injected with chocolate syrup, which mutates them into a person made out of chocolate. While doing a part-time job at the Daycare, they are devoured by the hungry babies. :chocolate_bar:',
            '{0} is sucked into Minecraft. {0}, being a noob at the so called "Real-Life Minecraft" faces the Game Over screen.',
            '{1} turns on Goosebumps(2015 film) on the TV. {0} being a scaredy-cat, dies of an heart attack.',
            '{1} after a long day, plops down on the couch with {0} and turns on The Big Bang Theory. After a Sheldon Cooper joke, {0} laughs uncontrollably as they die.',
            '{0} was given a chance to synthesize element 119 (Ununennium) and have it named after them, but they messed up. R.I.P.',
            '{1} gets {0} to watch anime with them. {0} couldn\'t handle it.',
            '{0} tried to get crafty, but they accidentally cut themselves with the scissors.:scissors:',
            '{0} goes genocide and Sans totally dunks {0}!',
            '{1} was so swag that {0} died due to it. #Swag',
            '{0} has been found guilty, time for their execution!',
            '{0} fell down a cliff while playing Pokemon Go. Good job on keeping your nose in that puny phone. :iphone:',
            '{1} strikes {0} with the killing curse... *"Avada Kedavra!"*',
            '{0} ate an apple and turned out it was made out of wax. Someone died from wax poisoning later that day.',
            '{0} was teleported to the timeline where Jurassic World was real and they were eaten alive by the Indominus Rex.',
            '{0} was charging their Samsung Galaxy Note 7...',
            '{1} shot {0} using the Starkiller Base!',
            '{0} was a resident of Alderaan before Darth Vader destroyed the planet...',
            '{0} was scooped by {1} and their innards are now Ennard.',
            '{1} Alt+F4\'d {0}.exe!',
            '{0} was accused of stealing Neptune\'s crown...'
                ]

        if user.id == self.bot.user.id:
            await self.bot.say('**{0}, how dare you try to kill me? DIE!**'.format(killer))
        else:
            await self.bot.say('**{0}**'.format(random.choice(technique).format(victim, killer)))
    @commands.command(pass_context=True)
    async def interact(self, context, user : discord.Member):
        """Interact with the user you mention."""
        executer = context.message.author.display_name
        victim = user.display_name

        interaction = [
            '{0} winks at {1}.',
            '{0} hugs {1}.',
            '{0} shakes hands with {1}.',
            '{0} bows down to {1}.',
            '{0} pokes {1}.',
            '{0} tickles {1}.',
            '{0} slaps {1}.',
            '{0} scratches {1}.',
            '{0} bites {1}.',
            '{0} sells {1} for a dime.',
            '{0} canes {1}.',
            '{0} whips {1}.',
            '{0} restrains {1}',
            '{0} kneels down to {1}.',
            '{0} gets the box of toys out from {1}.',
            '{0} ties up {1}.',
            '{0} ties up and tickles {1}.',
            '{0} kisses {1}.',
            '{0} meows at {1}.',
            '{0} maow meeeeeeoooooows at {1}.',
            '{0} purrs at {1}.',
            '{0} wuffs at {1}.',
            '{0} wwwwuuuuuuuuuffff wwwwuuuuffffs at {1}.',
            '{0} sniffs {1}.',
            '{0} crawls on all fours to {1}.',
            '{0} stands wearing a latex maid uniform, offering a glass of wine to {1}.',
            '{0} waves their feet in the face of {1}.',
            '{0} gives a candy bar to {1}.',
            '{0} throws a rock at {1}.',
            '{0} licks {1}.'
                ]

        if user.id == self.bot.user.id:
            await self.bot.say('**Error: Could not interact. Get cleverbot.py from 26-cogs to interact with bot!**')
        else:
            await self.bot.say('**{0}**'.format(random.choice(interaction).format(executer, victim)))
    @commands.command(pass_context=True)
    async def poke(self, context, user : discord.Member):
        """Poke peeps! :3"""
        pokedoer = context.message.author.display_name
        victim = user.display_name

        poke = [
            '{0} pokes {1}\'s eye.',
            '{0} boops {1}\'s snoot.',
            '{0} pokes {1} with a stick.',
            '{0} pokes {1} with a pin.',
            '{0} pokes {1} on facebook.'
                ]

        if user.id == self.bot.user.id:
            await self.bot.say('**Awww, Don\'t poke me! It makes me laugh!**')
        else:
            await self.bot.say('**{0}**'.format(random.choice(poke).format(pokedoer, victim)))
    @commands.command(pass_context=True)
    async def throw(self, context, user : discord.Member, *, item : str):

        """Throw stuff at people!"""
        thrower = context.message.author.display_name
        victim = user.display_name
        b0t = self.bot.user.display_name

        if user.id == self.bot.user.id:
            await self.bot.say('**You\'re throwing stuff at me! {0} threw {1} at {2}!**'.format(b0t, item, thrower))
        else:
            await self.bot.say('**{0} threw {1} at {2}!**'.format(thrower, item, victim))
def setup(bot):
    bot.add_cog(Interactions(bot))
