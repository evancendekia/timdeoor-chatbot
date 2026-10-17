import os
import discord
from dotenv import load_dotenv

load_dotenv()
intents = discord.Intents.default()
intents.message_content = True 
client = discord.Client(intents=intents) 

@client.event 
async def on_ready(): 
    print("We have logged in as {0.user}".format(client))


@client.event
async def on_message(message): #on_message()is called when the bot receives a message
    if message.author == client.user:
        return

    if message.content.startswith('!hi'):
        await message.channel.send(f'Hello 👋😃')      

client.run(os.environ["DISCORD_TOKEN"])