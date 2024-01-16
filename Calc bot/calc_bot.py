import discord
from discord.ext import commands
import random
import requests

# Variabel intents menyimpan hak istimewa bot
intents = discord.Intents.default()
# Mengaktifkan hak istimewa message-reading
intents.message_content = True
# Membuat bot di variabel klien dan mentransfernya hak istimewa
bot = commands.Bot(command_prefix='$', intents=intents)
choice = []
@bot.event
async def on_ready():
    print(f'Kita telah masuk sebagai {bot.user}')

@bot.command()
async def hello(ctx):
     await ctx.send(f'Hi! I am a bot {bot.user}! im here to help your mathemathics problem\n'
                    '$guide : to see what commands you can use')
     
@bot.command()
async def guide(ctx):
     await ctx.send(f'$divided : untuk membagi nomor\n'
                    '$plus : untk menambahkan nomor\n'
                    '$minus : untuk mengurangi nomor\n'
                    '$multiple : untuk mengkali nomor\n')

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


bot.run()
