import discord
from discord.ext import commands
import os
import random
from clasificador import clasf

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hola(ctx):
    await ctx.send("Hola! Soy ReciclaBot y te voy a ayudar con tus problemas de desechos. Para empezar seleccióna que problema tienes:\n $basura: Para saber como separar la basura \n $agua: Para saber como cuidar mejor el agua \n $reciclar: Para saber que reciclar y que no ")

@bot.command()
async def basura(ctx):
    with open('Images/Basura.png', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)
    await ctx.send("Como podemos en esta imagen, deberias separar la basura por si son organicos, inorganicos, de vidrio o plastico. Con esto nos facilitaria la recogida y separada de estos objeto.")

@bot.command()
async def agua(ctx):
    await ctx.send("Para reducir nuestro consumo de agua podemos reducir nuestro tiempo mientras nos bañamos, lavar el carro con cubeto y no con manguera, y no dejar la llave del agua abierta")

@bot.command()
async def check(ctx):
    if ctx.message.attachments:
        for attachment in ctx.message.attachments:
            file_name = attachment.filename
            image_extensions = (".jpg", ".jpeg", ".png")

            if file_name.endswith(image_extensions):
                await attachment.save(f"./images/{file_name}")
                await ctx.send(clasf(f"./images/{file_name}"))
            else:
                await ctx.send("El archivo no es valido")
    else:
        await ctx.send("No se ha adjuntado ningun archivo")

bot.run("code")
