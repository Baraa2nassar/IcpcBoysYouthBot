'''naassar
Author: Baraa 
Application Name: YouthJun_Bot
'''
import discord
import re, os, time, smtplib
import asyncio
import mysql.connector
from random import randint
from config import *
from discord.ext import commands
#------------------------------------------------------------------------------------------------------------------------------
#if you are copying the code to repl.it start from here: 
intents = discord.Intents.all()
intents.members = True
#bot = commands.Bot(command_prefix = '!', intents=intents)  # add the intents= part to your existing constructor call
client = discord.Client(intents=intents)
#client = discord.Client()

VERIFY_ID = 772789130974330910
SERVER_ID = 702367598238761010
#channel = 702367598238761013 #general chat

@client.event
async def on_ready():
    await client.change_presence(activity = discord.Game(name = "/This bot adds users)"))
    print("We have logged in as {0.user}".format(client))
    refresh = []
    
    
def check_admin(msg):
    roles = msg.author.roles
    
    for role in roles:
        if role.name == "Admin" or role.name == "Committee Members" or role.name == "Committee Staff": 
            return True
    return False
@client.event
async def on_message(message):
    if message.author == client.user:
        return -1;
    if message.content.startswith('hi'):
        await message.channel.send("hello")
    
    if "as" == message.content:
        await message.channel.send("Assalamualaikum Warahmatullahi Wabarakatuh")
        
    if "ws" == message.content.lower():
        await message.channel.send("Walaikum Assalam Wa Rahmatullahi Wa Barakatuh")
    
    if re.search(r"\b(retard|ass|fuck|shit|ass|hell|pussy?|fucker|dick|nigger|bitch|bitch|nig|damn|prick|nigga)s?\b", str(message.content).lower()): # No Bad Language/Cussing
            await message.channel.send("https://gyazo.com/45ad780b2d98f884f00273e3dc0db6cc")
            await message.delete(delay=1)

    if "/baraa" in message.content.lower(): # baraa
        if message.author.id == 670325339263860758:
          await message.channel.send("very well inshAllah")
    if message.content.startswith('/help'): # Help command
        with open("cmds.md") as f:
            cmds = f.read()
        await message.channel.send("__**icpcboysyouth_bot Commands:**__```CSS\n" + cmds + "```")

    if message.content.startswith('/add'): # Add user officially  
        if check_admin(message):
            user_id = re.search("\d{5,}", message.content)
            if user_id:
                guild = client.get_guild(SERVER_ID)
                print ("guild is", guild)
                print("type guild is",type(guild))
                print ("groupID", (int (user_id.group())))
                

                member = guild.get_member(int(user_id.group()))
                if member is None:
                    return None
                print (guild.members[1])
                print ("member is", member) #
                print (member.roles)
                role = discord.utils.get(client.get_guild(SERVER_ID).roles, name= "Youth")
                await member.add_roles(role)
                channel = client.get_channel(702367598238761013)

                await channel.send("<@!" + user_id.group() + "> *has* ***officially*** *joined the IcpcBoysYouth! Welcome your Brother!")

#end here:    
#--------------------------------------------------------------------------------------------------------------------------------------------------
#if message.content.startswith('/name'):
 #       await message.channel.send("hello")
def read_token():
    with open ("token.txt","r") as f:
        lines = f.readlines()
        return lines [0].strip()

TOKEN = read_token()


client.run(TOKEN)

