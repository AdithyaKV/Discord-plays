from discord.ext import commands
import pydirectinput
import time
import json
TOKEN = "YOUR DISCORD TOKEN HERE"

#Select your prefix
bot = commands.Bot(command_prefix="!")

@bot.event
async def on_ready():
    print(f'{bot.user} logged in!')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    await bot.process_commands(message)


file = open("funcs.json")
data = json.load(file)
for i in data:
    exec(f"@bot.command()"
        "\nasync def " + i["name"] + "(ctx):"
        "\n    for i in range("+i["time"]+"):"
        "\n        pydirectinput.keyDown('"+i["button"]+"')"
        "\n        time.sleep("+i["duration"]+")"
        "\n        pydirectinput.keyUp('"+i["button"]+"')")
    
file.close()

bot.run(TOKEN)