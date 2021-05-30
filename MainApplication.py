import os

import discord

token = "NTUwODgzMDE2NTI0NjkzNTA0.XHinyg.Jq_UQI1pikxyjrRVfLI6lW_Eido"

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')


client.run(token)