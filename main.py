import os
import random

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

intents = discord.Intents.default()
intents.members = True
client = discord.Client(intents=intents)


@client.event
async def on_ready():
    for guild in client.guilds:
        if guild.name == GUILD:
            break

    print(
        f'{client.user} is connected to the following guild: \n' 
        f'{guild.name} (id: {guild.id})'
    )

    members = '\n - '.join([member.name for member in guild.members])
    print(f'Guild Members:\n - {members}')


@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome to my Discord server!'
    )


@client.event
async def on_message(message):
    for guild in client.guilds:
        if guild.name == GUILD:
            break
    if message.author == client.user:
        return
    if message.content == "Dog!":
        images = ["https://i.kym-cdn.com/entries/icons/original/000/008/342/ihave.jpg",
                  "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRoeG1Ou26bboi1iGmcRHFXBFHNilxaDmGZUg&usqp=CAU",
                  "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcShDXzpCo448fjzZmzPDJwtAVF4AJKp3lGLHg&usqp=CAU"]

        response = random.choice(images)
        await message.channel.send(response)
    elif message.content == "NewFriend!":
        names = [member.name for member in guild.members]
        names = random.choice(names)
        while names == "Annoying Dog":
            names = random.choice(names)
        await message.channel.send("Here is a new friend for you to connect with! :  -" + names +
                                   "  - Everything is better with friends!")
    elif "encouragement" in message.content or "sad" in message.content:
        words = ["You can do anything you set your mind to!",
                 "You're amazing!",
                 "You're the best!",
                 "You got this!"]

        response = random.choice(words)
        await message.channel.send(response)

client.run(TOKEN)

