import discord
import aiohttp

async def check_minecraft_server(server_name: str) -> discord.Embed:
    api_url = f"https://api.mcstatus.io/v2/status/java/{server_name}"
    
    async with aiohttp.ClientSession() as session:
        async with session.get(api_url) as response:
            if response.status == 200:
                data = await response.json()
                
                if data["online"]:
                    embed = discord.Embed(title=f"{server_name} Status", color=discord.Color.green())
                    embed.add_field(name="Status", value="Online", inline=False)
                    
                    players = data["players"]["list"]
                    if players:
                        player_names = "\n".join([player["name_clean"] for player in players])
                        embed.add_field(name="Online Players", value=player_names, inline=False)
                    else:
                        embed.add_field(name="Online Players", value="No players online", inline=False)
                else:
                    embed = discord.Embed(title=f"{server_name} Status", color=discord.Color.red())
                    embed.add_field(name="Status", value="Offline", inline=False)
            else:
                embed = discord.Embed(title="Error", color=discord.Color.red())
                embed.add_field(name="Message", value="Unable to fetch server status.", inline=False)
    
    return embed