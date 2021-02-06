import discord
from discord.ext import commands
from discord import Intents
from backend import randomQue
from datetime import datetime
import requests
import random
import json
import time
import os

with open('Data\\BotData.json') as j:
    BotData = json.load(j)
client = commands.Bot(command_prefix=BotData["Syntax"], intents=Intents.all(), help_command=None)


#-------------------------------------------------------------------------------- done
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
        UserData.append({"ID":member.id,"Warnings":0,"Wallet":0,"Bank":0,"WantedLevel":0,"JailTime":0,"Messages":0,"Xp":0,"Job": None,"EducationLvl":0,"EducationMarks":0,"EducationCooldown": 0,"Items":[],"Crimes":[]})
    
    with open('Data\\UserData.json', 'w') as f:
        json.dump(UserData, f, indent=2)
#--------------------------------------------------------------------------------

#-------------------------------------------------------------------------------- done
@client.command()
async def invite(ctx):
    await ctx.author.send(requests.get('https://pastebin.com/raw/EAJ6Ng0S').text)
#--------------------------------------------------------------------------------

#-------------------------------------------------------------------------------- todo
@client.command()
async def learn(ctx):
    UserData = json.load(open("Data\\UserData.json"))
    BotData = json.load(open("Data\\BotData.json"))
    TempData = json.load(open("Data\\TempData.json"))
    for x in UserData:
        if x["ID"] == ctx.author.id:
            if time.time() - x["EducationCooldown"] < 3600 and x["ID"] not in TempData["TempLearnId"]:
                await ctx.send(f"Your brain is hurting, try again in {int( (time.time() - x['EducationCooldown']) / 60 )} Minute(s)")
            else:
                if ctx.author.id in TempData["TempLearnId"]:
                    for x in TempData["TempLearn"]:
                        await ctx.send(x["que"])
                else:
                    v = randomQue()
                    TempData["TempLearn"].append({"que": v["que"],"anw": v["anw"],"id": ctx.author.id})
                    TempData["TempLearnId"].append(ctx.author.id)
                    x["EducationCooldown"] = int(time.time())
                    json.dump(TempData, open("Data\\TempData.json", "w"), indent=2)
                    json.dump(UserData, open("Data\\UserData.json", "w"), indent=2)
                    await ctx.send(v["que"])
#--------------------------------------------------------------------------------

