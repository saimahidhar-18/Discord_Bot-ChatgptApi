# app id:1142540327526342716
# public key:4561d063a66798abb13c900d1b34037301ee9e7420735170d95e6ffe66d9bc41
import discord
import os
token = os.getenv("SECRET_KEY");
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")



class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        print(f'Message from {message.author}: {message.content}')
        print(message.mentions)
        if self.user!=message.author:
          if self.user in message.mentions:
            channel=message.channel
            response = openai.Completion.create(
              model="text-davinci-002",
              prompt=message.content,
              temperature=1,
              max_tokens=256,
              top_p=1,
              frequency_penalty=0,
              presence_penalty=0
            )
            messageToSend=response.choices[0].text
            await channel.send(messageToSend)
      

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run(token)
