import discord
from discord.ext import commands
from config import settings

import requests
from bs4 import BeautifulSoup

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix=settings['prefix'], intents=intents)


def jokes():
    url = 'https://www.anekdots.com/Случайный_анекдот/'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    quotes = soup.find_all('div', class_='marg10')
    a = ""
    for quote in quotes:
        a = quote.text
    return a


@bot.event
async def on_message(ctx):
    if ctx.author != bot.user and f"{settings['prefix']}анекдот" in ctx.content.lower():
        await ctx.reply(jokes())


bot.run(settings['token'])
