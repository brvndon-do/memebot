# Title: MemeBot
# Author: Brandon Do, Andrew Nguyen
# Date: 1/1/2020

import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
from search import RedditSearcher

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
        await ctx.send('you suck' + args[0] + f' {ctx.author.mention}')
    else:   
        await ctx.send(f'you suck {ctx.author.mention}')

@bot.command(name='meme', help='Selects random meme image.')
async def meme(ctx, *args):
    print(f'***{ctx.message.author} has activated command: meme***')
    reddit = RedditSearcher()

    if len(args) == 1:
        name = args[0]
        if reddit.sub_exists(name):
            reddit_data = reddit.get_meme(name)
        else:
            await ctx.send('Provided subreddit does not exist!')
    else:
        reddit_data = reddit.get_meme()
    
    author_name = reddit_data['author']
    thread_title = reddit_data['title']
    subreddit = reddit_data['subreddit']
    img_url = reddit_data['img']
    e = discord.Embed(title=thread_title, url=img_url, color=14485255)
    e.set_author(name=subreddit)
    e.set_image(url=img_url)
    e.set_footer(text='Posted by {0}'.format(author_name))

    await ctx.send(embed=e)

@bot.command(name='joke', help='Tells a joke.')
async def joke(ctx, *args):
    print(f'***{ctx.message.author} has activated command: joke***')
    reddit = RedditSearcher()
    reddit_data = reddit.get_joke()

    author = reddit_data['author']
    title = reddit_data['title']
    text = reddit_data['text']

    await ctx.message.channel.send(f'user: **{author}**\n**{title}**\n{text}\n')

bot.run(token)
