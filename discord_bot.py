import discord 
from config import discord_token as D_TOKEN

import requests
import json

client = discord.Client(intents=discord.Intents.default())

commands = ['!run','!quote','!appointment', '!help']

starter_commands = [
    "Running the bot",
    "Adding appointment...",
    "Adding quote...",
    "etc..."
]

def get_quote():
    response = requests.get('https://zenquotes.io/api/random')
    json_data = json.loads(response.text)
    quote = json_data[0]['q'] + " - " + json_data[0]['a']
    return quote


@client.event
async def on_ready():
    print("We have logged in as {0.user}".format(client))


# a client multilayered event that will accept commands from the user
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    # somthing to inspire
    if message.content.startswith('!inspire'):
        quote = get_quote()
        await message.channel.send(quote)


    if any (word in message.content for word in commands):

        # this matches any command in the message
        await message.channel.send("Running command {}".format(message.content))

# runs the bot
client.run(D_TOKEN)