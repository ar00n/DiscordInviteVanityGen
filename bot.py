import discord
from discord.ext import commands
import json
import asyncio

bot = commands.Bot(command_prefix='$')

key = "BOT_KEY_HERE"

@bot.event
async def on_ready():
    print (bot.user.name + ' is ready')

@bot.command(pass_context=True)
async def vanitygen(ctx, *, vanity):
    global crunching
    crunching = 1
    attempt = 0
    alert = await ctx.send('Discord Invite VanityGen has begun.')
    general = bot.get_channel(CHANNEL_ID_HERE)
    while crunching == 1:
        inv = await general.create_invite()
        invend = str(inv)[18:]
        if vanity.lower() in invend.lower():
            await ctx.send(inv)
            crunching = 0
        else:
            attempt += 1
            alertNew = 'Discord Invite VanityGen has begun. :x:' + str(attempt)
            await alert.edit(content=alertNew)
            await inv.delete()
        await asyncio.sleep(1)

@bot.command(pass_context=True)
async def stop(ctx):
    global crunching
    crunching = 0
    await ctx.send('VanityGen halted.')


bot.run(key)
