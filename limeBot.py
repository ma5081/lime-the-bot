import discord
from discord.ext import commands
from discord.utils import get


outfile = open ("logs.txt", 'a')

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
    else:
        await ctx.send("to send an anonymous message, use ```;a <message>```")

@client.command()
async def t(ctx, ser: discord.Guild, chann="",  *, msg=""):
    if chann == "":
        await ctx.send(f"to send an anonymous message, use ```;t {serv} <channel_name> <message>```")
        return
    for chan in ser.text_channels:
        if chan.name == chann:
            if msg !="":
                if chan.permissions_for(ctx.author).send_messages:
                    outfile.write(f"{ctx.author} in {chann}: {msg}\n")
                    await chan.send(f"asking for a friend: {msg}")
                    await ctx.send("sent! stay bitter!")
                else:
                    await ctx.send("I can't send that >:(")
                return
            else:
                await ctx.send(f"to send an anonymous message, use ```;t {serv} {chann} <message>```")
                return
    await ctx.send(f"to send an anonymous message, use ```;t {serv} <channel_name> <message>```make sure the channel name is written correctly (and exists in the given server)")
    return
client.run("NzczNjMyOTkxMTc5MDQ2OTIy.X6MD3g.R5M7kvU_FY5MDEMa3QR50PKWbVo")
outfile.close()
