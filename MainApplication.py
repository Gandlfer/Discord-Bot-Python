import os
import random
import discord
import datetime
import mysql.connector
from mysql.connector import errorcode

#import threading

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
    if(userID=="操你妈的逼#9267" or userID=="belair#8279" or userID=="Dań#4617"):
        if(random.randint(0,9)==0):
            await channel.send("Shut the fuck up {}".format(user.mention))
            #Keep talking – someday you’ll say something intelligent.
    # else:
    #     print("{}#{} chatting in {} - {}".format(user.name,user.discriminator,channel,channel.guild.name))
def cardSum(arr):
    cardValue=list()
    flagA=False
    sum=0
    for x in range(0,len(arr)):
        cardValue.append(arr[x][0].split(":")[1][1:])
    
    if "A" in cardValue: flagA=True

    for x in cardValue:
        if x.isnumeric():
            sum+=int(x)
        elif x=="K" or x=="Q" or x=="J":
            sum+=10

    if flagA and sum<=10:
        sum+=11
    elif flagA:
        sum+=1
    
    return sum

def cardsToString(arr):
    string=""
    
    for x in range(0,len(arr)):
        string+=arr[x][0]
          
    string+="\n"

    for x in range(0,len(arr)):
        string+=arr[x][1]  
    return string

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

        elif(token[1]=="copypasta"):

            copypasta=open("copypasta","r",encoding="utf8").read()
            token=copypasta.split("cawfee")

            await message.channel.send(token[random.randint(0,len(token)-1)])

        elif(token[1]=="blackjack"):

            # Message for instructions
            await message.channel.send("{}: hit \n {}: Stop ".format("\U0001F447","\U0000270B"))

            ranksBlack=["<:bA:623575870375985162>","<:b2:623564440574623774>","<:b3:623564440545263626>",
                "<:b4:623564440624824320>","<:b5:623564440851316760>","<:b6:623564440679350319>",
                "<:b7:623564440754978843>","<:b8:623564440826150912>","<:b9:623564440868225025>",
                "<:b10:623564440620630057>","<:bJ:623564440951980084>","<:bQ:623564440851185679>",
                "<:bK:623564440880807956>"]
            ranksRed=["<:rA:623575868672835584>","<:r2:623564440989859851>",
                "<:r3:623564440880545798>","<:r4:623564441103106058>","<:r5:623564440868225035>",
                "<:r6:623564440759173121>","<:r7:623564440964694036>","<:r8:623564440901779496>",
                "<:r9:623564440897454081>","<:r10:623564440863899663>","<:rJ:623564440582881282>",
                "<:rQ:623564440880807936>","<:rK:623564441073614848>"]

            cards=[["<:eclubs:623564441224740866>"],["<:espades:623564441094586378>"],
                ["<:ehearts:623564441065226267>"],["<:ediamonds:623564440926683148>"]]
            for x in range(len(cards)):
                if x < 2:
                    cards[x].extend(ranksBlack)
                else:
                    cards[x].extend(ranksRed)
            dealers=list()
            players=list()

            suits=random.randint(0,len(cards)-1)
            # print(f"Before dealers pop:{len(cards[suits])}")
            dealers.append(list((cards[suits].pop(random.randint(1,len(ranksBlack)-1)),cards[suits][0])))
            dealers.append(["<:blankbacktop:714565166070759454>","<:blankbackbot:714565093798576455>"])
            # print(f"After dealers pop:{len(cards[suits])}")            
            
            # dealerSum=cardSum(dealers)

            suits=random.randint(0,len(cards)-1)
            players.append(list((cards[suits].pop(random.randint(1,len(cards[0])-1)),cards[suits][0])))

            suits=random.randint(0,len(cards)-1)
            players.append(list((cards[suits].pop(random.randint(1,len(cards[0])-1)),cards[suits][0])))

            dealerSumMessage= await message.channel.send("Dealer's cards: {}".format(cardSum(dealers)))
            dealerCardsMessage= await message.channel.send(cardsToString(dealers))

            playerSumMessage= await message.channel.send("Player's cards: {}".format(cardSum(players)))
            playerCardsMessage=await message.channel.send(cardsToString(players))

            await playerCardsMessage.add_reaction("\U0001F447") #hit
            await playerCardsMessage.add_reaction("\U0000270B") #stop

            while True:

                                

                def check(reaction, user):
                    return user == message.author and (str(reaction.emoji) == "\U0001F447" or str(reaction.emoji) == "\U0000270B")

                
                reaction, user = await client.wait_for('reaction_add', timeout=60.0, check=check)
                if(str(reaction.emoji) == "\U0000270B"):
                    break
                else:
                    #check total
                    suits=random.randint(0,len(cards)-1)
                    players.append(list((cards[suits].pop(random.randint(1,len(cards[0])-1)),cards[suits][0])))
                    total=cardSum(players)
                    await playerSumMessage.edit(content="Player's cards: {}".format(total))
                    await playerCardsMessage.edit(content=cardsToString(players))
                    await playerCardsMessage.remove_reaction("\U0001F447", message.author)   
                    if(total>21):
                        await message.channel.send("You lost!")
                        break

                    # print(reaction.emoji)
                    # print(user.name)
                    pass
                
        else:
                
            await message.channel.send("Unknown command\n \"-cc help\" for command list")

if __name__=="__main__":

    token = open("bot-token","r").read().split("\n")
    db=token[1].split(",")

    # try:

    #     mydb=mysql.connector.connect(host=db[0],user=db[1],password=db[2])

    # except mysql.connector.Error:

    #     db=token[2].split(",")
    #     mydb=mysql.connector.connect(host=db[0],user=db[1],password=db[2])

    client.run(token[0])