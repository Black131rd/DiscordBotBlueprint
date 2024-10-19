from dotenv import load_dotenv
import discord
import os

class DCClient(discord.Client):
    async def on_ready(self):
        print(f'Logged in as {self.user}.')
        print('------')

    async def on_message(self, message):
        # Make the bot not reply to itself.
        if message.author == self.user:
            return
        print(f'New Message sent: [{message.channel}] {message.author}: {message.content}')
        await message.channel.send(message.content)

intents = discord.Intents.default()
intents.messages = True  
intents.message_content = True 

client = DCClient(intents=intents)

load_dotenv()
DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')
client.run(DISCORD_TOKEN)