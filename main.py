import discord
from discord.ext import commands
from model import get_class
import os, random
import requests

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')
def get_no_violence_image_url():
    url = 'https://images.app.goo.gl/bsd6EobtVzYHRafD6'
    res = requests.get(url)
    data = res.json()
    return data['url']
@bot.command('no_violence')
async def violence(ctx):
    '''The violence command returns the photo of the violence'''
    print('hello')
    image_utl = get_no_violence_image_url()
    await ctx.send(image_utl)
@bot.command()
async def heh(ctx):
    if ctx.message.attachments:
        for attachment in ctx.message.attachments:
            file_name = attachment.filename
            file_url = attachment.url
            await attachment.save(f"./{attachment.filename}")
            await ctx.send(get_class(model_path="./keras_model.h5", labels_path="labels.txt", image_path=f"./{attachment.filename}"))
    else:
        await ctx.send("You forgot to upload the image :(")

bot.run("MTMxODMwMDU1MDE2MDE5MTU0OQ.GOeUT-.UFS61nFkHTrl7QjGA41Ro2h-m6diDzYaq1qEHc")