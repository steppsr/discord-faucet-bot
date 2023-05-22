import discord
from discord.ext import commands
import requests

discord_token = "YOUR_DISCORD_TOKEN"

client = commands.Bot(command_prefix="/", intents=discord.Intents.all())

@client.event
async def on_ready():
        print("Go Bot!")

@client.command()
async def faucet(ctx, *, address=""):

        # remove whitespace
        address = address.strip()

        # get start & end positions for txch address and set address to that substring
        s = address.index("txch")
        e = len(address)
        if address.find(" ", s) >= 0:
                e = address.index(" ", s)
        address = address[s:e]

        # address should start with "txch" and be 63 characters long otherwise it is an invalid address.
        if "txch" == address[0:4] and len(address) == 63:
                response = requests.get("https://xchdev.com/faucet/index.php?address=" + address)
                await ctx.send(f"{ctx.message.author.mention} Request submitted. Expect 5 to 10 minutes to receive your TXCH.")

        # addresses starting with "xch" are for mainnet and not testnet
        elif "xch" == address[0:3]:
                await ctx.send(f"{ctx.message.author.mention} Invalid testnet address. You may have provided a mainnet address.")

        # could not find a valid testnet address
        else:
                await ctx.send(f"{ctx.message.author.mention} Invalid testnet address.")

client.run(discord_token)
