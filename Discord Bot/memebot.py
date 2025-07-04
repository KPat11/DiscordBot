import discord
import requests
import json

# update the url to https://meme-api.com/gimme
def get_meme():
    response = requests.get('https://meme-api.com/gimme')
    json_data = json.loads(response.text)
    return json_data['url']

# This method is called when the bot has successfully connected to Discord and is ready to start interacting with the API.
class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}')
# Reading and responding to messages
    async def on_message(self, message):
        if message.author == self.user:
            return
        if message.content.startswith('$meme'):
            await message.channel.send(get_meme())

# create intents keyword argument
intents = discord.Intents.default()
intents.message_content = True

#Starting client and authenticating with Discord
#client = MyClient(intents=intents)
#client.run('Your Token here')
