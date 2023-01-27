import os
import discord
import openai

openai_apikey = ''
discord_token = ''


class MyClient(discord.Client):
    openai.api_key = openai_apikey

    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, message):
        if message.author == self.user:
            return
        
        object = openai.Completion.create(engine="text-davinci-003",prompt=message.content,temperature=0.4,max_tokens=1000,top_p=1,frequency_penalty=0,presence_penalty=0)
        print(object)
        choices = object['choices']
        text = choices[0]['text']

        await message.channel.send(text)

intents = discord.Intents.default()
intents.message_content = True
client = MyClient(intents=intents)
client.run(discord_token)