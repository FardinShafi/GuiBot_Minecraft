import discord
from discord import app_commands
import os
from dotenv import load_dotenv
from responses import check_minecraft_server

# Load the token from .env file
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

# Set up the bot
class MinecraftStatusBot(discord.Client):
    def __init__(self):
        super().__init__(intents=discord.Intents.default())
        self.tree = app_commands.CommandTree(self)

    async def setup_hook(self):
        await self.tree.sync()

client = MinecraftStatusBot()

# Define the /server command
@client.tree.command(name="server", description="Check Minecraft server status")
async def server(interaction: discord.Interaction, server_name: str):
    await interaction.response.defer()
    embed = await check_minecraft_server(server_name)
    await interaction.followup.send(embed=embed)

# Run the bot
if __name__ == "__main__":
    client.run(TOKEN)