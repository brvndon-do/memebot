# Title: MemeBot
# Author: Brandon Do, Andrew Nguyen
# Date: 1/1/2020

import os
import discord

from search import SearchReddit
from commands import Commands
from dotenv import load_dotenv

# load environment variables
load_dotenv()
token = os.getenv('DISCORD_TOKEN')

client = discord.Client()

@client.event
async def on_ready():
    print(f'Logged in to Discord as {client.user}')

@client.event
async def on_message(message:discord.Message):
    if message.author == client.user:
        return
    
    if message.content.startswith('!test'):
        print(f'{message.author} has activated {Commands.Joke.name}')
        await message.channel.send(f'ur a bitch {message.author.mention}')
    
    if message.content.startswith('!memetest'):
        print(f'{message.author} has activated {Commands.Meme.name}')
        meme = SearchReddit()
        await message.channel.send(meme.get_data())

    if message.content.startswith('!paramtest'):
        print(f'{message.author} has activated paramtest')
        params: list = message.content.split(' ')

        print(params)

        if len(params) > 2:
            await message.channel.send(f'You inserted too many parameters - {message.author.mention}')
        elif params[1] == 'baka':
            await message.channel.send(f'ur a fookin baka {message.author.mention}')
        elif params[1] == 'tits':
            await message.channel.send(f'( . Y . ) {message.author.mention}')
        else:
            await message.channel.send(f'Parameter not recognized - {message.author.mention}')

client.run(token)