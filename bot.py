import discord
import time
import os

client=discord.Client()

@client.event #event_decorator
async def on_ready():
    print(f"We have logged in as {client.user}")

@client.event
async def on_message(message):
	if(message.channel.id==584162815812829184):
		if(message.content!="Processing Your Commands" and message.content!="Please Wait"):
			time.sleep(3)
			await message.channel.send("Processing Your Commands")
			time.sleep(6)
			await message.channel.send("Please Wait")


client.run(str(os.environ.get('BOT_TOKEN')))
