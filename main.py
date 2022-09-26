from types import MemberDescriptorType
import discord
import random

no = "https://c.tenor.com/hvtkROeQzQgAAAAC/ben-no.gif"
yes = "https://c.tenor.com/evyoapv3BnsAAAAC/ben-yes.gif"
ho_ho = "https://c.tenor.com/SLBbnychkCkAAAAC/ben-ho-ho-ho.gif"
ugh = "https://c.tenor.com/d2itSSm1PRsAAAAC/ben-ugh.gif"
token = "MTAxOTk2MDM3NDI3NzE4NTU4OA.GUA"+"ckw.tuqSZDSueZZWx_xYArW-7L8yX_kb-8hMDgG0rw"
reactoin = [no, yes, ho_ho, ugh]

intents = discord.Intents.all()
intents.typing = True
intents.presences = True
intents.members = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print("Bot started")

@client.event
async def on_message(ctx):
    if ctx.content.startswith('Бен'):
        react = random.choice(reactoin)
        await ctx.channel.send(react)
        print("Ben say", react)
        
@client.event
async def on_message(ctx):
    if ctx.content.startswith('gachi'):
        await ctx.channel.send("https://media-cdn.tripadvisor.com/media/photo-p/1b/41/a3/eb/hey-bro-nice-dick.jpg")

client.run(token)
