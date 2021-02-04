
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
</p>

## Update
```console
THIS PROJECT IS IN DEVELOPMENT
```

## Features
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
},
```
<h3>Why isnt there 1 price set?</h3>
The price is randomised between the min and max per day and a rarity will be assigned to the item.

```python
price = random.randint(min, max)
rarity = price / max
```

// Example preset item
```json
{
      "name": ":hotdog: Glizzy",
      "genre": "Food",
      "stock": 10,
      "min": 5,
      "max": 7
},
```

## Contributors
* [ZenoEchozZ](https://github.com/NotReeceHarris) 

## License

MIT © CryptoniteData<br/>
Original Creator - [Reece Harris](https://github.com/NotReeceHarris)
