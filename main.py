import discord
from discord.ext import commands
from PIL import Image, ImageDraw, ImageFont, ImageFilter , ImageOps
from random import randint
import requests
import os


clnt = commands.Bot(command_prefix = ">", case_insensitive = True)
img = Image.new('RGBA', (400, 400), color = (randint(0,255),randint(0,255),randint(0,255)))
draw = ImageDraw.Draw(img)
channel = clnt.get_channel("430978574833680384")
fnt = ImageFont.truetype(f"{os.path.dirname(__file__)}\F\ALGER.TTF",randint(60,60))

@clnt.event
async def on_ready():
  print(f'ligado {clnt}')

@clnt.command()
async def cn(ctx,arg1,arg2):
  draw.text((300,300), f"{int(arg1)+int(arg2)}", font=fnt,fill=(randint(0,250),randint(0,250),randint(0,250)),stroke_width=1)
  img.save(f'{os.path.abspath(__file__)}pil_text.png',quality=100)
  await ctx.send('working',file=discord.File('bot.pypil_text.png'))

clnt.run('ODYyODMzMzA4MTg1MTMzMDg2.YOeGIw.0QBa_2uqWa9YheULPlDAjH7Gspg')

##~jão
