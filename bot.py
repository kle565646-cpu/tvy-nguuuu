import os
import discord
from discord.ext import commands
import google.generativeai as genai

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-2.0-flash")

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Đã đăng nhập: {bot.user}")

@bot.command(name="tvyngu")
async def tvyngu(ctx, *, question):
    try:
        response = model.generate_content(question)
        await ctx.send(response.text[:1900])
    except Exception as e:
        await ctx.send(f"Lỗi: {e}")
        
bot.run(os.getenv("TOKEN"))
