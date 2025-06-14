import discord
import random
from discord.ext import commands
from Clasificador import identificador

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hola, soy un bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)


@bot.command()
async def Help(ctx):
    await ctx.send("The Commands are $hello , $Help , $CoinFlip , $heh " )

@bot.command()
async def fruitsorter(ctx):
    if ctx.message.attachments:
        for imagen in ctx.message.attachments:
            nombre_imagen = imagen.filename
            url_imagen = imagen.url
            await imagen.save(f"image/{nombre_imagen}")
            await ctx.send(identificador(f"image/{nombre_imagen}"))

            

    else:
        await ctx.send("No se ha adjuntado ninguna imagen")

@bot.command()
async def coinflip(ctx):
    Result = random.randint(1,2)
    if Result == 1:
        await ctx.send(f'The Coin Flip is Tails')
    else:
         await ctx.send(f'The Coin Flip is Heads')

bot.run("")