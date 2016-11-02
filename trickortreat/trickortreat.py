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
        suprise['1'] = 'trick: https://i.ytimg.com/vi/lwgch2vrZxs/maxresdefault.jpg'
        suprise['2'] = 'treat: https://cdn.shopify.com/s/files/1/0972/7116/products/harry-potter-chocolate-frog-unwrapped4_1024x1024.png?v=1459347352'
        suprise['3'] = 'trick: https://s-media-cache-ak0.pinimg.com/236x/d4/75/5a/d4755aa7bb99a73b38592dd1c4d06df7.jpg'
        suprise['4'] = 'treat: https://i.kinja-img.com/gawker-media/image/upload/s--8Xs1eS4c--/c_scale,fl_progressive,q_80,w_800/evwu1nukixart6mcn8vw.jpg'
        suprise['5'] = 'trick: http://scontent.cdninstagram.com/t51.2885-15/e35/12965880_565667836948598_2099180853_n.jpg?ig_cache_key=MTIzNzgxNDM0OTUxMjMyNDk0MA%3D%3D.2'
        suprise['6'] = 'treat: https://heathersweets.files.wordpress.com/2011/10/haribo-horror-mix-inside.jpg'
        suprise['7'] = 'trick: https://s-media-cache-ak0.pinimg.com/236x/04/3a/68/043a68cbf7789a508d802be4809ed0f1.jpg'
        suprise['8'] = 'treat: http://www.bakingdom.com/wp-content/uploads/2010/11/Delicious-Cauldron-Cakes.jpg'
        suprise['9'] = 'trick: http://vignette4.wikia.nocookie.net/bigbangtheory/images/2/22/Vlcsnap-2011-11-20-15h18m17s164.png/revision/latest?cb=20111120111901'
        suprise['10'] = 'treat :http://metanomicon.net/wp-content/uploads/2011/12/hansolo.jpg'
        suprise['11'] = 'trick: http://cdn.mos.cms.futurecdn.net/k5MFr2h8GviPwuBnuKDzSN-970-80.jpg'
        suprise['12'] = 'treat: http://www.ics.uci.edu/~eppstein/pix/t7bd/BottsBeans-m.jpg'
        suprise['13'] = 'trick: https://i.ytimg.com/vi/4U7l9AvVT_E/hqdefault.jpg'
        suprise['14'] = 'treat: http://2.bp.blogspot.com/_rzdB5a4kLAo/THbY9-VGbLI/AAAAAAAAVjY/INzjpgmJIk8/s1600/e59b_stay_puft_marshmallows.jpg'
        suprise['15'] = 'trick: https://v.cdn.vine.co/r/avatars/678A1382AC1394436560929370112_10abb68344d.3.4.jpg?versionId=thOdcbEvqApSRbfgPk8WYGJYg5rwH3ZH'
        suprise['16'] = 'treat: http://sweets.seriouseats.com/images/images/2011/10/20111011-candy-a-day-nerds.jpg'
        suprise['17'] = 'trick: http://static2.hypable.com/wp-content/uploads/2015/05/Dementor-wasp-2.jpg'
        suprise['18'] = 'treat: https://pioneerpartyandgift.com/image/cache/data/product/pioneer_party_eyeball_gumballs-500x500.jpg'
        suprise['19'] = 'trick: http://i.imgur.com/nbcTtZC.gif'
        suprise['20'] = 'treat: http://www.zombiegift.com/zombie-blog/wp-content/uploads/2014/01/zombie-bar-chocolate-bar-sugar-plum-chocolates-zombie-chocolate-bar-review11.jpg'
        suprise['21'] = 'trick: http://media.tumblr.com/tumblr_lkqcixv4UN1qd3url.gif'
        suprise['22'] = 'treat: https://cdn.instructables.com/FM3/X5MC/H88XIJR6/FM3X5MCH88XIJR6.MEDIUM.jpg'
        suprise['23'] = 'trick: http://img00.deviantart.net/12db/i/2006/185/a/4/jack_skellington_by_kev2137.jpg'
        suprise['24'] = 'treat: http://melvillecandy.com/assets/images/spooky_assortment.jpg'
        suprise['25'] = 'trick: https://upload.wikimedia.org/wikipedia/commons/2/2f/Roachies.JPG'
        suprise['26'] = 'treat: https://cdn.discordapp.com/attachments/237897212791619584/242635869884776451/download_31.jpg'
        suprise['27'] = 'trick: http://akphoto4.ask.fm/887/424/258/910003021-1sall78-c0gn67b3hog258a/original/Riddlesolved.jpg'
        suprise['28'] = 'treat: http://www.partycity.com/images/products/en_us/gateways/candy-2015/candy-by-type/candy-by-type-bubblegum.jpg'
        suprise['29'] = 'trick: http://i2.kym-cdn.com/photos/images/original/001/063/320/27c.jpg'
        suprise['30'] = 'treat: http://67.media.tumblr.com/268692a326296b9571409c235cc6ac44/tumblr_inline_nyws9cnoXd1tbiwft_1280.jpg'
        suprise['31'] = 'trick: http://vignette2.wikia.nocookie.net/freddy-fazbears-pizza/images/0/0f/FNAFSL_Ennard_Model.png/revision/latest/'
        suprise['32'] = 'treat: https://s-media-cache-ak0.pinimg.com/736x/84/eb/ce/84ebce7a284c1c40d20b4aa1dd13734c.jpg'

        await self.bot.say('{0} got a {1}'.format(trickortreater, random.choice([suprise[i] for i in suprise])))

def setup(bot):
    bot.add_cog(TrickOrTreat(bot))
