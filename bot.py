import discord
import os
from discord.ext import commands, tasks
import random
from itertools import cycle

#prefix, tidak bisa diganti karena saya malas untuk menambahkan fiturnya
client = commands.Bot(command_prefix='>')
client.remove_command('help')
TOKEN = os.getenv("DISCORD_TOKEN")

#status
status = cycle(['Human Simulator'])
@client.event
async def on_ready():
    change_status.start()
    print("bot is ready")
@tasks.loop (seconds=3)
async def change_status():
    await client.change_presence(activity=discord.Game(next(status)))


#ERRORS
@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send('command tidak ditemukan\n_bila tidak ada kesalahan penulisan, tolong jangan panik karena mungkin saja creator terlalu malas untuk membuat command tersebut_ ._.) _untuk informasi lebih lanjut, silahkan hubungi _contact_ yang tersedia dalam _command:_ >contact')

#HAPUS PESAN
@client.command()
async def clear(ctx, amount =5):
    await ctx.channel.purge(limit=amount)
    await ctx.send ('cleared messages' +amount)

#UMUM
@client.command() #mengecek ping
async def ping(ctx):
    await ctx.send(f'the current latency is: {round(client.latency *1000)}ms')

@client.command() #pat
async def pat(ctx):
    await ctx.send('_uwu, can i have more?_ (ﾉ´ з `)ノ')

@client.command() #morepat
async def morepat(ctx):
    await ctx.send('_ahh kimochiiii desuuu~~_ (ﾉ´ з `)ノ')

@client.command() #i love you
async def ily(ctx):
    await ctx.send('_wanna know a secret?_ \n\n _i love you too!_   ヽ(♡‿♡)ノ')

@client.command() # i hate you
async def ihateyou(ctx):
    await ctx.send('```_but i love you_	(ಥ﹏ಥ) ```')

@client.command() #fuck
async def fuck (ctx, nama:str):
    await ctx.channel.purge(1)
    await ctx.send('fuck you '+nama+' uwu\nhttps://giphy.com/embed/l0MYQCtMEe5WUrskg')

@client.command() #hug
async def hug(ctx, nama:str):
    await ctx.send('hugged '+nama+' _uwu_\nhttps://media.giphy.com/media/ZBQhoZC0nqknSviPqT/giphy.gif')

@client.command() #goodnight
async def goodnight (ctx):
    await ctx.send('_oyasumi_ ♡( ◡‿◡ ) \n_semoga mimpimu indah_')

@client.command() #goodmorning
async def goodmorning (ctx):
    await ctx.send('_ohayouuu!_ ＼(＾▽＾)／ \n_apa kau siap untuk beraktifitas?_')

#MEME
@client.command() #jokes buyung puyuh
async def buyungpuyuh(ctx):
    await ctx.send('_buyung apatuh man?_\nhttps://tenor.com/view/burung-puyuh-burung-apa-bird-burung-apa-itu-gif-17384520')

@client.command() #wahai kerang ajaib, tapi dengan prefix wahai saja suaya bisa dimodifikasi oleh orang lain menjadi wahai biji (orang) atau lain sebagainya
async def wahai(ctx, ask: str):
    answer= random.randint(1,6)
    if answer == 1:
        await ctx.send("```iya```")
    elif answer == 2:
        await ctx.send("```tidak```")
    elif answer == 3:
        await ctx.send("```mungkin iya```")
    elif answer == 4:
        await ctx.send("```mungkin tidak```")
    elif answer == 5:
        await ctx.send("```sangat tidak mungkin```")
    elif answer == 6:
        await ctx.send("```sangat memungkinkan```")

@client.command(pass_context=True)
async def help(ctx):
    author = ctx.message.author

    embed = discord.Embed(
        colour = discord.Colour.blurple()
    )
    embed.set_author(name ='HELP')
    embed.add_field(name='pat', value='+1 pat your bot', inline=False)
    embed.add_field(name='morepat', value='+10 pat your bot', inline=False)
    embed.add_field(name='ily', value='love your bot', inline=False)
    embed.add_field(name='wahai bot ajaib,', value='bot ajaib! ululululu', inline=False)
    embed.add_field(name='buyungpuyuh', value='local meme for you', inline=False)
    embed.add_field(name='ping', value='check your latency', inline=False)
    embed.add_field(name='clear', value='delete some messages', inline=False)
    embed.add_field(name='fuck', value='send a fuck message to a people you hate in the server', inline=False)
    embed.add_field(name='hug', value='send a virtual hug for you', inline=False)
    embed.add_field(name='goodnight', value='send a warm message to make you sleep well', inline=False)
    embed.add_field(name='goodmorning', value='send a warm message to start your day', inline=False)
    embed.add_field(name='creator', value='to see the contact from the man who builds it', inline=False)

    await ctx.send(author, embed=embed)





#@client.command()
#async def contact(ctx, ):
#    embed=discord.embeds (title="this bot is created by 4RC", description="_might develop later_"),
#    embed.add_field(name="instagram:", value="https://instagram.com/aruki_cg"),
#    embed.add_field(name="facebook:", value="https://www.facebook.com/willyam.thung.5"),
#    await client.say(embed=embed)
#    await message.channel.send(embed=embed) #atau #await ctx.send(embed)
#    await ctx.send("this bot is created by 4RC _(might develop later)_\n_instagram:_ https://instagram.com/aruki_cg\n_facebook:_ https://www.facebook.com/willyam.thung.5\n")

@client.command()
async def creator(ctx):
    embed = discord.Embed(
        title = 'About Creator',
        description = 'this bot is created by 4RC\n_might develop later_',
        colour = discord.Colour.blue()
    )

    embed.set_footer(text='all rights reserved.')
#    embed.set_image('https://cdn.discordapp.com/attachments/744159607483793548/744278639969042443/4RC.jpg'),
#    embed.set_thumbnail('https://cdn.discordapp.com/attachments/744159607483793548/744278639969042443/4RC.jpg'),
    embed.set_author(name='Aruki_cg'),
    embed.add_field(name="facebook:", value="https://www.facebook.com/willyam.thung.5", inline=True),
    embed.add_field(name="instagram:", value="https://instagram.com/aruki_cg"),
    await ctx.send(embed=embed)

client.run("TOKEN")
