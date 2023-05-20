import discord
from discord.ext import commands
import requests
from dotenv import load_dotenv
from PIL import Image
import os

discord_token = "YOUR_DISCORD_TOKEN"

load_dotenv()
client = commands.Bot(command_prefix="*", intents=discord.Intents.all())

directory = os.getcwd()
print(directory)

async def make_request(url)
        response = requests.get(url)
        if response.status_code == 200:

                print(f"Request submitted.")

@client.event
async def on_ready():
        print("Bot connected")

@client.event
async def on_message(message):
        for attachment in message.attachments:
                if "/faucet" in message.content or "!faucet" in message.content:
                        if "txch" in message.content:
                                s = message.content.index("txch")
                                e = len(message.content)
                                if message.content.find(" ", s) >= 0:
                                        e = message.content.index(" ", s)
                                address = message.content[s:e]
                                url = "https://xchdev.com/faucet/index.php?address=" + address
                                await make_request(url)
                        elif "xch" in message.content:
                                print("Invalid address. This is a testnet faucet. You provided a mainnet address.")
                        else:
                                print("Missing testnet address.")

client.run(discord_token)
