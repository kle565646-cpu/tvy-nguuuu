import os
import discord
from discord.ext import commands
import google.generativeai as genai

# ===== API KEY =====
api_key = os.getenv("GOOGLE_API_KEY")

if not api_key:
    raise Exception("Thiếu GOOGLE_API_KEY trong Railway Variables")

genai.configure(api_key=api_key)

model = genai.GenerativeModel("gemini-2.0-flash")

# ===== DISCORD BOT =====
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

        text = response.text if response.text else "Không có phản hồi"
        await ctx.send(text[:1900])

    except Exception as e:
        await ctx.send(f"Lỗi: {e}")

# ===== RUN BOT =====

bot.run(os.getenv("TOKEN"))
