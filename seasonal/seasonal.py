from discord.ext import commands
import random
import discord
import datetime

class Seasonal:
    """All your cog needs for holidays!""" #Remember: I don't own any of the following images and videos!
    
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def newyear(self):
        """New Year's Wishes!"""
        d = datetime.date.today()
        cday = d.day
        cmonth = d.month

        if (cmonth == 1 and cday == 1):
            await self.bot.say('**HAPPY NEW YEAR @everyone!**')
        else:
            await self.bot.say('**It isn\'t New Year yet! Come back on the first day of the year!**')
    @commands.command()
    async def valentine(self, user : discord.Member):
        """Say it with Red!"""
        d = datetime.date.today()
        cday = d.day
        cmonth = d.month

        if (cmonth == 2 and cday == 14):
            await self.bot.say('**{0}, I love you!** :heart: :rose:')
        else:
            await self.bot.say('**Today isn\'t the day for that... Come back on 14th of February!**')
    @commands.command()
    async def stpaddyday(self):
        """Find the Pot of Gold!"""
        d = datetime.date.today()
        cmonth = d.month

        if cmonth == 3:
            await self.bot.say('**You found the magical Pot of Gold!** http://vignette4.wikia.nocookie.net/fantasy-story/images/0/05/Deluxe_Pot_of_Gold.png/revision/latest?cb=20150310185350')
        else:
            await self.bot.say('**The Leprachauns are asleep, they won\'t be up till March!**')
    @commands.command(pass_context=True)
    async def easter(self, context):
        """Go on an easter egg hunt and find eggs!"""
        egghunter = context.message.author.mention
        
        d = datetime.date.today()
        cmonth = d.month

        egg = {}
        egg['1'] = '**peeps:** https://mymorningchocolate.files.wordpress.com/2010/04/marshmallow-peeps.jpg'
        egg['2'] = '**stickers:** http://i.ebayimg.com/images/g/VDgAAOSwoBtW2Qk5/s-l300.jpg'
        egg['3'] = '**mini-toys:** http://g03.a.alicdn.com/kf/HTB1YrkWLVXXXXa5XXXXq6xXFXXXx/1440-pcs-lot-Pokemon-Pikachu-Raichu-Charizard-Arceus-Mewtwo-mini-figures-Anime-Pocket-Monster-PVC-toys.jpg_640x640.jpg'
        egg['4'] = '**chocolate eggs:** https://cdn.instructables.com/FML/J2OQ/GKI19F8T/FMLJ2OQGKI19F8T.RECT2100.jpg'
        egg['5'] = '**money:** http://i.forbesimg.com/media/2009/12/16/1216_cash-dollars_650x455.jpg'

        if (cmonth == 4):
            await self.bot.say('**{0} found {1}**'.format(egghunter, random.choice([egg[i] for i in egg])))
        else:
            await self.bot.say('**It\'s not Easter! Come back in April for the Easter Egg Hunt!**')
    @commands.command()
    async def fool(self):
        """Try it for yourselves fellas!"""
        d = datetime.date.today()
        cday = d.day
        cmonth = d.month

        if (cmonth == 4 and cday == 1):
            await self.bot.say('**It\'s April 1... You actually waited to use this command. GET REKT SON! THIS DOES NOTHING! You\'ve just been... FOOLED!**')
        else:
            await self.bot.say('**Fool, come back on 1st April!**')
    @commands.command()
    async def earthday(self):
        """Celebrate Earth Day with a Song!"""
        d = datetime.date.today()
        cday = d.day
        cmonth = d.month

        if (cmonth == 4 and cday == 22):
            await self.bot.say('**Celebrate Earth Day!** https://www.youtube.com/watch?v=Slpz0D35oRI')
        else:
            await self.bot.say('**It ain\'t Earth Day, but you can still plant a few trees!**')
    @commands.command()
    async def fourthofjuly(self):
        """Watch the 4th of July Fireworks show!"""
        d = datetime.date.today()
        cday = d.day
        cmonth = d.month

        if (cmonth == 7 and cday == 4):
            await self.bot.say('https://www.youtube.com/watch?v=5ItMkqYeS0Y')
        else:
            await self.bot.say('**Today isn\'t the 4th of July. Come back later for the fireworks show!**')
    @commands.command(pass_context=True)
    async def trickortreat(self, context):
        """Go trick or treating on Discord and get either a trick or a treat! Don't let the tricks spoop you!"""
        trickortreater = context.message.author.mention

        d = datetime.date.today()
        cday = d.day
        cmonth = d.month
    
        surprise = {}
        surprise['1'] = 'trick: https://i.ytimg.com/vi/lwgch2vrZxs/maxresdefault.jpg'
        surprise['2'] = 'treat: https://cdn.shopify.com/s/files/1/0972/7116/products/harry-potter-chocolate-frog-unwrapped4_1024x1024.png?v=1459347352'
        surprise['3'] = 'trick: https://s-media-cache-ak0.pinimg.com/236x/d4/75/5a/d4755aa7bb99a73b38592dd1c4d06df7.jpg'
        surprise['4'] = 'treat: https://i.kinja-img.com/gawker-media/image/upload/s--8Xs1eS4c--/c_scale,fl_progressive,q_80,w_800/evwu1nukixart6mcn8vw.jpg'
        surprise['5'] = 'trick: http://scontent.cdninstagram.com/t51.2885-15/e35/12965880_565667836948598_2099180853_n.jpg?ig_cache_key=MTIzNzgxNDM0OTUxMjMyNDk0MA%3D%3D.2'
        surprise['6'] = 'treat: https://heathersweets.files.wordpress.com/2011/10/haribo-horror-mix-inside.jpg'
        surprise['7'] = 'trick: https://s-media-cache-ak0.pinimg.com/236x/04/3a/68/043a68cbf7789a508d802be4809ed0f1.jpg'
        surprise['8'] = 'treat: http://www.bakingdom.com/wp-content/uploads/2010/11/Delicious-Cauldron-Cakes.jpg'
        surprise['9'] = 'trick: http://vignette4.wikia.nocookie.net/bigbangtheory/images/2/22/Vlcsnap-2011-11-20-15h18m17s164.png/revision/latest?cb=20111120111901'
        surprise['10'] = 'treat :http://metanomicon.net/wp-content/uploads/2011/12/hansolo.jpg'
        surprise['11'] = 'trick: http://cdn.mos.cms.futurecdn.net/k5MFr2h8GviPwuBnuKDzSN-970-80.jpg'
        surprise['12'] = 'treat: http://www.ics.uci.edu/~eppstein/pix/t7bd/BottsBeans-m.jpg'
        surprise['13'] = 'trick: https://i.ytimg.com/vi/4U7l9AvVT_E/hqdefault.jpg'
        surprise['14'] = 'treat: http://2.bp.blogspot.com/_rzdB5a4kLAo/THbY9-VGbLI/AAAAAAAAVjY/INzjpgmJIk8/s1600/e59b_stay_puft_marshmallows.jpg'
        surprise['15'] = 'trick: https://v.cdn.vine.co/r/avatars/678A1382AC1394436560929370112_10abb68344d.3.4.jpg?versionId=thOdcbEvqApSRbfgPk8WYGJYg5rwH3ZH'
        surprise['16'] = 'treat: http://sweets.seriouseats.com/images/images/2011/10/20111011-candy-a-day-nerds.jpg'
        surprise['17'] = 'trick: http://static2.hypable.com/wp-content/uploads/2015/05/Dementor-wasp-2.jpg'
        surprise['18'] = 'treat: https://pioneerpartyandgift.com/image/cache/data/product/pioneer_party_eyeball_gumballs-500x500.jpg'
        surprise['19'] = 'trick: http://i.imgur.com/nbcTtZC.gif'
        surprise['20'] = 'treat: http://www.zombiegift.com/zombie-blog/wp-content/uploads/2014/01/zombie-bar-chocolate-bar-sugar-plum-chocolates-zombie-chocolate-bar-review11.jpg'
        surprise['21'] = 'trick: http://media.tumblr.com/tumblr_lkqcixv4UN1qd3url.gif'
        surprise['22'] = 'treat: https://cdn.instructables.com/FM3/X5MC/H88XIJR6/FM3X5MCH88XIJR6.MEDIUM.jpg'
        surprise['23'] = 'trick: http://img00.deviantart.net/12db/i/2006/185/a/4/jack_skellington_by_kev2137.jpg'
        surprise['24'] = 'treat: http://melvillecandy.com/assets/images/spooky_assortment.jpg'
        surprise['25'] = 'trick: https://upload.wikimedia.org/wikipedia/commons/2/2f/Roachies.JPG'
        surprise['26'] = 'treat: https://cdn.discordapp.com/attachments/237897212791619584/242635869884776451/download_31.jpg'
        surprise['27'] = 'trick: http://akphoto4.ask.fm/887/424/258/910003021-1sall78-c0gn67b3hog258a/original/Riddlesolved.jpg'
        surprise['28'] = 'treat: http://www.partycity.com/images/products/en_us/gateways/candy-2015/candy-by-type/candy-by-type-bubblegum.jpg'
        surprise['29'] = 'trick: http://i2.kym-cdn.com/photos/images/original/001/063/320/27c.jpg'
        surprise['30'] = 'treat: http://67.media.tumblr.com/268692a326296b9571409c235cc6ac44/tumblr_inline_nyws9cnoXd1tbiwft_1280.jpg'
        surprise['31'] = 'trick: http://vignette2.wikia.nocookie.net/freddy-fazbears-pizza/images/0/0f/FNAFSL_Ennard_Model.png/revision/latest/'
        surprise['32'] = 'treat: https://s-media-cache-ak0.pinimg.com/736x/84/eb/ce/84ebce7a284c1c40d20b4aa1dd13734c.jpg'

        if (cmonth == 10 and cday == 31):
            await self.bot.say('{0} got a {1}'.format(trickortreater, random.choice([surprise[i] for i in surprise])))
        else:
            await self.bot.say('**Oh, it isn\'t Halloween today! Come back on 31st of October!**')
    @commands.command(pass_context=True)
    async def thanksgiving(self, context):
        """Get ready for Thanksgiving!"""
        feaster = context.message.author.mention

        d = datetime.date.today()
        cmonth = d.month

        if cmonth == 11:
            await self.bot.say('**{0}, Get down to the dining room for the Thanksgiving feast!** http://gossiplankasinhala.net/wp-content/uploads/2012/11/thanksgiving-dinner-table-setting.jpg'.format(feaster))
        else:
            await self.bot.say('**It\'s not time for Thanksgiving!**')
    @commands.command()
    async def adventcalender(self):
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
            await self.bot.say('**It\'s not December! Come back later to use the Advent Calender!**')
def setup(bot):
    bot.add_cog(Seasonal(bot))
