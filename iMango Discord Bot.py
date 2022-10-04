
import requests
import discord
from discord.ext import commands
import json

client = commands.Bot(command_prefix = ".")


def get_info(search):
    url = f"https://google-search3.p.rapidapi.com/api/v1/search/q={search}&num=5"

    headers = {
        "X-User-Agent": "desktop",
        "X-Proxy-Location": "US",
        "X-RapidAPI-Key": "b43be43a44msh52bc86ffba34392p150d9ajsna0b355819458",
        "X-RapidAPI-Host": "google-search3.p.rapidapi.com"
    }
    response = requests.request("GET", url, headers=headers)
    json_data = json.loads(response.text)['results'][0]

    return json_data['title'] + '\n' + json_data['link']


def get_time(location):
    response = requests.get(f'http://worldtimeapi.org/api/timezone/{location}')
    json_data = json.loads(response.text)
    date = json_data['datetime'][:10]
    time = json_data['datetime'][11:19]
    return f'Date is: {date}\nTime is {time}'
def get_stock(ticker):
    url = "https://alpha-vantage.p.rapidapi.com/query"

    querystring = {"interval": "30min", "function": "TIME_SERIES_INTRADAY", "symbol": f"{ticker}", "datatype": "json",
                   "output_size": "compact"}

    headers = {
        "X-RapidAPI-Key": "b43be43a44msh52bc86ffba34392p150d9ajsna0b355819458",
        "X-RapidAPI-Host": "alpha-vantage.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    json_data = json.loads(response.text)['Time Series (30min)']
    close = list(json_data.keys())[0][11:16]
    # return json_data
    highs = {}

    date = list(json_data.keys())[0][:10]
    for i, j in json_data.items():
        if i[:10] != date:
            date = i[:10]


        elif i[:10] == date and i[11:16] == '10:00':
            highs[date + ' Open'] = (j['1. open'])
        elif i[:10] == date and i[11:16] == '16:00':
            highs[date + ' Close'] = j['4. close']

        highs[date + ' Average'] = round((float(j['1. open']) + float(j['4. close'])) / 2,3)

    return highs
@client.event
async def on_ready():
    print('Hello World {0.user}'.format(client))



@client.event
async def on_message(message):
    if message.author == client.user:
        return



    await client.process_commands(message)
@client.command()
async def info(message, *args):
    read_info = get_info('+'.join(list(args)))
    await message.channel.send(read_info)
    print('+'.join(list(args)))

@client.command()
async def stock(message, tck):
    fetched_data = get_stock(tck)
    for i, b in fetched_data.items():
        await message.channel.send(f'{i}: {b}')

@client.command()
async def time(message, location= None):
    if location is not None:
        tell_time = get_time(location)
        await message.channel.send(tell_time)
    else:
        await message.channel.send('pick a timezone from http://worldtimeapi.org/api/timezone')

@client.command()
async def timezones(message):
    timezones = get_timezones()[:150]+ get_timezones()[160:]
    for i in timezones:
        await message.channel.send(timezones)




client.run('MTAwNjIzNjY5MTYzNzQ2OTIxNQ.G_F87m.DXwfAFxIKeJbuQUBQWPm29Gy-oZDlab1gDmNmc')

