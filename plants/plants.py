from discord.ext import commands
import random
import discord
import asyncio
import datetime

class Plants:
    """Grow your own plants! There are 10 of them!"""
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def grow(self, context, num : int):
        """Grow a plant! Type a seed number from 1 to 10."""
        gardener = context.message.author.mention
        d = datetime.date.today()
        cday = d.month
        cmonth = d.month

        if num == 1:
            await self.bot.say('{0}, you have sown the seed! http://image.prntscr.com/image/8216eab27b63462bbae5fc7cd068b666.png'.format(gardener))
            if (cmonth == 4 and cday == 22):
                await asyncio.sleep(60)
            else:
                await asyncio.sleep(3600)
                await self.bot.say('{0}, you have grown a: **Truffula Tree**! http://image.prntscr.com/image/4f3a95bdc418414a83a9b12c90285df1.png'.format(gardener))
        elif num == 2:
            await self.bot.say('{0}, you have sown the seed! http://image.prntscr.com/image/d6659c57560c48c4aafb34b99c7213ce.png'.format(gardener))
            if (cmonth == 4 and cday == 22):
                await asyncio.sleep(60)
            else:
                await asyncio.sleep(3600)
                await self.bot.say('{0}, you have grown a: **Peashooter**! http://vignette3.wikia.nocookie.net/plantsvszombies/images/c/ca/Peashooter2.png/revision/latest?cb=20130717035301&format=webp'.format(gardener))
        elif num == 3:
            await self.bot.say('{0}, you have sown the seed! http://cdn.bulbagarden.net/upload/thumb/7/7a/Sunkern_anime.png/200px-Sunkern_anime.png'.format(gardener))
            if (cmonth == 4 and cday == 22):
                await asyncio.sleep(60)
            else:
                await asyncio.sleep(3600)
                await self.bot.say('{0}, you have grown a: **Sunflora**! http://cdn.bulbagarden.net/upload/thumb/9/98/192Sunflora.png/250px-192Sunflora.png'.format(gardener))
        elif num == 4:
            await self.bot.say('{0}, you have sown the seed! https://nookipedia.com/w/images/e/ee/Bag_\'o_Bells.jpg'.format(gardener))
            if (cmonth == 4 and cday == 22):
                await asyncio.sleep(60)
            else:
                await asyncio.sleep(3600)
                await self.bot.say('{0}, you have grown a: **Money Tree**! http://vignette2.wikia.nocookie.net/new-leaf/images/1/19/9image.jpg/revision/latest?cb=20130405102017'.format(gardener))
        elif num == 5:
            await self.bot.say('{0}, you have sown the seed! http://image.prntscr.com/image/b3837ff3596942c5ba59da3dfd6f740d.png'.format(gardener))
            if (cmonth == 4 and cday == 22):
                await asyncio.sleep(60)
            else:
                await asyncio.sleep(3600)
                await self.bot.say('{0}, you have grown a: **Pikmin**! http://vignette2.wikia.nocookie.net/pikmin/images/6/6e/PikRedPikWave.jpg/revision/latest?cb=20100105163552'.format(gardener))
        elif num == 6:
            await self.bot.say('{0}, you have sown the seed! https://s-media-cache-ak0.pinimg.com/236x/75/dc/05/75dc057dbd2ead0bd36bc35634c0f100.jpg'.format(gardener))
            if (cmonth == 4 and cday == 22):
                await asyncio.sleep(60)
            else:
                await asyncio.sleep(3600)
                await self.bot.say('{0}, you have grown a: **Groot**! http://www.sideshowtoy.com/wp-content/uploads/2014/07/902220-product-silo.png'.format(gardener))
        elif num == 7:
            await self.bot.say('{0}, you have sown the seed! http://wow.zamimg.com/uploads/screenshots/small/571307.jpg'.format(gardener))
            if (cmonth == 4 and cday == 22):
                await asyncio.sleep(60)
            else:
                await asyncio.sleep(3600)
                await self.bot.say('{0}, you have grown a: **Starlight Rose**! http://media-azeroth.cursecdn.com/attachments/110/579/636091096044323300.png'.format(gardener))
        elif num == 8:
            await self.bot.say('{0}, you have sown the seed! http://vignette2.wikia.nocookie.net/farmville/images/0/01/Magic_Beans-icon.png/revision/latest?cb=20140702134740'.format(gardener))
            if (cmonth == 4 and cday == 22):
                await asyncio.sleep(60)
            else:
                await asyncio.sleep(3600)
                await self.bot.say('{0}, you have grown a: **Magic Beanstalk**! http://zynga2-a.akamaihd.net/farmville/assets/hashed/assets/decorations/44d54df054b03bb97878d5a45dbf9965.png'.format(gardener))
        elif num == 9:
            await self.bot.say('{0}, you have sown the seed! http://image.prntscr.com/image/e2361346585c45af8658fa3e38649ea3.png'.format(gardener))
            if (cmonth == 4 and cday == 22):
                await asyncio.sleep(60)
            else:
                await asyncio.sleep(3600)
                await self.bot.say('{0}, you have grown a: **Radiant Roxy Rose**! http://vignette2.wikia.nocookie.net/moshimonsters/images/7/73/Radiant_Roxy_Rose_grown.png/revision/latest?cb=20161001205046'.format(gardener))
        elif num == 10:
            await self.bot.say('{0}, you have sown the seed! http://vignette2.wikia.nocookie.net/clubpenguin/images/a/a9/Puffle_Care_Icons_Pizzapepperoni.png/revision/latest/scale-to-width-down/100?cb=20131003041210&format=webp'.format(gardener))
            if (cmonth == 4 and cday == 22):
                await asyncio.sleep(60)
            else:
                await asyncio.sleep(3600)
                await self.bot.say('{0}, you have grown a: **Pizza Plant**! http://vignette2.wikia.nocookie.net/clubpenguin/images/1/13/Mine_Shack_pizza_plant.png/revision/latest?cb=20121224163241'.format(gardener))
        else:
            await self.bot.say('Seed not found: Pick a seed number from 1 to 10.')
def setup(bot):
    bot.add_cog(Plants(bot))
