from discord.ext import commands
import discord
import os
#from dotenv import load_dotenv

#load_dotenv(".devcontainer/devcontainer.env")

bot_token = os.environ['BOT_TOKEN']
msg_platform = os.environ['CHANNEL_ID']

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print("el bot420 esta pucheado")

@bot.event
async def on_message(message: discord.Message):
    if message.author == bot.user:
        return

    if message.content.startswith('!420'):
        await message.channel.send('Tren de pucho')


bot.run(bot_token)