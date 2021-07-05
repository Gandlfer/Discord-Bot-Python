import os
import random
import discord
import datetime
import mysql.connector
from mysql.connector import errorcode
#import threading

token = open("bot-token","r").read()
#print(token)
intents = discord.Intents.default()
intents.members=True
intents.typing = True
intents.presences = True
client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')
    await client.change_presence(activity=discord.Game(name="with Caffeine"))

@client.event
async def on_typing(channel,user,when):
    userID="{}#{}".format(user.name,user.discriminator)
    if(userID=="DeIeted User#9267" or userID=="belair#8279" or userID=="Dań#4617"):
        if(random.randint(0,4)==0):
            await channel.send("Shut the fuck up {}".format(user.mention))
            #Keep talking – someday you’ll say something intelligent.
    # else:
    #     print("{}#{} chatting in {} - {}".format(user.name,user.discriminator,channel,channel.guild.name))

@client.event
async def on_message(message):
    
    if message.author == client.user:
        return

    if message.content.startswith('-cc'):
        token=message.content.split(" ")

        if(len(token)<=1):
            # print("Called this")
            # def check(m):
            #     return m.content == 'hello' and m.channel == message.channel
            # msg = await client.wait_for('message', check=check)
            await message.channel.send("Unknown command\n \"-cc help\" for command list")
            
        elif(token[1]=="help"):
            helpEmbed=discord.Embed(title="Commands for CoffeeCup Bot",
                        description="Link for invite https://discord.com/api/oauth2/authorize?client_id=550883016524693504&permissions=8&scope=bot"
                        ,color=discord.Color.dark_red())
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
        elif(token[1]=="blackjack"):
            pass
        else:
            await message.channel.send("Unknown command\n \"-cc help\" for command list")

if __name__=="__main__":
    try:
        mydb=mysql.connector.connect(host="192.168.0.252",user="bot",password="Darryllee_99")
    except mysql.connector.Error as err:
        mydb=mysql.connector.connect(host="localhost",user="root",password="")
        # if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        #     print("Something is wrong with your user name or password")
        # elif err.errno == errorcode.ER_BAD_DB_ERROR:
        #     print("Database does not exist")
        # else:
        #     print(err)
    #mydb=mysql.connector.connect(host="192.168.0.252",user="bot",password="Darryllee_99")
    # try:
    #     mydb=mysql.connector.connect(host="210.186.45.55",user="root",password="")
    # except mysql.connector.Error as err:
    #     if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
    #         print("Something is wrong with your user name or password")
    #     elif err.errno == errorcode.ER_BAD_DB_ERROR:
    #         print("Database does not exist")
    #     else:
    #         print(err)
    client.run(token)