import os
import random
import discord
from discord.ext import commands
import youtube_dl
from discord import user
# import mysql.connector
# from mysql.connector import errorcode

#import threading

# intents = discord.Intents.default()
# intents.members=True
# intents.typing = True
# intents.presences = True
# client = discord.Client(intents=intents)

client = commands.Bot(command_prefix="-cc")

@client.event
async def on_ready():
    print("Bot Online")

@client.command()
async def play(event, url : str):
    song = os.path.isfile("song.mp3")
    try:
        if song:
            os.remove("song.mp3")
    except PermissionError:
        await event.send("Playing song")

    
    voiceChannel=event.message.author.voice.channel
    print(voiceChannel)
    await voiceChannel.connect()
    voice = discord.utils.get(client.voice_clients,guild=event.guild)

    print(voice.is_connected())
    #if not voice.is_connected():
    
    YDL_OPTIONS = {'format': 'bestaudio', 'noplaylist':'True'}
    FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}

    with youtube_dl.YoutubeDL(YDL_OPTIONS) as ydl:
        try:
            info = ydl.extract_info("ytsearch:%s" % url, download=False)['entries'][0]
        except Exception as e:
            print(e)
    
        print(info)
    # for file in os.listdir("./"):
    #     if file.endswith(".mp3"):
    #         os.rename(file, "song.mp3")
    voice.play(discord.FFmpegPCMAudio(info["url"],**FFMPEG_OPTIONS))

if __name__=="__main__":

    token = open("bot-token","r").read().split("\n")
    db=token[1].split(",")

    client.run(token[0])