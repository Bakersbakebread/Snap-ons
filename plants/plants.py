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

        plant = {} #No plants were harmed in making of this cog. (Well, if you kill them while using this cog...)
        plant['1'] = 'a: **Dandelion** [COMMON] http://i.imgur.com/emqnQP2.jpg'
        plant['2'] = 'a: **Poppy** [COMMON] http://i.imgur.com/S4hjyUX.jpg'
        plant['3'] = 'a: **Daisy** [COMMON] http://i.imgur.com/lcFq4AB.jpg'
        plant['4'] = 'a: **Daffodil** [COMMON] http://i.imgur.com/pnCCRsH.jpg'
        plant['5'] = 'a: **Chrysanthemum** [COMMON] http://i.imgur.com/5jLtqWL.jpg'
        plant['6'] = 'an: **Aster** [COMMON] http://i.imgur.com/1tN04Hl.jpg'
        plant['7'] = 'a: **Pansy** [COMMON] http://i.imgur.com/f7TgD1b.jpg'
        plant['8'] = 'a: **Lavender** [COMMON] http://i.imgur.com/g3OmOSK.jpg'
        plant['9'] = 'a: **Lily** [COMMON] http://imgur.com/a/HTEgm'
        plant['10'] = 'a: **Petunia** [COMMON] http://i.imgur.com/rJm8ISv.jpg'
        plant['11'] = 'an: **Aloe Vera** [COMMON] http://i.imgur.com/WFAYIpx.jpg'
        plant['12'] = 'a: **Tulip** [COMMON] http://i.imgur.com/kodIFjE.jpg'
        plant['13'] = 'a: **Rose** [COMMON] http://i.imgur.com/sdTNiOH.jpg'
        plant['14'] = 'a: **Sunflower** [COMMON] http://i.imgur.com/AzgzQK9.jpg'
        plant['15'] = 'an: **Orchid** [COMMON] http://i.imgur.com/IQrQYDC.jpg'
        plant['16'] = 'a: **Four-Leaved Clover*** [COMMON] http://i.imgur.com/0GSsABG.jpg'
        plant['17'] = 'a: **Dragon Fruit** [UNCOMMON] http://i.imgur.com/pfngpDS.jpg'
        plant['18'] = 'a: **Mango** [UNCOMMON] http://i.imgur.com/ybR78Oc.jpg'
        plant['19'] = 'a: **Lychee** [UNCOMMON] http://i.imgur.com/w9LkfhX.jpg'
        plant['20'] = 'a: **Durian** [UNCOMMON] http://i.imgur.com/jh249fz.jpg'
        plant['21'] = 'a: **Fig** [UNCOMMON] http://i.imgur.com/YkhnpEV.jpg'
        plant['22'] = 'a: **Jack Fruit** [UNCOMMON] http://i.imgur.com/2D79TlA.jpg'
        plant['23'] = 'a: **Prickly Pear** [UNCOMMON] http://i.imgur.com/GrcGAGj.jpg'
        plant['24'] = 'a: **Pineapple** [UNCOMMON] http://i.imgur.com/VopYQtr.jpg'
        plant['25'] = 'a: **Citron** [UNCOMMON] http://i.imgur.com/zh7Dr23.jpg'
        plant['26'] = 'a: **Cherimoya** [UNCOMMON] http://i.imgur.com/H62gQK6.jpg'
        plant['27'] = 'a: **Mangosteen** [UNCOMMON] http://i.imgur.com/McNnMqa.jpg'
        plant['28'] = 'a: **Apple** [UNCOMMON] http://i.imgur.com/QI3UTR3.jpg'
        plant['29'] = 'a: **Bamboo** [UNCOMMON] http://i.imgur.com/gIQrMcN.jpg'
        plant['30'] = 'a: **Orange** [UNCOMMON] http://i.imgur.com/lwjEJTm.jpg'
        plant['31'] = 'a: **Guava** [UNCOMMON] http://i.imgur.com/iy8WgPt.jpg'
        plant['32'] = 'a: **Franklin Tree** [RARE] http://i.imgur.com/hoh17hp.jpg'
        plant['33'] = 'a: **Jade Vine** [RARE] http://i.imgur.com/h4fJo2R.jpg'
        plant['34'] = 'a: **Koki\'o** [RARE] http://i.imgur.com/Dhw9ync.jpg'
        plant['25'] = 'a: **Parrot\'s Beak** [RARE] http://i.imgur.com/lhSjfQY.jpg'
        plant['26'] = 'a: **Chocolate Cosmos** [RARE] http://i.imgur.com/4ArSekX.jpg'
        plant['27'] = 'a: **Venus Fly Trap** [RARE] http://i.imgur.com/NoSdxXh.jpg'
        plant['28'] = 'a: **Pizza Plant** [SUPER RARE] http://i.imgur.com/ASZXr7C.png'
        plant['29'] = 'a: **Radiant Roxy Rose** [SUPER RARE] http://i.imgur.com/aLe56mr.png'
        plant['30'] = 'a: **Pod Plant** [SUPER RARE] http://i.imgur.com/ECAGMUM.jpg'
        plant['31'] = 'a: **Pirahna Plant** [SUPER RARE] http://i.imgur.com/c03i9W7.jpg'
        plant['32'] = 'a: **Peashooter** [SUPER RARE] http://imgur.com/a/IJBu2'
        plant['33'] = 'a: **Starlight Rose** [EPIC] http://i.imgur.com/em8Kg5M.png'
        plant['34'] = 'a: **Groot** [EPIC] http://i.imgur.com/9f5QzaW.jpg'
        plant['35'] = 'a: **Triffid** [EPIC] http://i.imgur.com/WZlwqUt.jpg'
        plant['36'] = 'an: **Athelas** [EPIC] http://i.imgur.com/PNNMEjB.jpg'
        plant['37'] = 'a: **Pikmin** [EPIC] http://i.imgur.com/cFSmaHH.png'
        plant['38'] = 'a: **Money Tree** [LEGENDARY] http://i.imgur.com/MIJQDLL.jpg'
        plant['39'] = 'a: **Whomping Willow** [LEGENDARY] http://i.imgur.com/Ibwm2xY.jpg'
        plant['40'] = 'a: **Truffula Tree* [LEGENDARY] http://i.imgur.com/cFSmaHH.png'

        await self.bot.say('{0}, you have sown the seed! http://i.imgur.com/4uIktZQ.jpg'.format(gardener))
        t1 = random.randint(1800, 3600)
        await asyncio.sleep(t1)
        await self.bot.say('{0}, your plant need water! Do you want to water it? (yes/no)'.format(gardener))
        answer = await self.bot.wait_for_message(timeout=300,
                                                 author=context.message.author)

        if answer is None:
            await self.bot.say('{0}, your plant has died...'.format(gardener))
        elif answer.content.lower().strip() == "yes":
            await self.bot.say('You have successfully watered the plant.')
            t2 = random.randint(1800, 3600)
            await asyncio.sleep(t2)
            await self.bot.say('{0}, the soil needs fertilizer! Do you want to fertilize it? (yes/no)'.format(gardener))
            answer = await self.bot.wait_for_message(timeout=300,
                                                     author=context.message.author)

            if answer is None:
                await self.bot.say('{0}, your plant has died...'.format(gardener))
            elif answer.content.lower().strip() == "yes":
                await self.bot.say('You have successfully fertilized the soil.')
                t3 = random.randint(1800, 3600)
                await asyncio.sleep(t3)
                await self.bot.say('{0}, you have grown {1}'.format(gardener, random.choice([plant[i] for i in plant])))
            else:
                await self.bot.say('{0}, your plant has died...'.format(gardener))
        else:
            await self.bot.say('{0}, your plant has died...'.format(gardener))
def setup(bot):
    bot.add_cog(Plants(bot))
