import os
import requests
import datetime
from datetime import date
import discord
from discord.ext import commands, tasks

today = date.today()

# Program title :)
os.system("cls")
os.system(
    "TITLE Discord Itemshop boy by revolex")

# Grabs current date, and puts it into Month, Day, Year
d2 = today.strftime("%B %d, %Y")
print("\nCurrent date:", d2)

# -----------------------------------------------------------------------------------------#

#  Put your Twitter API keys, username, and SAC here!
username = 'revolex'
sac = 'DeachOpOp'

# Item Shop Config - leave both configs the same for default. Background urls are NOT supported.

textcolor = 'FFFFFF'
backgroundcolor = '1F1F1F' #1F1F1F

# https://fortniteapi.io API key goes here (ONLY REPLACE THE XXXX PART):

apikey = 'af17b1e9-31ed87dd-c3c75197-4b4d5108'
# -----------------------------------------------------------------------------------------#

# Grabs twitter api keys from settings


# ------------------
response = requests.get('https://pastebin.com/raw/i6UiYQX8')
print('\n------------')
print('Current updates:')
ln1 = response.json()["1"]
ln2 = response.json()["2"]
ln3 = response.json()["3"]
seasonend = response.json()["seasonend"]
currentseason = response.json()["currentseason"]
latestVersion = response.json()["currentVersion"]
leaksimage = response.json()['leaksurl']
print("")
print("")
print(ln1)
print(ln2)
print('------------')
# ------------------

parsedseasonend = seasonend.split(", ")

seasoncountdown = datetime.date(int(parsedseasonend[0]), int(parsedseasonend[1]),
                                int(parsedseasonend[2])) - datetime.date.today()

seasoncountdown = str(seasoncountdown)

print('----------------------------------------------')
print("Supported lines:\n\n")
print('shop = Posts Item Shop')
print('----------------------------------------------\n')

# If user wants to post the shop, then....
def createItemShop():
    print("Running shop for", username)
    url = 'https://api.nitestats.com/v1/shop/image?footer=Creator%20Code%3A%20' + str(sac) + '&textcolor=' + str(
        textcolor) + '&background=' + str(backgroundcolor)
    r = requests.get(url, allow_redirects=True)
    open('shop.png', 'wb').write(r.content)
    print("\nOpened shop.png")
    print("\nSaved shop.png")
    print('Now authorizating discrod bot!')






if __name__ == '__main__':
    createItemShop()

    TOKEN = ''
    bot = commands.Bot(command_prefix='!')

    @bot.command()
    async def itemshop(shop):
        createItemShop()
        print('sended!')
        await shop.send('Магазин на: ' + d2 + ' ✨')
        x = await shop.send('Используй тег автора **DeachOpOp** при покупке товаров в магазине предметов! 🥰',
                               file=discord.File('shop.png'))
        await x.add_reaction(emoji="👍")
        await x.add_reaction(emoji="👎")
        await shop.send('Кидай скрины в канал чтобы получить специальную роль. ✔️')
        await shop.send('С этой ролью ты сможешь играть со стримером **вне очереди**! 🔥')


    @bot.event
    async def on_ready():
        change_status.start()
        print('bot in active')

    @tasks.loop(seconds=10800)
    async def change_status():
        createItemShop()
        channel = bot.get_channel(638652839689846795)
        print('sended!')
        await channel.send('Магазин на: ' + d2 + ' ✨')
        x = await channel.send('Используй тег автора **DeachOpOp** при покупке товаров в магазине предметов! 🥰',
                        file=discord.File('shop.png'))
        await x.add_reaction(emoji="👍")
        await x.add_reaction(emoji="👎")
        await channel.send('Кидай скрины в канал чтобы получить специальную роль. ✔️')
        await channel.send('С этой ролью ты сможешь играть со стримером **вне очереди**! 🔥')



    bot.run(TOKEN)