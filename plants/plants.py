from discord.ext import commands
import random
import discord
import asyncio

class Plants:
    """Grow your own plants! There are 15 of them!"""
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(pass_context=True)
    async def grow(self, context):
        """Grow a plant!"""
        gardener = context.message.author.mention

        plant = {}
        plant['1'] = '**Truffula Tree**! http://image.prntscr.com/image/4f3a95bdc418414a83a9b12c90285df1.png'
        plant['2'] = '**Peashooter**! http://vignette3.wikia.nocookie.net/plantsvszombies/images/c/ca/Peashooter2.png/revision/latest?cb=20130717035301&format=webp'
        plant['3'] = '**Sunflora**! http://cdn.bulbagarden.net/upload/thumb/9/98/192Sunflora.png/250px-192Sunflora.png'
        plant['4'] = '**Money Tree**! http://vignette2.wikia.nocookie.net/new-leaf/images/1/19/9image.jpg/revision/latest?cb=20130405102017'
        plant['5'] = '**Pikmin**! http://vignette2.wikia.nocookie.net/pikmin/images/6/6e/PikRedPikWave.jpg/revision/latest?cb=20100105163552'
        plant['6'] = '**Groot**! http://www.sideshowtoy.com/wp-content/uploads/2014/07/902220-product-silo.png'
        plant['7'] = '**Starlight Rose**! http://media-azeroth.cursecdn.com/attachments/110/579/636091096044323300.png'
        plant['8'] = '**Magic Beanstalk**! http://zynga2-a.akamaihd.net/farmville/assets/hashed/assets/decorations/44d54df054b03bb97878d5a45dbf9965.png'
        plant['9'] = '**Radiant Roxy Rose**! http://vignette2.wikia.nocookie.net/moshimonsters/images/7/73/Radiant_Roxy_Rose_grown.png/revision/latest?cb=20161001205046'
        plant['10'] = '**Pizza Plant**! http://vignette2.wikia.nocookie.net/clubpenguin/images/1/13/Mine_Shack_pizza_plant.png/revision/latest?cb=20121224163241'
        plant['11'] = '**Whomping Willdow**! http://hogsmeade.pl/images/photoalbum/album_9/zima.jpg'
        plant['12'] = '**Triffid**! http://triffids.guidesite.co.uk/images/triffids/triffidPoole.jpg'
        plant['13'] = '**Goomba**! http://www.ssbwiki.com/images/5/5d/Goomba-Brawl.png'
        plant['14'] = '**Athelas**! http://vignette2.wikia.nocookie.net/lotr/images/7/7e/Athelas.jpg/revision/latest?cb=20120505172036'
        plant['15'] = '**Pod Plant**! http://vignette2.wikia.nocookie.net/memoryalpha/images/3/31/Omicron_Ceti_III_flower.jpg/revision/latest?cb=20050929090117&path-prefix=en'

        await self.bot.say('{0}, you have sown the seed! http://wow.zamimg.com/uploads/screenshots/small/571307.jpg'.format(gardener))
        await asyncio.sleep(3600)
        await self.bot.say('{0}, you have grown a: {1}'.format(gardener, random.choice([plant[i] for i in plant])))
def setup(bot):
    bot.add_cog(Plants(bot))
