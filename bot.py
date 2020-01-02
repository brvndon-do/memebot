# Title: MemeBot
# Author: Brandon Do, Andrew Nguyen
# Date: 1/1/2020

import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

# load environment variables
load_dotenv()
token = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print(f'Logged in to Discord as {bot.user.name}')

@bot.command(name='diss', help='Disrespects the user.')
async def diss(ctx, *args): 
    if len(args) == 1:
        await ctx.send('you suck x' + args[0] + f' {ctx.author.mention}')
    else:   
        await ctx.send(f'you suck {ctx.author.mention}')
    
@bot.command(name='paramtest')
async def paramtest(ctx, *args):
    print(f'{ctx.message.author} has activated paramtest')

    if len(args) > 0:
        if args[0] == 'baka':
            await ctx.message.channel.send(f'ur a baka {ctx.author.mention}')    
        elif args[0] == 'tits':
            await ctx.message.channel.send(f'( . Y . ) {ctx.author.mention}')

bot.run(token)
