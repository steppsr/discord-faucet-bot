import discord
from discord.ext import commands
import requests

discord_token = "YOUR_DISCORD_TOKEN"

client = commands.Bot(command_prefix="/", intents=discord.Intents.all())

@client.event
async def on_ready():
        print("Bot is ready.")

@client.command()
async def faucet(ctx, *, address=""):
        if "txch" == address[0:4] and len(address) == 63:
                s = address.index("txch")
                e = len(address)
                if address.find(" ", s) >= 0:
                        e = address.index(" ", s)
                address = address[s:e]
                response = requests.get("https://xchdev.com/faucet/index.php?address=" + address)
                await ctx.send(f"{ctx.message.author.mention} Request submitted. Expect 5 to 10 minutes to receive your TXCH.")
        elif "xch" == address[0:3]:
                await ctx.send(f"{ctx.message.author.mention} Invalid testnet address. You may have provided a mainnet address.")
        else:
                await ctx.send(f"{ctx.message.author.mention} Invalid testnet address.")

client.run(discord_token)
