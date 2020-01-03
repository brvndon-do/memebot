# Title: MemeBot
# Author: Brandon Do, Andrew Nguyen
# Date: 1/1/2020

import os
import discord

from discord.ext import commands
from dotenv import load_dotenv

from search import SearchReddit

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

@bot.command(name='memetest', help='Pulls a random/specific meme from a subreddit')
async def memetest(ctx, *args):
    print(f'***{ctx.message.author} has activated memetest***')
    reddit = SearchReddit()

    if (len(args) > 0):
        author = reddit.get_data(args[0])['author']
        title = reddit.get_data(args[0])['title']
        subreddit = reddit.get_data(args[0])['subreddit']
        img = reddit.get_data(args[0])['img']
        #await ctx.message.channel.send(f'user: **{author}**\ntitle: **{title}**\nsubreddit: **{subreddit}**\n{img}')
    else:
        author = reddit.get_data()['author']
        title = reddit.get_data()['title']
        subreddit = reddit.get_data()['subreddit']
        img = reddit.get_data()['img']

    await ctx.message.channel.send(img)


bot.run(token)
