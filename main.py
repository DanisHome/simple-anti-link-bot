import discord
from discord.ext import commands
import re

bot = commands.Bot(command_prefix='!')

# Event Listener
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name='Danis Home'))

# Event listener
@bot.event
async def on_message(message):
    # Check if the message was sent by a bot
    if message.author.bot:
        return

    # Regex
    link_regex = r'https?://|\.gg|\.com'

    # Check if the message contains a link
    if re.search(link_regex, message.content):
        await message.delete()  # Deletes the message with the link
        await message.channel.send(f'{message.author.mention}, links are not allowed in this channel!')

    # This is necessary
    await bot.process_commands(message)

# bot token here
bot.run('YOUR_BOT_TOKEN')
