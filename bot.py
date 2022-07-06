import os
import discord
from dotenv import load_dotenv
from discord.ext import commands, tasks

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents().all()
bot = commands.Bot(command_prefix = "!", intents=intents)

@bot.event
async def on_ready():
    print("Blueberrinnie bot en marche !")

@bot.event
async def on_message(message):
    if (message.content == "Ping" or message.content == "PING" or message.content == "ping"):
        await message.channel.send("Pong")
    await bot.process_commands(message)

@bot.event
async def on_member_join(member):
    channel = bot.get_channel(993872731319832729)
    await channel.send(f"Bienvenue sur le serveur {member.display_name} !")

@bot.command(name="del")
async def delete(ctx, number: int):
    messages = await ctx.channel.history(limit=number + 1).flatten()
    
    for each_message in messages:
        await each_message.delete()

@bot.command(name='say')
async def say(ctx, *, text):
    await ctx.send(text)
    await ctx.message.delete()
    
bot.run(TOKEN)
