import os

import discord


token = open("bot-token","r").read()

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')


client.run(token)