#-------------------------------------------------------------------------------- done
@client.command()
async def credit(ctx):
    value = BotData["EmbedColor"]
    lv = len(BotData["EmbedColor"])
    colorRGB = tuple(int(value[i:i+lv//3], 16) for i in range(0, lv, lv//3))
    embed = discord.Embed(
                colour = discord.Colour.from_rgb(r=colorRGB[0], g=colorRGB[1], b=colorRGB[2]))
    embed.set_author(name=f"𝐂𝐑𝐄𝐃𝐈𝐓 𝐌𝐄𝐍𝐔", icon_url="https://cdn.discordapp.com/avatars/421717515614289950/2e0e8805ba107885a6449e258bb5d5e2.png?size=256", url="https://discord.gg/aKNDueym5p")
    embed.add_field(name=f"** **", value=f"Creator: ZenoEchozZ#2296\nServer: https://discord.gg/aKNDueym5p\nGithub: https://github.com/NotReeceHarris/EconomyDiscord-Bot", inline=False)
    await ctx.author.send(embed=embed)
#--------------------------------------------------------------------------------

#-------------------------------------------------------------------------------- done
@client.command()
async def stats(ctx):
    UserData = json.load(open("Data\\UserData.json"))
    BotData = json.load(open("Data\\BotData.json"))
    for x in UserData:
        if x["ID"] == ctx.author.id:
            lvl = int(x['Xp']/BotData["XpPerLvl"])
            if x['Job'] == None:
                job = "Unemployed"
            else:
                job = x['Job']
            
            value = BotData["EmbedColor"]
            lv = len(BotData["EmbedColor"])
            colorRGB = tuple(int(value[i:i+lv//3], 16) for i in range(0, lv, lv//3))

            embed = discord.Embed(
                        colour = discord.Colour.from_rgb(r=colorRGB[0], g=colorRGB[1], b=colorRGB[2]))#r=12,g=249,b=48
            embed.add_field(name=f"**𝐒𝐞𝐫𝐯𝐞𝐫 𝐒𝐭𝐚𝐭𝐬**", value=f"**:trophy: LEVEL** : `{lvl:,}`\n**:military_medal: XP** : `{x['Xp']:,}`\n**:speech_balloon: MESSAGES** : `{x['Messages']:,}`", inline=True)
            embed.add_field(name=f"**𝐒𝐞𝐫𝐯𝐞𝐫 𝐂𝐚𝐫𝐞𝐞𝐫**", value=f"**:briefcase:  JOB** : `{job}`\n**:mortar_board: Qualification** : `{x['EducationLvl']}`\n**:white_check_mark: MARKS** : `{x['EducationMarks']}`", inline=True)
            embed.add_field(name=f"** **", value=f"▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔", inline=False)
            embed.add_field(name=f"**𝐒𝐞𝐫𝐯𝐞𝐫 𝐄𝐜𝐨𝐧𝐨𝐦𝐲**", value=f"**:credit_card: BANK** : `{str(BotData['Symbol'])}{x['Bank']:,}`\n**:pound: WALLET** : `{str(BotData['Symbol'])}{x['Wallet']:,}`\n**:gift: ITEMS** : `{len(x['Items']):,}`", inline=True)
            embed.add_field(name=f"**𝐒𝐞𝐫𝐯𝐞𝐫 𝐂𝐫𝐢𝐦𝐞**", value=f"**:chains: JAIL TIME** : `{x['JailTime']} Hours`\n**:fire: CRIME HEAT** : `{x['WantedLevel']}`\n**:exclamation: WARNINGS** : `{x['Warnings']}`", inline=True)
            embed.set_author(name=f"{ctx.author.name}'s Stats", icon_url=f"{ctx.author.avatar_url}")
            await ctx.send(embed=embed)
#--------------------------------------------------------------------------------

#-------------------------------------------------------------------------------- done
@client.command()
async def backpack(ctx):
    UserData = json.load(open("Data\\UserData.json"))
    BotData = json.load(open("Data\\BotData.json"))
    for x in UserData:
        if x["ID"] == ctx.author.id:
            embed = discord.Embed(
                        colour = discord.Colour.blue())
            embed.set_author(name=f"{ctx.author.name}'s Backpack", icon_url=f"https://i.imgur.com/n43fAu8.png")
            if len(x["Items"]) == 0:
                embed.add_field(name=f"**Information**", value=f"You dont have any items in your backpack!", inline=True)
            else:
                for x in x["Items"]:
                    embed.add_field(name=f"**{x['name']}**", value=f"`Stock : {x['stock']}`\n`Price : {x['price']}`\n`Rarity: {x['rarity']}`", inline=True)
            await ctx.send(embed=embed)
#--------------------------------------------------------------------------------

#-------------------------------------------------------------------------------- todo
@client.command()
async def help(ctx, page="1"):
    BotData = json.load(open("Data\\BotData.json"))
    x = str(page)
    s = BotData["Syntax"]

    value = BotData["EmbedColor"]
    lv = len(BotData["EmbedColor"])
    colorRGB = tuple(int(value[i:i+lv//3], 16) for i in range(0, lv, lv//3))

    if x == "1" or x.lower() == "one":
        embed = discord.Embed(
                colour = discord.Colour.from_rgb(r=colorRGB[0], g=colorRGB[1], b=colorRGB[2]),
                description=f"`{s}help [number] (1, 2)`\n`{s}shop`\n`{s}stats`\n`{s}backpack`")
        embed.set_author(name=f"Help menu | Page 1", icon_url=f"https://i.imgur.com/9V25HVB.png")
    elif x == "2" or x.lower() == "two":
        embed = discord.Embed(
                colour = discord.Colour.from_rgb(r=colorRGB[0], g=colorRGB[1], b=colorRGB[2]),
                description=f"`{s}help [number] (1, 2)`\n`{s}shop`\n`{s}stats`\n`{s}backpack`")
        embed.set_author(name=f"Help menu | Page 2", icon_url=f"https://i.imgur.com/9V25HVB.png")
    await ctx.send(embed=embed)
#--------------------------------------------------------------------------------

#-------------------------------------------------------------------------------- done
@client.command()
async def shop(ctx):
    TempData = json.load(open("Data\\TempData.json"))
    EcoData = json.load(open("Data\\EcoData.json"))
    BotData = json.load(open("Data\\BotData.json"))
    value = BotData["EmbedColor"]
    lv = len(BotData["EmbedColor"])
    colorRGB = tuple(int(value[i:i+lv//3], 16) for i in range(0, lv, lv//3))
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
        colour = discord.Colour.from_rgb(r=colorRGB[0], g=colorRGB[1], b=colorRGB[2]))
    embed.set_author(name=f"𝐒𝐇𝐎𝐏", icon_url=f"https://i.imgur.com/lOShv1G.png")
    if int(TempData['DailyShopTime'] - (time.time() - 86400)) < 3600:
        embed.set_footer(text=f"Resets in {int((TempData['DailyShopTime'] - (time.time() - 86400))/60)} Minute(s)")
    else:
        embed.set_footer(text=f"Resets in {int((TempData['DailyShopTime'] - (time.time() - 86400))/3600)} Hour(s)")
    id = 1
    for x in TempData["DailyShop"]:
        embed.add_field(name=f"**{x['name']}**", value=f"`id : {id}`\n`genre : {x['genre']}`\n`Stock : {x['stock']}`\n`Price : {BotData['Symbol']}{x['price']:,}`\n`Rarity: {x['rarity']}`", inline=True)
        id += 1
    await ctx.send(embed=embed)
#--------------------------------------------------------------------------------

#-------------------------------------------------------------------------------- todo
@client.command()
async def job(ctx, *, option=None):
    EcoData = json.load(open("Data\\EcoData.json"))
    UserData = json.load(open("Data\\UserData.json"))
    BotData = json.load(open("Data\\BotData.json"))

    value = BotData["EmbedColor"]
    lv = len(BotData["EmbedColor"])
    colorRGB = tuple(int(value[i:i+lv//3], 16) for i in range(0, lv, lv//3))


    embed = discord.Embed(
            colour = discord.Colour.from_rgb(r=colorRGB[0], g=colorRGB[1], b=colorRGB[2]),
            description=f"`{s}help [number] (1, 2)`\n`{s}shop`\n`{s}stats`\n`{s}backpack`")
    embed.set_author(name=f"Help menu | Page 2", icon_url=f"https://i.imgur.com/9V25HVB.png")
    await ctx.send(embed=embed)
#--------------------------------------------------------------------------------

#-------------------------------------------------------------------------------- done
@client.event
async def on_message(message):
    BotData = json.load(open("Data\\BotData.json"))
    TempData = json.load(open("Data\\TempData.json"))
    UserData = json.load(open("Data\\UserData.json"))
    if message.content.startswith(BotData["Syntax"]):
        pass 
    elif message.author.id in TempData["TempLearnId"]:
        for x in TempData["TempLearn"]:
            if x["id"] == message.author.id:
                if message.content == str(x["anw"]):
                    for z in UserData:
                        if x["id"] == z["ID"]:
                            if z["EducationMarks"] + 1 >= BotData["EducationMarkTillLvl"]:
                                z["EducationLvl"] += 1
                                z["EducationMarks"] = 0
                                json.dump(UserData, open("Data\\UserData.json", "w"), indent=2)
                                await message.channel.send(f"Weldone im going to give you a pass [+1 Qualification]")
                            else:
                                z["EducationMarks"] += 1
                                json.dump(UserData, open("Data\\UserData.json", "w"), indent=2)
                                await message.channel.send(f"Correct welldone, {message.author.name}")
                            TempData["TempLearn"].remove(x)
                            TempData["TempLearnId"].remove(message.author.id)
                            json.dump(TempData, open("Data\\TempData.json", "w"), indent=2)
    else:
        for x in UserData:
            if message.author.id == x["ID"]:
                x["Messages"] += 1
                x["Xp"] += BotData["XpPerMsg"]
        json.dump(UserData, open("Data\\UserData.json", "w"), indent=2)
    
    if not message.author.bot:
        f = open("Data\\ChatLog\\Log.txt", "a")
        f.write(f"[{datetime.utcfromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')}] [{message.author.name}#{message.author.discriminator} / {message.author.id}] : {message.content}\n")
        f.close()
    

    await client.process_commands(message)
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
@client.event
async def on_ready():
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=BotData["Status"]))
    print("ready")
#--------------------------------------------------------------------------------

client.run(BotData["Token"])