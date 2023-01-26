import os
import sys
import asyncio
import time
import discord
from discord.ext import commands
os.system("clear")
token = ""

tecno = commands.Bot(command_prefix=";", self_bot=True)

stock = "--------------------------------------------------\n**🤖 Discord Verified Bots 🤖**\n--------------------------------------------------\n**[+] Verified Bots - oge**\n**[+] Verified Bots - oge + intents**\n**[+] Bot With Form**\n**[+] Increasing Your Bot Guilds**\n**[+] Docs To Verify Bot Identity**\n**[+] Mass Bot Adder**\n**[+] Mass Bot Hoster**\n**[+] Mass Guild Botter**\n**[+] Paid Src, Tools, Codes**\n**[+] Auto Stock Sender**\n--------------------------------------------------"

@tecno.event 
async def on_ready():
  print(f"Connected To: {tecno.user}")
  guild = tecno.get_guild(1067517893576769596)
  while True:
    await asyncio.sleep(5)
    for channel in guild.channels:
      if channel.name == "-":
        await channel.send(stock)
        print("[$] Successfully Sent Stock")

@tecno.event
async def on_message(message):
    if message.author == tecno.user:
        return
    if message.channel.type == discord.ChannelType.private:
        await message.channel.send("*Hey, Please Dm Me On `~ Tecno_xD#1603`*\nhttps://discord.com/users/1037585623143428166")

tecno.run(token, bot=False)
