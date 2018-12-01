import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
import random
from discord import Game


Client = discord.client
client = commands.Bot(command_prefix = '.')
Clientdiscord = discord.Client()


@client.event
async def on_member_join(member):
    await client.change_presence(game=Game(name='Im a bot'))
    await client.send_message(member, 'Thanks for joining our server!!')
    print('Sent message to ' + member.name)
async def on_ready():
    await client.change_presence(game=Game(name='Im a bot'))
    print('Ready, Freddy') 


@client.event
async def on_message(message):
    if message.content == '.yt':
        await client.send_message(message.channel,'Subscribe! https://www.youtube.com/channel/UC5eoTT9ZPz_4TLxn81dR5bA')
    if ('fuck') in message.content:
       await client.delete_message(message)
    if ('shit') in message.content:
       await client.delete_message(message)
    if message.content == '.work':
        await client.send_message(message.channel,'why dont u work!')
    if message.content.startswith('.random'):
        randomlist = ["What do u want!", "WTF", "lol, u'r weird"]
        await client.send_message(message.channel,(random.choice(randomlist)))
    if message.content.startswith('.pingmepls'):
        await client.send_message(message.channel,'No! <@%s>'  %(message.author.id))
    if message.content == '.trump':
        em = discord.Embed(description='Wrong!')
        em.set_image(url='https://www.abc.net.au/news/image/9026192-3x2-700x467.jpg')
        await client.send_message(message.channel, embed=em)
    if message.content == '.pewdiepie':
        await client.send_message(message.channel,'T-Gay')
    if ('fck') in message.content:
       await client.delete_message(message)
    if ('dick') in message.content:
       await client.delete_message(message)
    if message.content == '.udumb':
        await client.send_message(message.channel,' u are')
client.run('NTE4NDQ3MzAyNjE3MjAyNjkx.DuRp2Q.x0kDcnW47y3hAt4ovUxLDnR9lT4')
