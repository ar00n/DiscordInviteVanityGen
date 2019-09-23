import discord
from discord.ext import commands
from discord.ext.commands import Bot
import json
import asyncio

bot = commands.Bot(command_prefix=['$'])

key = "BOT_KEY_HERE"

@bot.event
async def on_ready():
    print (bot.user.name + ' is ready')

@bot.command(pass_context=True)
@commands.has_permissions(administrator=True)
async def vanitygen(ctx, *, vanity):
    """Only ??? can run.

    """
    if ctx.message.author.id == 'YOUR_DISCORD_ID_HERE':
        global crunching
        crunching = 1
        attempt = 0
        alert = await bot.say('Discord Invite VanityGen has begun.')
        while crunching == 1:
            inv = await bot.create_invite(ctx.message.channel)
            invend = str(inv)[18:]
            if vanity.lower() in invend.lower():
                await bot.say(inv)
                crunching = 0
            else:
                attempt += 1
                alertNew = 'Discord Invite VanityGen has begun. :x:' + str(attempt)
                await bot.edit_message(alert, new_content=alertNew)
                await bot.delete_invite(inv)
            await asyncio.sleep(1)

@bot.command(pass_context=True)
@commands.has_permissions(administrator=True)
async def stop(ctx):
    global crunching
    crunching = 0
    await bot.say('VanityGen halted.')

bot.run(key)
