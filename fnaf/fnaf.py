import discord
from discord.ext import commands
import random

class FNAF:
    """Use FNAF commands! Commands ranging from bonbon to animstrucure!"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def animstructure(self, num : int): #Images are not owned by me.
        """Look through animatronic structures. IDs: ``1 = Freddy, 2 = Bonnie, 3 = Chica, 4 = Foxy, 5 = Balloon Boy, 6 = Puppet, 7 = Baby, 8 = Ballora``"""
        
        if num == 1:
            await self.bot.say('http://orig08.deviantart.net/ec50/f/2016/220/2/2/freddy_fazbear_by_cakebombs-dad2y7p.png')
        elif num == 2:
            await self.bot.say('http://img02.deviantart.net/b719/i/2015/229/c/4/bonnie_the_bunny_full_body_by_doctoroctoroc-d964ezc.jpg')
        elif num == 3:
            await self.bot.say('http://orig00.deviantart.net/c25b/f/2016/009/8/9/chica_full_body_by_dafredgle87-d9ncz97.png')
        elif num == 4:
            await self.bot.say('http://orig03.deviantart.net/5809/f/2015/240/f/4/withered_foxy_full_body_by_joltgametravel-d97ilot.png')
        elif num == 5:
            await self.bot.say('http://vignette1.wikia.nocookie.net/freddy-fazbears-pizza/images/b/b6/FNAF2BB.png/revision/latest?cb=20141111111744')
        elif num == 6:
            await self.bot.say('http://vignette1.wikia.nocookie.net/freddy-fazbears-pizza/images/b/b6/FNAF2BB.png/revision/latest?cb=20141111111744')
        elif num == 7:
            await self.bot.say('http://orig15.deviantart.net/0aaa/f/2016/282/b/f/baby_png_by_x_puzzy-dakewzu.png')
        elif num == 8:
            await self.bot.say('http://orig11.deviantart.net/d578/f/2016/281/8/4/ballora_full_body_edit_by_joltgametravel-da6q949.png')
        else:
            await self.bot.say('Invalid Animatronic.')
    @commands.command(pass_context=True)
    async def scoop(self, context,  user : discord.Member):
        """Scoop your enemies. ;)"""

        if user.id == self.bot.user.id:
            await self.bot.say("**ERROR:** Scooping Target not found. **RETRY:** Target located. Successfully scooped {0}.".format(context.message.author.mention))
        else:
            await self.bot.say("Successfully scooped {0}.".format(user.mention))
    @commands.command()
    async def bonbon(self):
        """Awaken Bonbon!"""

        await self.bot.say("**Funtime Freddy:** *Bawn-Bawn, It's showtime!*")
    @commands.command()
    async def cupcake(self, user : discord.Member):
        """Order a Cupcake at Chica's Bakery!"""

        await self.bot.say("**Chica:** *Cupcake served to {0}.*".format(user.mention))
    @commands.command()
    async def foxyshow(self):
        """Watch Foxy's Show?"""

        await self.bot.say("**ERROR:** Animatronic out of order.")
    @commands.command()
    async def springlog(self):
        """View the springlock log!"""

        await self.bot.say("```===========SPRINGLOCK SUIT LOG===========\n #1 SPR-BONNIE-1         IN STORAGE\n #2 SPR-BONNIE-2         MISSING (NOTE: Last seen in 1987)\n #3 SPR-FREDDY-1         IN STORAGE\n #4 SPR-FREDDY-2         MISSING\n =========================================```")
    @commands.command()
    async def fnafquote(self):
        """Get FNAF quotes..."""

        quote = {}
        quote['1'] = '**HandUnit:** We have gift baskets containing fruit, nuts, flowers, and of course the ever-popular cash basket. Using the keypad below, please enter the first few letters of the gift basket you would like. It seems that you had some trouble with the keypad. I see what you were trying to type and I will autocorrect it for you. Thank you for selecting "Exotic Butters."'
        quote['2'] = '**HandUnit:** Please enter your name as seen above the keypad. This cannot be changed later, so please be careful. It seems that you had some trouble with the keypad. I see what you were trying to type and I will autocorrect it for you. Welcome, Eggs Benedict.'
        quote['3'] = '**HandUnit:** Using the keypad below, please select a new companion voice... It seems that you had some trouble with the keypad. I see what you were trying to type and I will autocorrect it for you. Thank you for choosing "Angsty Teen."'
        quote['4'] = '**HandUnit:** Using the keypad below please type the first few letters of the musical selection you would prefer. It seems that you had some trouble with the keypad. I see what you were trying to type and I will autocorrect it for you. Thank you for selecting "Casual Bongos."'
        quote['5'] = '**Circus Baby:** You don\'t know what we\'ve been through...'
        quote['6'] = '**Circus Baby:** Don\'t hold it against us...'
        quote['7'] = '**Circus Baby:** Isn\'t "the scooper" a fun name? It sounds like something you would use for ice cream, or custard, or sprinkles. It sounds like something you would want at your birthday party, to ensure you get a heaping portion of every. Good. Thing.'
        quote['8'] = '**Circus Baby:** I  wonder, though, if you were a freshly opened pint of ice cream, how you would feel about something with that name. Thankfully, I don\'t think a freshly opened pint of ice cream feels amything at all.'
        quote['9'] = '**Circus Baby:** Did you know that I was on stage once? It wasn\'t for very long, only one day. What a wonderful day, though. I was in a small room with balloons and a few tables. No-one sat at the tables, though, but children would run in and out. Some were afraid of me, others enjoyed my songs. Music was always coming from somewhere else, down a hall. I would always count the children; I\'m not sure why. I was always acutely aware of how many there were in the room with me. Two, then three, then two, then three, then four, then two, then none. They usually played together in groups of two or three. I was covered in glitter. I smelled like birthday cake. There were two, then three, then five, then four. I can do something special, did you know that? I can make ice cream, although I only did it once. There were four, then three, then two, then one. Something happened when there was one. A little girl, standing by herself. I was no longer myself. And I stopped singing. My stomach opened and there was ice cream. I couldn\'t move, at least not until she stepped closer. There was screaming for a moment, but only for a moment. Then other children rushed in again, but they couldn\'t hear her over the sounds of their own excitement. I still hear her sometimes. Why did that happen?'
        quote['10'] = '**Ennard:** There\'s a bit of me in everybody...'
        quote['11'] = '**Phone Guy:** So, just be aware, the characters do tend to wander a bit. Uh, they\'re left in some kind of free roaming mode at night. Uh... Something about their servos locking up if they get turned off for too long. Uh, they used to be allowed to walk around during the day too. But then there was The Bite of \'87. Yeah. I-It\'s amazing that the human body can live without the frontal lobe, you know?'
        quote['12'] = '**Phone Guy:** Uh, the animatronic characters here do get a bit quirky at night, but do I blame them? No. If I were forced to sing those same stupid songs for twenty years and I never got a bath? I\'d probably be a bit irritable at night, too. So remember, these characters hold a special place in the hearts of children, and we need to show them a little respect, right?'
        quote['13'] = '**Phone Guy:** Hello, hello? Hey you\'re doing great! Most people do not last this long. I mean, you know, they usually move on to other things by now. I\'m not implying that they died. Th-th-that\'s not what I meant.'
        quote['14'] = '**Phone Guy:** Hello, hello ... hello? Uh, well, if you\'re hearing this, then chances are you\'ve made ​​a very poor career choice.'
        quote['15'] = '**Phone Guy:** Uh, hello? Hello, hello! Uh, there\'s been a slight change of company policy concerning use of the suits. Um, don\'t.'
        quote['16'] = '**...:** He will come back. He always does. We have a place for him..'
        quote['17'] = '**...:** What is it that you think you see? What game do you think you are playing? What have you brought home?'
        quote['18'] = '**Ballora:** Get back on your stage. NOW.'
        await self.bot.say('*{0}*'.format(random.choice([quote[i] for i in quote])))
def setup(bot):
    bot.add_cog(FNAF(bot))
