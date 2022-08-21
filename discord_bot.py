import discord 
from config import discord_token as D_TOKEN

client = discord.Client(intents=discord.Intents.default())

@client.event
async def on_ready():
    print("We have logged in as {0.user}".format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$Connect'):
        await message.channel.send('Connected!')

client.run(D_TOKEN)