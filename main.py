import discord
import os
from discord.ext import commands
from keep_alive import keep_alive

intents = discord.Intents.default()
intents.messages = True  # Ensure the bot can read messages
intents.message_content = True  # Needed to access message content

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

@bot.event
async def on_message(message):
    # Prevent the bot from responding to its own messages

    # Check if the message contains 'reddit.com'
    if "reddit.com" in message.content:
        # Replace 'reddit.com' with 'rxddit.com'
        modified_message = message.content.replace("reddit.com", "rxddit.com")
        await message.channel.send(f"{modified_message}")

    # Delete the original message
    await message.delete()
    
    # Allow commands to work alongside on_message
    await bot.process_commands(message)

# Run the bot with your token
keep_alive()
bot.run(os.environ['discord_bot_key'])