import discord
from discord.ext import commands
from discord import Intents
import requests
import random
import json
import time
import os

with open('Data\\BotData.json') as j:
    BotData = json.load(j)
client = commands.Bot(command_prefix=BotData["Syntax"], intents=Intents.all(), help_command=None)


#--------------------------------------------------------------------------------
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
        UserData.append({"ID":member.id,"Wallet":0,"Bank":0,"WantedLevel":0,"JailTime":0,"Messages":0,"Level":0,"Xp":0,"Items":[],"Crimes":[]})
    
    with open('Data\\UserData.json', 'w') as f:
        json.dump(UserData, f, indent=2)
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
@client.command()
async def invite(ctx):
    await ctx.author.send(requests.get('https://pastebin.com/raw/EAJ6Ng0S').text)
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
@client.command()
async def credit(ctx):
    embed = discord.Embed(
                colour = discord.Colour.blue())
    embed.set_author(name=f"𝐂𝐑𝐄𝐃𝐈𝐓 𝐌𝐄𝐍𝐔", icon_url="https://cdn.discordapp.com/avatars/421717515614289950/2e0e8805ba107885a6449e258bb5d5e2.png?size=256", url="https://discord.gg/aKNDueym5p")
    embed.add_field(name=f"** **", value=f"Creator: ZenoEchozZ#2296\nServer: https://discord.gg/aKNDueym5p\nGithub: https://github.com/NotReeceHarris/EconomyDiscord-Bot", inline=False)
    await ctx.author.send(embed=embed)
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
@client.command()
async def stats(ctx):
    UserData = json.load(open("Data\\UserData.json"))
    BotData = json.load(open("Data\\BotData.json"))
    for x in UserData:
        if x["ID"] == ctx.author.id:
            embed = discord.Embed(
                        colour = discord.Colour.blue(),
                        description=f"**LEVEL** : {x['Level']}\n**XP** : {x['Xp']}\n**BANK** : {str(BotData['Symbol'])}{x['Bank']}\n**WALLET** : {str(BotData['Symbol'])}{x['Wallet']}\n")
            embed.set_author(name=f"{ctx.author.name}'s Stats", icon_url=f"{ctx.author.avatar_url}")
            await ctx.send(embed=embed)
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
@client.command()
async def shop(ctx):
    TempData = json.load(open("Data\\TempData.json"))
    EcoData = json.load(open("Data\\EcoData.json"))
    BotData = json.load(open("Data\\BotData.json"))
    if TempData["DailyShopTime"] < time.time() - 86400:
        TempData1 = json.load(open("Data\\TempData.json"))
        x = []
        w = []
        while True:
            y = random.choice(EcoData["shopItems"])
            if y in w:
                pass
            else:
                x.append(y)
                price = random.randint(y["min"], y["max"])
                w.append({"name": y["name"],"genre": y["genre"],"stock": y["stock"],"price": price, "rarity": round(price / y["max"], 2)})
            if len(x) == BotData["ShopSize"]:
                TempData["DailyShop"] = w
                TempData["DailyShopTime"] = int(time.time())
                json.dump(TempData, open("Data\\TempData.json", "w"), indent=2)
                break
            else:
                pass
    embed = discord.Embed(
        colour = discord.Colour.blue())
    embed.set_author(name=f"𝐒𝐇𝐎𝐏")
    for x in TempData["DailyShop"]:
        embed.add_field(name=f"**{x['name']}**", value=f"`Stock : {x['stock']}`\n`Price : {x['price']}`\n`Rarity: {x['rarity']}`", inline=True)
    await ctx.send(embed=embed)
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
@client.event
async def on_ready():
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=BotData["Status"]))
    print("ready")
#--------------------------------------------------------------------------------

client.run(BotData["Token"])