import discord
from discord.ext import commands
from discord import Intents
import requests
import json
import os

with open('Data\\BotData.json') as j:
    BotData = json.load(j)

client = commands.Bot(command_prefix=BotData["Syntax"], intents=Intents.all(), help_command=None)

@client.event # When the member joins add them to the system
async def on_member_join(member):

    with open('Data\\UserData.json') as j:
        UserData = json.load(j)

    found = False
    for x in UserData:
        if found == True:
            break
        if int(member.id) == int(x["ID"]):
            found = True
    if found == False:
        UserData.append({"ID":member.id,"Wallet":0,"Bank":0,"WantedLevel":0,"JailTime":0,"Items":[],"Crimes":[]})
    
    with open('Data\\UserData.json', 'w') as f:
        json.dump(UserData, f, indent=2)

@client.command()
async def invite(ctx):
    await ctx.author.send(requests.get('https://pastebin.com/raw/EAJ6Ng0S').text)

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f'out for {BotData["Syntax"]}invite'))
    print("ready")

for fn in os.listdir('cogs'):
    if fn.endswith('.py'):
        client.load_extension(f'cogs.{fn[:-3]}')

client.run(BotData["Token"])