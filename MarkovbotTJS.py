import os
import discord
import markov

client = discord.Client()

@client.event
async def on_ready():
    print(f'Sucessfully connected! Logged in as {client.user}.')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send(chains)


client.run(os.environ['DISCORD_TOKEN'])
