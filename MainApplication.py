import os
import random
import discord

token = open("bot-token","r").read()
print(token)

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message):
    print(message.guild.name)
    if message.author == client.user:
        return

    if message.content.startswith('-cc '):
        token=message.content.split(" ")
        if(token[1]=="8ball"):
            if(len(token)>2):
                rolls=["It is Certain.", "It is decidedly so.", "Without a doubt.", "Yes definitely.",
                        "You may rely on it.", "As I see it, yes.", "Most likely.", "Outlook good.", "Yes.",
                        "Signs point to yes.", "Reply hazy, try again.", "Ask again later.", "Better not tell you now.",
                        "Cannot predict now.", "Concentrate and ask again.", "Don't count on it.", "My reply is no.",
                        "My sources say no.", "Outlook not so good.", "Very doubtful."]

                await message.channel.send(rolls[random.randint(0,19)])
            else:
                await message.channel.send("What is the question?")
        elif(token[1]=="reboot"):
            pass
            #os.system("python3 MainApplication.py")
        else:
            await message.channel.send("Unknown command")

client.run(token)