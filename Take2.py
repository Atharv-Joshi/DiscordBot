import discord
import random
from discord.ext import commands


client = commands.Bot(command_prefix = ".")

with open('C:\\Users\\dell\\Documents\\GitHub\\Token\\Token_File.txt','r') as obj:
    Token_here = obj.read()

client = commands.Bot(command_prefix = ".")

@client.event
async def on_ready():
    #await change_presence(activity = discord.Game(name = 'fortnut'))
    print(f"{client.user} is connected to the guild ")

@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(f'Hi {member.mention}, welcome to our Guild!')
    for channel in member.guild.channels:
        if (str(channel) == "voidmain"):
            await channel.send(f"{member.mention} has joined the guild.")

       
    
@client.event
async def on_member_remove(member):
    print(f"{member} has left the server")
    await member.dm_channel.send(f'{member.mention}! has left the guild')
    for channel in member.guild.channels:
        if (str(channel) == "voidmain"):
            await channel.send(f"{member.mention} has left the guild")

@client.command(aliases = ["Take2","take2","Bot"])
async def _8ball(ctx,*,question):
    responses =['Likely.',
                'Yes - Definitely',
                'Without a doubt',
                'My reply is no',
                'Very doubtful']   
    await ctx.send(random.choice(responses))   

@client.command()
async def clear(ctx,amount = 5):
    if amount == 0:

        await ctx.send(f"You cannot delete {amount} messages.\nPlease enter a proper number.")
    else:
        amount += 1
        await ctx.channel.purge(limit = amount)               

@client.command()
async def ping(ctx):
    await ctx.send(f"pong {round(client.latency *1000)}ms ")

@client.command()
async def marco(ctx):
    await ctx.send("polo")

@client.command()
async def hi(ctx):
    await ctx.send("Hello")    

@client.command()
async def kick(ctx,member : discord.Member,*,reason = None):
    await member.kick(reason = reason)
    
@client.command()
async def ban(ctx,member : discord.Member,*,reason = None):
    await member.ban(reason = reason)
    await ctx.send(f"Banned : {member.mention}")


@client.command()
async def unban(ctx,*,member):
    banned_users = await ctx.guid.bans()
    member_name,member_descriminator = member.split("#")

    for banned_entry in banned_users:
        user = banned_entry.user

        if (member_name,member_descriminator) == (user.name,user.descriminator):
            await ctx.guild.unban(user)
            await ctx.send(f"unbanned : {user.mention}")
            return        

@client.event
async def on_message(message):
    await client.process_commands(message)
    if (message.author == client.user):
        return

    tbbt = ["My Brain is better than EveryBody's",
            "That's my spot",
            "Bazinga PUNK ",
            "I'm not crazy ,my mother had me tested"]    


    if (message.content == 'tbbtquotes'):
        await message.channel.send(random.choice(tbbt))    
    















client.run(f"{Token_here}") 