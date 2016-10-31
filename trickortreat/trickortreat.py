from discord.ext import commands
import random
import discord

class TrickOrTreat:
    """Go trick or treating on Discord and get either a trick or a treat!"""
    
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def trickortreat(self, context):
        """Go trick or treating on Discord and get either a trick or a treat! Don't let the tricks spoop you!"""
        trickortreater = context.message.author.mention
        suprise = {} #Remember, I do not any of the following images.
        suprise['1'] = 'https://i.ytimg.com/vi/lwgch2vrZxs/maxresdefault.jpg'
        suprise['2'] = 'https://cdn.shopify.com/s/files/1/0972/7116/products/harry-potter-chocolate-frog-unwrapped4_1024x1024.png?v=1459347352'
        suprise['3'] = 'https://s-media-cache-ak0.pinimg.com/236x/d4/75/5a/d4755aa7bb99a73b38592dd1c4d06df7.jpg'
        suprise['4'] = 'https://i.kinja-img.com/gawker-media/image/upload/s--8Xs1eS4c--/c_scale,fl_progressive,q_80,w_800/evwu1nukixart6mcn8vw.jpg'
        suprise['5'] = 'http://scontent.cdninstagram.com/t51.2885-15/e35/12965880_565667836948598_2099180853_n.jpg?ig_cache_key=MTIzNzgxNDM0OTUxMjMyNDk0MA%3D%3D.2'
        suprise['6'] = 'https://heathersweets.files.wordpress.com/2011/10/haribo-horror-mix-inside.jpg'
        suprise['7'] = 'https://s-media-cache-ak0.pinimg.com/236x/04/3a/68/043a68cbf7789a508d802be4809ed0f1.jpg'
        suprise['8'] = 'http://www.bakingdom.com/wp-content/uploads/2010/11/Delicious-Cauldron-Cakes.jpg'
        suprise['9'] = 'http://vignette4.wikia.nocookie.net/bigbangtheory/images/2/22/Vlcsnap-2011-11-20-15h18m17s164.png/revision/latest?cb=20111120111901'
        suprise['10'] = 'http://metanomicon.net/wp-content/uploads/2011/12/hansolo.jpg'
        suprise['11'] = 'http://cdn.mos.cms.futurecdn.net/k5MFr2h8GviPwuBnuKDzSN-970-80.jpg'
        suprise['12'] = 'http://www.ics.uci.edu/~eppstein/pix/t7bd/BottsBeans-m.jpg'
        suprise['13'] = 'https://i.ytimg.com/vi/4U7l9AvVT_E/hqdefault.jpg'
        suprise['14'] = 'http://2.bp.blogspot.com/_rzdB5a4kLAo/THbY9-VGbLI/AAAAAAAAVjY/INzjpgmJIk8/s1600/e59b_stay_puft_marshmallows.jpg'
        suprise['15'] = 'https://v.cdn.vine.co/r/avatars/678A1382AC1394436560929370112_10abb68344d.3.4.jpg?versionId=thOdcbEvqApSRbfgPk8WYGJYg5rwH3ZH'
        suprise['16'] = 'http://sweets.seriouseats.com/images/images/2011/10/20111011-candy-a-day-nerds.jpg'
        suprise['17'] = 'http://static2.hypable.com/wp-content/uploads/2015/05/Dementor-wasp-2.jpg'
        suprise['18'] = 'https://pioneerpartyandgift.com/image/cache/data/product/pioneer_party_eyeball_gumballs-500x500.jpg'
        suprise['19'] = 'http://i.imgur.com/nbcTtZC.gif'
        suprise['20'] = 'http://www.zombiegift.com/zombie-blog/wp-content/uploads/2014/01/zombie-bar-chocolate-bar-sugar-plum-chocolates-zombie-chocolate-bar-review11.jpg'
        suprise['21'] = 'http://media.tumblr.com/tumblr_lkqcixv4UN1qd3url.gif'
        suprise['22'] = 'https://cdn.instructables.com/FM3/X5MC/H88XIJR6/FM3X5MCH88XIJR6.MEDIUM.jpg'
        suprise['23'] = 'http://img00.deviantart.net/12db/i/2006/185/a/4/jack_skellington_by_kev2137.jpg'
        suprise['24'] = 'http://melvillecandy.com/assets/images/spooky_assortment.jpg'

        await self.bot.say('**{0} got: **{1}'.format(trickortreater, random.choice([suprise[i] for i in suprise])))

def setup(bot):
    bot.add_cog(TrickOrTreat(bot))
