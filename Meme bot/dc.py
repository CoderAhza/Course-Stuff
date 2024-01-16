import discord
from discord.ext import commands
import random
import os
import requests

# Variabel intents menyimpan hak istimewa bot
intents = discord.Intents.default()
# Mengaktifkan hak istimewa message-reading
intents.message_content = True
# Membuat bot di variabel klien dan mentransfernya hak istimewa
bot = commands.Bot(command_prefix='/', intents=intents)
choice = []
@bot.event
async def on_ready():
    print(f'Kita telah masuk sebagai {bot.user}')

@bot.command()
async def hello(ctx):
     await ctx.send(f'Hi! I am a bot {bot.user}!')

@bot.command()
async def hah(ctx, count_hah = 5):
    await ctx.send("ha" * count_hah)

@bot.command()
async def plus(ctx, left: int, right: int):
    """Adds two numbers together."""
    await ctx.send(left + right)

@bot.command()
async def minus(ctx, left: int, right: int):
    """Adds two numbers together."""
    await ctx.send(left - right)

@bot.command()
async def multiple(ctx, left: int, right: int):
    """Adds two numbers together."""
    await ctx.send(left * right)

@bot.command()
async def divided(ctx, left: int, right: int):
    """Adds two numbers together."""
    await ctx.send(left / right)

@bot.command()
async def meme(ctx):
    file_name = random.choice(os.listdir('/Users/ahzafatahar-rayyan/Documents/Coding/Other code/test/Test/images'))
    with open('/Users/ahzafatahar-rayyan/Documents/Coding/Other code/test/Test/images/' + file_name, 'rb') as f:
        # Mari simpan file perpustakaan/library Discord yang dikonversi dalam variabel ini!
        picture = discord.File(f)
   # Kita kemudian dapat mengirim file ini sebagai tolok ukur!
    await ctx.send(file=picture)

def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']


@bot.command('duck')
async def duck(ctx):
    '''Setelah kita memanggil perintah bebek (duck), program akan memanggil fungsi get_duck_image_url'''
    image_url = get_duck_image_url()
    await ctx.send(image_url)

def get_dog_image_url():    
    url = 'https://random.dog/woof.json'
    res = requests.get(url)
    data = res.json()
    return data['url']

@bot.command('dog')
async def dog(ctx):
    '''Setelah kita memanggil perintah dog (anjing), program akan memanggil fungsi get_dog_image_url'''
    image_url = get_dog_image_url()
    await ctx.send(image_url)

    # if message.author == client.user:
    #     return
    # if message.content.startswith('/halo'):
    #     await message.channel.send("Hi!")
    # elif message.content.startswith('/bye'):
    #     await message.channel.send("👋")
    # elif message.content.startswith('/generate'):
    #     await message.channel.send(Generator(10))
    # else:
    #     await message.channel.send(message.content)

bot.run("MTEyNDMwODU3MjczODY5OTI3Ng.GWao4H.rllm4-izQCreQ797JXpzp0U-xanj98nD12Alvw")