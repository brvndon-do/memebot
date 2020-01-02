# Title: MemeBot
# Author: Brandon Do, Andrew Nguyen
# Date: 1/1/2020

import os
import discord
from dotenv import load_dotenv

# load environment variables
load_dotenv()
token = os.getenv('TOKEN')

client = discord.Client()

@client.event
async def on_ready():
    print(f'Logged in to Discord as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content.startswith('!test'):
        print(f'{message.author} has activated command')
        await message.channel.send(f'ur a bitch {message.author.mention}')

client.run(token)