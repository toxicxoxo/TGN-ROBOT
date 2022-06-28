import os
import re
from platform import python_version as kontol
from telethon import events, Button
from TGN.events import register
from TGN import telethn as tbot


PHOTO = "https://telegra.ph/file/5433c44cab6436dcd0140.jpg"

@register(pattern=("/donate"))
async def awake(event):
  TEXT = f"**Donate for God **"
  BUTTON = [[Button.url("Razorpay", "")]]
  await tbot.send_file(event.chat_id, PHOTO, caption=TEXT,  buttons=BUTTON)
