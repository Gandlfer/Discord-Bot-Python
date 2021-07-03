import os
import random
import discord
import datetime

token = open("bot-token","r").read()
#print(token)
intents = discord.Intents.default()
intents.members=True
intents.typing = False
intents.presences = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message):
    
    if message.author == client.user:
        return

    if message.content.startswith('-cc '):
        token=message.content.split(" ")

        if(token[1]=="help"):
            helpEmbed=discord.Embed(title="Commands for CoffeeCup Bot",color=discord.Color.dark_red())
            helpEmbed.add_field(name="Prefix: ",value="-cc <command> <parameters>" ,inline=False)
            helpEmbed.add_field(name="List of commands:", value="8ball\nuser-stat\nserver-stat\ncopypasta")

            await message.channel.send(embed=helpEmbed)

        elif(token[1]=="8ball"):
            if(len(token)>2):
                rolls=["It is Certain.", "It is decidedly so.", "Without a doubt.", "Yes definitely.",
                        "You may rely on it.", "As I see it, yes.", "Most likely.", "Outlook good.", "Yes.",
                        "Signs point to yes.", "Reply hazy, try again.", "Ask again later.", "Better not tell you now.",
                        "Cannot predict now.", "Concentrate and ask again.", "Don't count on it.", "My reply is no.",
                        "My sources say no.", "Outlook not so good.", "Very doubtful."]

                await message.channel.send(rolls[random.randint(0,19)])
            else:
                await message.channel.send("What is the question?")

        elif(token[1]=="server-stat"):
            
            serverEmbed=discord.Embed(title="Server stat for {0}".format(message.guild.name),description=message.guild.description,color=discord.Color.blue())

            serverEmbed.set_thumbnail(url=message.guild.icon_url)
            
            serverEmbed.add_field(name="Server Name: ",value=message.guild.name, inline=True)
            serverEmbed.add_field(name="Server Region: ",value=message.guild.region, inline=True)
            serverEmbed.add_field(name="Server Owner: ",value="{}#{}".format(message.guild.owner.name,message.guild.owner.discriminator), inline=False)
            serverEmbed.add_field(name="Server Made On: ",
                                value="{0} {1} {2} \t".format(message.guild.created_at.strftime("%B"),
                                                        message.guild.created_at.strftime("%d"),
                                                        message.guild.created_at.strftime("%Y")),inline=True)

            serverEmbed.add_field(name="Member Count: ",value=message.guild.member_count,inline=False)
            online,offline,idle,dnd=0,0,0,0
            for x in message.guild.members:
                if(x.status==discord.Status.online):
                    online+=1
                elif(x.status==discord.Status.offline):
                    offline+=1
                elif(x.status==discord.Status.idle):
                    idle+=1
                else:
                    dnd+=1

            serverEmbed.add_field(name="Members Online: ",value=online)
            serverEmbed.add_field(name="Members Idle: ",value=idle)
            serverEmbed.add_field(name="Members DnD: ",value=dnd)
            serverEmbed.add_field(name="Members Offline: ",value=offline)
            
            serverEmbed.set_footer(text="Requested by {}".format(message.author.name,message))
            await message.channel.send(embed=serverEmbed)
            

        elif(token[1]=="user-stat"):
            
            userEmbed= discord.Embed(title="User stat for {0}".format(message.author.nick),color=discord.Color.dark_teal())

            userEmbed.set_thumbnail(url=message.author.avatar_url)

            userEmbed.add_field(name="Name: ",value=message.author.name)
            userEmbed.add_field(name="Status: ",value=message.author.status)
            userEmbed.add_field(name="ID: ",value="{}#{}".format(message.author.name,message.author.discriminator),inline=False)
            userEmbed.add_field(name="Account Creation: ",
                    value="{0} {1} {2} \t".format(message.author.created_at.strftime("%B"),message.author.created_at.strftime("%d"),message.author.created_at.strftime("%Y")),inline=True)
            userEmbed.add_field(name="Joined {} on: ".format(message.guild.name),
                    value="{0} {1} {2}".format(message.author.joined_at.strftime("%B"),message.author.joined_at.strftime("%d"),message.author.joined_at.strftime("%Y")))

            await message.channel.send(embed=userEmbed)

        elif(token[1]=="reboot"):
            pass
            #os.system("python3 MainApplication.py")
        elif(token[1]=="copypasta"):
            copypasta=open("copypasta","r",encoding="utf8").read()
            token=copypasta.split("cawfee")
            await message.channel.send(token[random.randint(0,len(token)-1)])

        else:
            await message.channel.send("Unknown command\n \"-cc help\" for command list")

client.run(token)