import discord
from discord.ext import commands
from discord.utils import get
from os import getenv

#outfile = open ("logs.txt", 'a')

intents = discord.Intents.default()
intents.guilds = True
client = commands.Bot(command_prefix = ';')

@client.event
async def on_ready():
    print("ready")

@client.command()
async def a(ctx, *, msg=""):
    await ctx.message.delete()
    if msg !="":
        await ctx.send(f"asking for a friend: {msg}")
        print(f"{ctx.author}: {msg}")
    else:
        await ctx.send("to send an anonymous message, use ```css\n;a [message]```")

@client.command()
async def i(ctx, ser: discord.Guild, chann="",  *, msg=""):
    if chann == "":
        await ctx.send(f"to send an anonymous message, use ```css\n;i {ser} [channel_name] [message]```")
        return
    for chan in ser.text_channels:
        if chan.name == chann:
            if msg !="":
                if chan.permissions_for(ser.get_member(ctx.author.id)).send_messages:
                    print(f"{ctx.author} in {chann}: {msg}")
                    await chan.send(f"asking for a friend: {msg}")
                    await ctx.send("sent! stay bitter!")
                else:
                    await ctx.send("I can't send that >:(")
                return
            else:
                await ctx.send(f"to send an anonymous message, use ```css\n;i {ser} {chann} [message]```")
                return
    await ctx.send(f"to send an anonymous message, use ```css\n;i {ser} [channel_name] [message]```make sure the channel name is written correctly (and exists in the given server)")
    return
client.run(getenv('TOKEN'))
#outfile.close()
