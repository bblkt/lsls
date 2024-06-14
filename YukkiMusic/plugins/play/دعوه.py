
from config import OWNER_ID
import asyncio
from pyrogram import Client, filters
from YukkiMusic.utils.database import get_assistant
from pyrogram.types import Message
from YukkiMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from YukkiMusic.core.call import Yukki


@app.on_message(filters.video_chat_started)
async def brah(_, msg):
       await msg.reply("**تم بدء المكالمه الي وده يسمعنا صوته حياه**")


@app.on_message(filters.video_chat_ended)
async def brah2(_, msg):
       await msg.reply("**واضح اصواتكم حلوه المكالمه تقفلت**")


@app.on_message(filters.video_chat_members_invited)
async def brah3(app :app, message:Message):
           text = f"↞ قام الحلو {message.from_user.mention} \n↞ بدعوتك يا :"
           x = 0
           for user in message.video_chat_members_invited.users:
             try:
               text += f"[{user.first_name}](tg://user?id={user.id})"
               x += 1
             except Exception:
               pass
           try:
             await message.reply(f"{text}")
           except:
             pass
