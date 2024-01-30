import os
os.system("pip install discord.py==1.7.3")
import discord
import json
import asyncio
from discord.ext import commands

with open('config.json') as f:
    config = json.load(f)

token = config['token']
prefix = config['prefix']
guild_id = int(config['guild_id'])
channel_name = config['channel_name']
message = config['message']
delay = config['delay']
dm_reply = config['dm_reply']
dm_reply_message = config['dm_reply_message']

bot = commands.Bot(command_prefix=prefix, intents=discord.Intents.all(), self_bot=True)

@bot.event
async def on_ready():
    print(f"Connected as {bot.user}")
    guild = bot.get_guild(guild_id)
    if not guild:
        print(f"Guild with ID {guild_id} not found.")
        return
    while True:
        await asyncio.sleep(delay)
        for channel in guild.channels:
            if isinstance(channel, discord.TextChannel) and channel.name == channel_name:
                await channel.send(message)
                print("[$] Successfully Sent Message")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    if dm_reply and message.channel.type == discord.ChannelType.private:
        await message.channel.send(dm_reply_message)

bot.run(token, bot=False)
