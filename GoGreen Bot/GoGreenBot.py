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
bot = commands.Bot(command_prefix='#', intents=intents)
choice = []
@bot.event
async def on_ready():
    print(f'Kita telah masuk sebagai {bot.user}')

@bot.command()
async def hello(ctx):
     await ctx.send(f'Hi! I am a bot {bot.user}! im here to guide you 😃\n'
                    'this are a few commmands you can use here 👇\n'
                    '#guide : untuk melihat daftar tips yang bisa di cari')

@bot.command()
async def guide(ctx):
     await ctx.send(
         'Hi!, berikut adalah beberapa guide yang bisa kamu cari \n'
         '#plastik : untuk menampilkan tips bagaimana cara mengurangi sampah plastik\n'
         '#makanan : untuk menampilkan bagaimana cara mengurangi limbah makanan\n'
         '#kendaraan : untuk menampilkan bagaimana cara mengurangi polusi kendaraan\n'
         '#udara : untuk menampilkan bagaimana cara mengunragi polusi udara'
         )

@bot.command('plastik')
async def plastik(ctx):
    file_name = 'Plastik.png'
    with open('/Users/ahzafatahar-rayyan/Documents/Coding/Other code/test/GoGreen/Tips/' + file_name, 'rb') as f:
        # Mari simpan file perpustakaan/library Discord yang dikonversi dalam variabel ini!
        picture = discord.File(f)
   # Kita kemudian dapat mengirim file ini sebagai tolok ukur!
    await ctx.send(file=picture)

@bot.command('makanan')
async def makanan(ctx):
    file_name = 'Makanan.png'
    with open('/Users/ahzafatahar-rayyan/Documents/Coding/Other code/test/GoGreen/Tips/' + file_name, 'rb') as f:
        # Mari simpan file perpustakaan/library Discord yang dikonversi dalam variabel ini!
        picture = discord.File(f)
   # Kita kemudian dapat mengirim file ini sebagai tolok ukur!
    await ctx.send(file=picture)

@bot.command('kendaraan')
async def kendaraan(ctx):
    file_name = 'kendaraan.png'
    with open('/Users/ahzafatahar-rayyan/Documents/Coding/Other code/test/GoGreen/Tips/' + file_name, 'rb') as f:
        # Mari simpan file perpustakaan/library Discord yang dikonversi dalam variabel ini!
        picture = discord.File(f)
   # Kita kemudian dapat mengirim file ini sebagai tolok ukur!
    await ctx.send(file=picture)

@bot.command('udara')
async def udara(ctx):
    file_name = 'polusi udara.png'
    with open('/Users/ahzafatahar-rayyan/Documents/Coding/Other code/test/GoGreen/Tips/' + file_name, 'rb') as f:
        # Mari simpan file perpustakaan/library Discord yang dikonversi dalam variabel ini!
        picture = discord.File(f)
   # Kita kemudian dapat mengirim file ini sebagai tolok ukur!
    await ctx.send(file=picture)

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

bot.run("MTEzNzYyNDQ2MTY0MjgyNTgzMA.G7D3S3.KqAzXMH-lqmSTt3Ocp0BNWzG6saJA90PTZ3-Ys")