import discord
import requests as re
from bs4 import BeautifulSoup
import datetime

client = discord.Client()


def info():
    _show = ''
    urlEni = 'https://www.camphub.in.th/engineer/'
    urlCom = 'https://www.camphub.in.th/computer-it/'
    urlArc = 'https://www.camphub.in.th/architect-finearts/'
    eni_data = re.get(urlEni)
    com_data = re.get(urlCom)
    arc_data = re.get(urlArc)
    eni_soup = BeautifulSoup(eni_data.text, 'html.parser')
    com_soup = BeautifulSoup(com_data.text, 'html.parser')
    arc_soup = BeautifulSoup(arc_data.text, 'html.parser')
    find_eni = eni_soup.find_all('h2', {'class': 'entry-title'})
    find_com = com_soup.find_all('h2', {'class': 'entry-title'})
    find_arc = arc_soup.find_all('h2', {'class': 'entry-title'})

    x = datetime.datetime.now()
    _show += '*----------------------------*\nประจำวันที่ ' + str(
        x) + '\n\n**ค่ายวิศวะ**\n'
    for i in find_eni:
        i = str(i).split('"')
        x = str(i[-1]).split('</a></h2>')
        _show += ('\n' + str(x[0]) + '\n')

    _show += ('\n**ค่ายคอม**\n')
    for i in find_com:
        i = str(i).split('"')
        x = str(i[-1]).split('</a></h2>')
        _show += ('\n' + str(x[0]) + '\n')

    _show += ('\n**ค่ายสถาปัต**\n')
    for i in find_arc:
        i = str(i).split('"')
        x = str(i[-1]).split('</a></h2>')
        _show += ('\n' + str(x[0]) + '\n')
    _show += ('*----------------------------*')
    embed = discord.Embed(title='**CAMP INFO**',
                          description=_show,
                          color=0x33F6FF)
    return (embed)


@client.event
async def on_ready():
    print('login as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$info'):
        await message.channel.send('wait a sec...')
        await message.channel.send(embed=info())
        await message.channel.send('Check more : https://www.camphub.in.th')

    if message.content.startswith('$help'):
        embed = discord.Embed(
            title='**MY COMMANDS**',
            description=
            '**$info** - for camp info!!\n**$donate** - for support devoloper!!',
            color=0x49FF33)
        await message.channel.send(embed=embed)

    if message.content.startswith('$donate'):
        embed = discord.Embed(title='**THANKS FOR SUPPORT**',
                              description='**KBANK 0918872515 ธนกร สอนชิต**',
                              color=0x49FF33)
        await message.channel.send(embed=embed)


client.run((open('token.txt','r')).read())
