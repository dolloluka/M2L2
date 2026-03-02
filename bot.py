import discord
from discord.ext import commands
from config import TOKEN
import os,random
import requests
intents = discord.Intents.default()
intents.message_content=True
bot  = commands.Bot(command_prefix="$",intents=intents)


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.content.startswith('$ geridön'):
        await message.channel.send("selam! geridön komutundan eminmisin??? (eminsen bunu yaz ($ evet))")

    if message.content.startswith('$ evet'):
        await message.channel.send("hazırsan ingilizce bir şekilde rakamları yazdığında başlıyoruzzzzz")

    await bot.process_commands(message)

@bot.command(name="one")
async def image(ctx):
    file = discord.File("images/mem6.png")
    await ctx.send("🔥 kullandığın kitapları okula geri teslim etmelisiniz yoksa çöp olurlar", file=file)


@bot.command(name="two")
async def image(ctx):
    file = discord.File("images/mem6.png")
    await ctx.send("🔥 eski kullanılmış kıyafetlerini kullanılmış kıyafet kutusuna at yoksa  ev de boşuna durur.", file=file)


@bot.command(name="three")
async def image(ctx):
    file = discord.File("images/mem6.png")
    await ctx.send("🔥 yağları torbada biriktirmeliyiz, pilleri bir torbada toplamalıyız ", file=file)


@bot.command(name="four")
async def image(ctx):
    file = discord.File("images/mem5.png")
    await ctx.send("🔥 bu kadar anladıysan anladın anlamadıysan benim sorunum değil ", file=file)

bot.run(TOKEN)