import os
import discord
from discord.ext import commands

TOKEN = os.environ.get('TOKEN')

bot = commands.Bot(command_prefix='!', description='A Gravy bot for the people')

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

    await bot.change_presence(activity=discord.Game(name="World of Warcraft, obviously"))

@bot.command()
async def gravy(ctx):
    await ctx.send('Gravy for President!')

@bot.command()
async def playgame(ctx):
    await ctx.send('INDIFFERENCE TO GAME!')

@bot.command()
async def favoritemovie(ctx):
    await ctx.send('Rush (with totally naked butts)')

@bot.command()
async def trenchaf(ctx):
    await ctx.send('https://media.giphy.com/media/cA7kvk12D4rvBeb4rR/giphy.gif')

@bot.command()
async def gravybeerface(ctx):
    await ctx.send('https://media.giphy.com/media/PNwk9K1FVvWyw1QDcz/giphy.gif')

@bot.command()
async def info(ctx):
    embed = discord.Embed(title="Gravy Bot", description="To get your daily gravy fix", color=0xeee657)

    # give info about you here
    embed.add_field(name="Author", value="fingedevil")

    # Shows the number of servers the bot is member of.
    embed.add_field(name="Server count", value=f"{len(bot.guilds)}")

    # give users a link to invite this bot to their server
    # embed.add_field(name="Invite", value="[Invite link](<insert your OAuth invitation link here>)")

    await ctx.send(embed=embed)

bot.remove_command('help')

@bot.command()
async def help(ctx):
    embed = discord.Embed(title="Gravy Bot", description="MOAR Gravy!! List of commands are:", color=0xeee657)

    embed.add_field(name="!gravy", value="A vote of confidence for Gravy", inline=False)
    embed.add_field(name="!playgame", value="Ask Gravy bot to play a game", inline=False)
    embed.add_field(name="!favoritemovie", value="Ask Gravy bot what his favorite movie is", inline=False)
    embed.add_field(name="!trenchaf", value="Gravy at peak performance", inline=False)
    embed.add_field(name="!gravybeerface", value="Vintage Gravy", inline=False)
    embed.add_field(name="!info", value="Details on the bot that is Gravy", inline=False)

    await ctx.send(embed=embed)

bot.run(TOKEN)