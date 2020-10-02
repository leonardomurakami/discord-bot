# bot.py
import os

import discord

TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()


@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')


@client.event
async def on_message(message):
    # avaliable commands #
    commands = {
        'help': help,
        'onlyfans': onlyfans
    }
    ######################


    # sexual related reaction #
    sexual_words = [
        'gostoso', 'gostosa', 'peito',
        'bunda', 'sexo', 'comer',
        'foder', 'fode', 'goza'
    ]
    if any(s in message.content.split(' ') for s in sexual_words):
        gachiGasm = client.get_emoji(668618328478056458)
        pogPlant = client.get_emoji(668619108769857548)

        await message.add_reaction(gachiGasm)
        await message.add_reaction(pogPlant)


    #TO-DO: Sexual content based on machine learning model
    ############################

    # help function #
    help = lambda message: message.channel.send('onlyfans')
    #################
    
    # onlyfans function #
    onlyfans = lambda message: message.channel.send('Eu to ligado que você não consegue pagar, eu sou muito caro pra você.')
    #####################

    if message.content.startswith('boa '):
        command = message.content.split(' ')[1:]
        if message.author == client.user:
            return
        else:
            command_to_run = commands[command[0]]
            print(command_to_run)
            await command_to_run(message)
client.run(TOKEN)
