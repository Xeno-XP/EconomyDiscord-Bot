
<p align=center>

  <img src="https://i.imgur.com/0Eqx8wH.png" alt="EconomyDiscord Bot" />

  <br>
  <br>
  <span>Advanced economy system for discord servers, shops, jobs<br>
rob, and much more there is also a leveling system all at your controll<br></span>
  <br>
  <a target="_blank" href="https://www.python.org/downloads/" title="Python version"><img src="https://img.shields.io/badge/python-3.7|3.8|3.9-green.svg"></a>
  <a target="_blank" href="https://github.com/Rapptz/discord.py" title="Python version"><img src="https://img.shields.io/badge/discord.py-1.6.0-blue.svg"></a>
</p>

<p align="center">
  <a href="#Contributors">Contributors</a>
  &nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#Update">Update</a>
  &nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#Features">Features</a>
  &nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#Screenshots">Screenshots</a>
</p>

## Update
```console
THIS PROJECT IS IN DEVELOPMENT AND NOT FULLY FEATURED, THIS MEANS THERE COULD BE BUGS AND LACK OF FEATURES
```

## Features
* Economy Features
  * Career
    * Education
    * Jobs
    * Maths questions
  * Currency
    * Wallet
    * Bank
  * Crime system
    * Rob
    * Crime heat
    * Murder
  * Shop
    * Items
    * 24 hour resets
* Moderation Systems
  * Warning system
    * Roleplay Identity (Hidden within the roleplay aspect)
  * Activity System
    * Message counter
  * Message logger
  
  
## Commands
```console
[SYNTAX]Shop
[SYNTAX]Job
[SYNTAX]Rob
[SYNTAX]Stats
[SYNTAX]Bal
[SYNTAX]Backpack
[SYNTAX]Buy
[SYNTAX]Gamble
```
## Setting up the bot

<strong>-</strong> First head over to <a href="https://discord.com/developers/applications">discord's developer page</a> 
<strong>-</strong> create a <strong>NEW APPLICATION</strong> and give it a creative name.
<img src="https://i.imgur.com/ssAeYnC.png">
<strong>-</strong> Go to the "Bot" tab and click on "add bot"
<img src="https://i.imgur.com/IRgdtiR.png"> <img src="https://i.imgur.com/MqqrVo3.png">
<strong>-</strong> Scroll down to "Privileged Gateway Intents" and slide "PRESENCE INTENT" and "SERVER MEMBERS INTENT" on!
<img src="https://i.imgur.com/Uj3f137.png">
<strong>-</strong> Then go back the the tab section and go to "Oauh2" select "bot" then scroll down to "BOT PERMISSIONS" and select "administrator"
<strong>-</strong> Click on "copy" and paste the url into your browser
<img src="https://i.imgur.com/bbDwpPD.png">
<strong>-</strong> Select your server and click invite


## How to add items
Within "Data\EcoData.json" add or remove the following.
```console
// Example how to setup
{
      "name": "ItemName",     //  STRING type  : This will disply as the items name.
      "genre": "ItemGenre",   //  STRING type  : This will organise the items within the backpack.
      "stock": 10,            //  INT type     : This is how many can be bought per day.
      "min": 2,               //  INT type     : This is the minimum price it can be.
      "max": 5                //  INT type     : This is the maximum price it can be.
}
```
<h3>Why isnt there 1 price set?</h3>
The price is randomised between the min and max per day and a rarity will be assigned to the item.

```python
price = random.randint(min, max)
rarity = price / max
```
<h3>How does it reset every 24 hours</h3>
A <a href="https://en.wikipedia.org/wiki/Unix_timestamp">unix timestamp</a> is asigned every 24 hours when the `shop` command is called
it will test if its been 24 hours since the last call, if so it will make a random selection for the next shop rotate.

<h3>Example preset item</h3>

```json
{
      "name": ":hotdog: Glizzy",
      "genre": "Food",
      "stock": 10,
      "min": 5,
      "max": 7
}
```

## Custom Embed color
Within "Data/BotData.json" there is a attribute called "EmbedColor" change the value to a hex color code example "fc0202" = Red
```json
{
  "EmbedColor": "fc0202"
}
```

## Screenshots
<img src="https://i.imgur.com/lOG2vOe.png" alt="Lol this didnt load refresh the page" />

## Contributors
* [ZenoEchozZ](https://github.com/NotReeceHarris) 
