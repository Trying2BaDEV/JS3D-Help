from ast import alias, arguments
from cgi import test
from distutils.log import error
from http.client import responses
from turtle import title
import discord
from discord.ext import commands
import random
from discord import Member
from discord.ext.commands import has_permissions, MissingPermissions

bot = commands.Bot(command_prefix = '.')
client = commands.Bot(command_prefix = '.')

embedmisingmember = discord.Embed(title='ERROR:', description='Please give me the name!', color=0xff0000)
embeddoneban = discord.Embed(title='Banned succesfully!', description='{member.mention} is banned succesfully!', color=0x00ff00)
embedmissingperms = discord.Embed(title='ERROR:', description='Access denied! You dont have the perms to do that!', color=0xff0000)
embeddonekick = discord.Embed(title='Kicked succesfully!', description= f'He/she is kicked succesfully!', color=0x00ff00)

embedhelp = discord.Embed(title="Here are all the commands!", colour=0x00ff00)
embedhelp.set_author(name="JS3D Bot", icon_url="https://cdn.discordapp.com/attachments/844618714439483435/952542066251038810/Schermafbeelding_2022-01-21_195022_2.png")
embedhelp.add_field(name="Command", value=".8ball\n.ping\n.clear\n.ban\n.kick", inline=True)
embedhelp.add_field(name="Description", value="Give me a yes or no question!\nI will show my latency!\nI will delete messages\nI will ban someone\nI will kick someone!", inline=True)
embedhelp.set_footer(text="Wow! A footer!", icon_url="https://cdn.discordapp.com/emojis/754736642761424986.png")



@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game(name=f'on {len(client.guilds)} servers'))
    print('Connected to Cryptus!')

async def ch_pr():
    await client.wait_until_ready()

    satuses = ['a game', f'on {len(client.guilds)} servers | .help', 'discord.py']

#NOT WORKING
#@client.event
#async def on_member_join(member):
#    print(f'{member} has joined has joined a server.')

#@client.event
#async def on_member_remove(member):
#    print(f'{member} has left a server.')

#latency
@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(client.latency * 1000)}ms')

#Arguments algemeen
@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        pass

#8ball
@client.command(aliases=['8ball'])
async def _8ball(ctx, *, question):
    responses = ['It is certain."',
                 'It is decidedly so.',
                 'Without a doubt',
                 'Yes - definitely.',
                 'You may rely on it.',
                 'As I see it, yes.',
                 'Most likely.',
                 'Outlook good. ',
                 'Yes.',
                 'Signs point to yes.',
                 'Reply hazy, try again.',
                 'Ask again later.',
                 'Better not tell you',
                 'Cannot predict now',
                 'Concentrate and ask',
                 "Don't count on it.",
                 "My reply is no.",
                 'My sources say no.',
                 "Outlook not so good.",
                 "Very doubtfull."]
    await ctx.send(f'**Question:** ``{question}``\n**Answer:** ``{random.choice(responses)}``')

#8ball arguments
@_8ball.error 
async def clear_error(ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('I need a question! Please give a question e.g: ``.8ball Will i get a girlfriend?``')

#purge messages
@has_permissions(manage_messages=True, administrator=True)
@client.command()
async def clear(ctx, amount = 2):
    await ctx.channel.purge(limit = amount)

#clear arguments
@clear.error
async def clear_error(ctx,error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('Please specify how many messages i need to delete!')

@clear.error
async def clear_error(ctx,error):
    if isinstance(error, MissingPermissions):
        await ctx.send('You need ``Manage Messages`` or ``Administrator`` permission to do that!')

#ban command
@has_permissions(ban_members=True, administrator=True)
@client.command()
async def ban(ctx,*, member : discord.Member = None, reason=None):
    if member is None:
            await ctx.send(embed=embedmisingmember)
    elif reason is None:
            reason = 'No reason specified!'
            await ctx.send(embed=embeddoneban)
            await member.ban(reason=reason)

@ban.error
async def ban_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send(embed=embedmissingperms)

@has_permissions(ban_members=True, administrator=True)
@client.command()
async def unban(ctx, member:discord.User = None, *, reason=None):
    if member is None:
        await ctx.send(embed=embedmisingmember)
    if reason is None:
        reason = 'No reason specified'
        await ctx.guild.unban(member, reason=reason)

@unban.error
async def unban_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send(embed=embedmissingperms)

#kick command
@has_permissions(kick_members=True, administrator=True)
@client.command()
async def kick(ctx,*, member : discord.Member = None, reason=None):
    if member is None:
        await ctx.send(embed=embedmisingmember)
    elif reason is None:
        reason = 'Reason was not specified'
        await ctx.send(embed=embeddonekick)
        await ctx.guild.kick(member)

@kick.error
async def kick_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send(embed=embedmissingperms)

#help command
@client.command()
async def commands(ctx):
    await ctx.send(embed=embedhelp)

client.run('OTMyNjk5NzQ0MjE4Nzc5Njk5.YeWyUw.6Q7HZgLheZnnoyXul7bWuu86ZlQ')