from discord.ext import commands
import discord
import os
import re
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

@bot.command(name="420")
async def fourtwenty(context: discord.ext.commands.Context):
    print("!420 invocado")
    await context.channel.send("Tren de pucho")

@bot.command(name="x2")
async def x2(context: discord.ext.commands.Context, arg: str|None):

    print("!x2 invocado con argumento: " + str(arg))

    if not arg:
        await context.channel.send("No escribiste nada broo")
        return
    elif bool(re.search(r'^\d+$', arg)):
        res = int(arg) * 2
    else:
        await context.channel.send("Eso no es un numero broo")
        return

    await context.channel.send("El doble de " + str(arg) + " es " + str(res))

@bot.command(name="sumalos")
async def suma2(context: discord.ext.commands.Context,*args: str|None):


    print("!sumalos invocado con argumentos: " + str(args))

    if not args or not len(args)>=2:
        await context.channel.send("No puedo sumar menos de 2 numeros bro")
        return
    elif bool(re.search(r"^\d+$", args[0])) and bool(re.search(r"^\d+$", args[1])):
        res = int(args[0]) + int(args[1])
    if not bool(re.search(r"^\d+$", args[0])):
        await context.channel.send("El argumento " + str(args[0]) + " no es un numero broo") 
    if not bool(re.search(r"^\d+$", args[1])):
        await context.channel.send("El argumento " + str(args[1]) + " no es un numero broo")
        return

    await context.channel.send("La suma de " + str(args[0]) + " y " + str(args[1]) + " es " + str(res))

bot.run(bot_token)
