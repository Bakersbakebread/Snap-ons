from discord.ext import commands
import random
import datetime


class Seasonal:
    """Go trick or treating or count days until Christmas!"""  # Remember: I don't own any of the following images and videos!

    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def trickortreat(self, context):
        """Go trick or treating on Discord and get either a trick or a treat! Don't let the tricks spoop you!"""
        trickortreater = context.message.author.mention

        d = datetime.date.today()
        cday = d.day
        cmonth = d.month
        surprise = [
            'trick: https://i.ytimg.com/vi/lwgch2vrZxs/maxresdefault.jpg',
            'treat: https://cdn.shopify.com/s/files/1/0972/7116/products/harry-potter-chocolate-frog-unwrapped4_1024x1024.png?v=1459347352',
            'trick: https://s-media-cache-ak0.pinimg.com/236x/d4/75/5a/d4755aa7bb99a73b38592dd1c4d06df7.jpg',
            'treat: https://i.kinja-img.com/gawker-media/image/upload/s--8Xs1eS4c--/c_scale,fl_progressive,q_80,w_800/evwu1nukixart6mcn8vw.jpg',
            'trick: http://scontent.cdninstagram.com/t51.2885-15/e35/12965880_565667836948598_2099180853_n.jpg?ig_cache_key=MTIzNzgxNDM0OTUxMjMyNDk0MA%3D%3D.2',
            'treat: https://heathersweets.files.wordpress.com/2011/10/haribo-horror-mix-inside.jpg',
            'trick: https://s-media-cache-ak0.pinimg.com/236x/04/3a/68/043a68cbf7789a508d802be4809ed0f1.jpg',
            'treat: http://www.bakingdom.com/wp-content/uploads/2010/11/Delicious-Cauldron-Cakes.jpg',
            'trick: http://vignette4.wikia.nocookie.net/bigbangtheory/images/2/22/Vlcsnap-2011-11-20-15h18m17s164.png/revision/latest?cb=20111120111901',
            'treat :http://metanomicon.net/wp-content/uploads/2011/12/hansolo.jpg',
            'trick: http://cdn.mos.cms.futurecdn.net/k5MFr2h8GviPwuBnuKDzSN-970-80.jpg',
            'treat: http://www.ics.uci.edu/~eppstein/pix/t7bd/BottsBeans-m.jpg',
            'trick: https://i.ytimg.com/vi/4U7l9AvVT_E/hqdefault.jpg',
            'treat: http://2.bp.blogspot.com/_rzdB5a4kLAo/THbY9-VGbLI/AAAAAAAAVjY/INzjpgmJIk8/s1600/e59b_stay_puft_marshmallows.jpg',
            'trick: https://v.cdn.vine.co/r/avatars/678A1382AC1394436560929370112_10abb68344d.3.4.jpg?versionId=thOdcbEvqApSRbfgPk8WYGJYg5rwH3ZH',
            'treat: http://sweets.seriouseats.com/images/images/2011/10/20111011-candy-a-day-nerds.jpg',
            'trick: http://static2.hypable.com/wp-content/uploads/2015/05/Dementor-wasp-2.jpg',
            'treat: https://pioneerpartyandgift.com/image/cache/data/product/pioneer_party_eyeball_gumballs-500x500.jpg',
            'trick: http://i.imgur.com/nbcTtZC.gif',
            'treat: http://www.zombiegift.com/zombie-blog/wp-content/uploads/2014/01/zombie-bar-chocolate-bar-sugar-plum-chocolates-zombie-chocolate-bar-review11.jpg',
            'trick: http://media.tumblr.com/tumblr_lkqcixv4UN1qd3url.gif',
            'treat: https://cdn.instructables.com/FM3/X5MC/H88XIJR6/FM3X5MCH88XIJR6.MEDIUM.jpg',
            'trick: http://img00.deviantart.net/12db/i/2006/185/a/4/jack_skellington_by_kev2137.jpg',
            'treat: http://melvillecandy.com/assets/images/spooky_assortment.jpg',
            'trick: https://upload.wikimedia.org/wikipedia/commons/2/2f/Roachies.JPG',
            'treat: https://cdn.discordapp.com/attachments/237897212791619584/242635869884776451/download_31.jpg',
            'trick: http://akphoto4.ask.fm/887/424/258/910003021-1sall78-c0gn67b3hog258a/original/Riddlesolved.jpg',
            'treat: http://www.partycity.com/images/products/en_us/gateways/candy-2015/candy-by-type/candy-by-type-bubblegum.jpg',
            'trick: http://i2.kym-cdn.com/photos/images/original/001/063/320/27c.jpg',
            'treat: http://67.media.tumblr.com/268692a326296b9571409c235cc6ac44/tumblr_inline_nyws9cnoXd1tbiwft_1280.jpg',
            'trick: http://vignette2.wikia.nocookie.net/freddy-fazbears-pizza/images/0/0f/FNAFSL_Ennard_Model.png/revision/latest/',
            'treat: https://s-media-cache-ak0.pinimg.com/736x/84/eb/ce/84ebce7a284c1c40d20b4aa1dd13734c.jpg'
                ]

        if (cmonth == 10 and cday == 31):
            await self.bot.say('{0} got a {1}'.format(trickortreater, random.choice(surprise)))
        else:
            await self.bot.say('**Oh, it isn\'t Halloween today! Come back on 31st of October!**')

    @commands.command()
    async def adventcalendar(self):
        """Get gifts on each of the 25 days leading up to Christmas!"""
        d = datetime.date.today()
        cday = d.day
        cmonth = d.month

        if (cmonth == 12 and cday == 1):
            await self.bot.say('http://www.tabletalkatlarrys.com/wp-content/uploads/2010/12/Peppermint-candies.jpg')
        elif (cmonth == 12 and cday == 2):
            await self.bot.say('http://richmedia.channeladvisor.com/ImageDelivery/imageService?profileId=52000717&imageID=162591372&recipeId=243')
        elif (cmonth == 12 and cday == 3):
            await self.bot.say('http://www.candywarehouse.com/assets/item/regular/Haribo--Christmas-Edition-131710.jpg')
        elif (cmonth == 12 and cday == 4):
            await self.bot.say('http://demandware.edgesuite.net/sits_pod26/dw/image/v2/AAWA_PRD/on/demandware.static/-/Sites-wilton-project-master/default/dw01737e3d/images/project/WLPROJ-7070/GbCtgBWeb2436-lg.jpg?sw=502&sh=502&sm=fit')
        elif (cmonth == 12 and cday == 5):
            await self.bot.say('https://img.mygiftcardsupply.com/wp-content/uploads/2016/03/steam-gift-card-100.png')
        elif (cmonth == 12 and cday == 6):
            await self.bot.say('http://www.nobiggie.net/wp-content/uploads/2014/11/Spiced-Gingerbread-Man-Cookies-plus-24-more-Christmas-Cookies.jpg')
        elif (cmonth == 12 and cday == 7):
            await self.bot.say('https://cdn1.tnwcdn.com/wp-content/blogs.dir/1/files/2016/07/Pokedex3-1-796x532.jpg')
        elif (cmonth == 12 and cday == 8):
            await self.bot.say('http://3.bp.blogspot.com/-Cbtr51gIWCc/T73eYWTCUNI/AAAAAAAACeY/OSNbIyxg-Jo/s1600/Hasbro+Marvel+Legends+The+Avengers+Assemble+6+Inch+Walmart+Exclusive+Action+Figures+Captain+America+Steve+Rogers+2012+(3).JPG')
        elif (cmonth == 12 and cday == 9):
            await self.bot.say('http://www.noblecollection.com/ItemImages/Large/PRP%20HP%208050.jpg')
        elif (cmonth == 12 and cday == 10):
            await self.bot.say('http://www.toysrus.com/graphics/product_images/pTRU1-20641450enh-z6.jpg')
        elif (cmonth == 12 and cday == 11):
            await self.bot.say('http://www.thetanooki.com/wp-content/uploads/2015/06/150606pokemonamiibo.jpg')
        elif (cmonth == 12 and cday == 12):
            await self.bot.say('http://vignette3.wikia.nocookie.net/phineasandferb/images/a/a9/Perry_12_inch_plush_toy.jpg/revision/latest?cb=20100913050211')
        elif (cmonth == 12 and cday == 13):
            await self.bot.say('https://cdn.shopify.com/s/files/1/0207/8554/products/socksmith_tangled_christmas_lights_in_green_fun_mens_socks_large.jpg?v=1472576578')
        elif (cmonth == 12 and cday == 14):
            await self.bot.say('http://cdn.wallpapersafari.com/21/51/B4h3me.jpg')
        elif (cmonth == 12 and cday == 15):
            await self.bot.say('http://thumbs3.ebaystatic.com/d/l225/pict/282077319349_1.jpg')
        elif (cmonth == 12 and cday == 16):
            await self.bot.say('https://www.outerrimtradingco.com.au/graphics/products/extra/mixels06box.jpg')
        elif (cmonth == 12 and cday == 17):
            await self.bot.say('http://ecx.images-amazon.com/images/I/91J5dOT2FQL._SL1500_.jpg')
        elif (cmonth == 12 and cday == 18):
            await self.bot.say('http://cdn.collider.com/wp-content/uploads/2015/09/star-wars-the-force-awakens-toy-bb8-in-box.png')
        elif (cmonth == 12 and cday == 19):
            await self.bot.say('https://ae01.alicdn.com/kf/HTB18NFuKVXXXXa1aXXXq6xXFXXXb/FPV-Quadcopter-Dron-Camera-Quadcopter-Control-Remote-Helicopter-Rc-With-Con-Radio-Copter-Quad-Hd-Heli.jpg_640x640.jpg')
        elif (cmonth == 12 and cday == 20):
            await self.bot.say('http://topgamescdkeys.com/wp-content/uploads/2016/03/OVERWATCH-dvd.jpg')
        elif (cmonth == 12 and cday == 21):
            await self.bot.say('http://www.nintendo.com/images/page/3ds/what-is-3ds/hero-new-3ds.png')
        elif (cmonth == 12 and cday == 22):
            await self.bot.say('https://cdn2.pcadvisor.co.uk/cmsdata/features/3635760/pokemon_sun_and_moon_fan_edition_thumb.jpg')
        elif (cmonth == 12 and cday == 23):
            await self.bot.say('http://cupcakerehab.com/blog/wp-content/uploads/2010/11/figgy-pudding1-300x242.jpg')
        elif (cmonth == 12 and cday == 24):
            await self.bot.say('http://instamoz.com/images/304ce4f4b47f04c1299895d221e917e8.jpg')
        elif (cmonth == 12 and cday == 25):
            await self.bot.say('Merry Christmas! Your final gift is... https://www.cyberpowerpc.com/images/cs/obsidian750dair/blk_220.png')
        else:
            await self.bot.say('**It\'s not Christmas time! Come back later to use the Advent Calendar!**')


def setup(bot):
    bot.add_cog(Seasonal(bot))
