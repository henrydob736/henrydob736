import asyncio
import random
import re
import time
import os
from datetime import datetime, timedelta
from platform import python_version

from telethon import version, TelegramClient, events
from telethon.errors.rpcerrorlist import (
    MediaEmptyError,
    WebpageCurlFailedError,
    WebpageMediaEmptyError,
)
from telethon.sessions import StringSession
from telethon.events import CallbackQuery

# Replace these with your actual config details
APP_ID = int(os.environ.get("APP_ID", 22030138))
API_HASH = os.environ.get("API_HASH", "c6c02e51a03f6b03dba9ad9a826dc2f1")
LEGEND_STRING = os.environ.get("LEGEND_STRING", "1BVtsOLoBuyROTmacKRT5RB46PvGIxc4YtJlg1xC1kXIDV737IVmtGEFLTWz7xtz8h-Nb1cB12b6WnXIi8ATFgouiUSrtlwmW4Vlyw03NZT_jGrr8NUZoxjEDVZC0P8iJdw6S2L4hER1epC6gAL-obNoARonp95X9LhfM5WnVCtuTcJ9BkyFb-56Krs9ndqyxX4qslKXxQ565lGvZCNfFNCn4uvzNOS728SR_KWpL8W7VvlTCJBZk9DtZdhpmZKcTI-KxEuPYs_qTr0yU2WJ7U6v0OkUZ1Jw6fPOAuHAptEw-tVrzij9FYKzHpumNHkeA6FQcJBXiP7WYxdX5xnHK4elj4uePKAQ=")
BOT_USERNAME = os.environ.get("BOT_USERNAME", "@Hehhvcbot")

# Replace with your custom implementations or imports
def reply_id(event):
    return event.message.reply_to_msg_id

def get_readable_time(seconds):
    return str(timedelta(seconds=seconds))

def check_data_base_health():
    return "Database OK", "No issues"

def gvarstatus(key):
    return "Sample Value"

mention = "@your_mention"
legendversion = "1.0"
StartTime = time.time()

# Session and client setup
session = StringSession(LEGEND_STRING) if LEGEND_STRING else None

legend = TelegramClient(
    session=session,
    api_id=APP_ID,
    api_hash=API_HASH,
    auto_reconnect=True,
    connection_retries=None,
)

@legend.on(events.NewMessage(pattern="legend$"))
async def handle_legend_command(event):
    reply_to_id = reply_id(event)
    uptime = get_readable_time(time.time() - StartTime)
    start = datetime.now()
    legendevent = await event.reply("`Checking...`")
    end = datetime.now()
    ms = (end - start).microseconds / 1000
    _, check_sgnirts = check_data_base_health()
    ALIVE_TEXT = gvarstatus("ALIVE_TEXT")
    EMOJI = gvarstatus("ALIVE_EMOJI") or "✥"
    lal = list(EMOJI.split())
    EMOTES = random.choice(lal)
    sweetie_caption = (
        "**⚜ LegendBot Is Online ⚜**\n\n" + f"{gvarstatus('ALIVE_TEMPLATE')}"
    )
    caption = sweetie_caption.format(
        ALIVE_TEXT=ALIVE_TEXT,
        EMOTES=EMOTES,
        mention=mention,
        uptime=uptime,
        telever=version.__version__,
        legendver=legendversion,
        pyver=python_version(),
        dbhealth=check_sgnirts,
        ping=ms,
    )
    try:
        await legendevent.edit(caption)
    except (WebpageMediaEmptyError, MediaEmptyError, WebpageCurlFailedError):
        await legendevent.edit(
            f"**Media Value Error!!**\n__Change the link by __`.setdv`\n\n**__Can't get media from this link :-**__ `{LEGEND_IMG}`",
        )

@legend.on(events.NewMessage(pattern="alive$"))
async def handle_alive_command(event):
    reply_to_id = reply_id(event)
    uptime = get_readable_time(time.time() - StartTime)
    a = gvarstatus("ALIVE_EMOJI") or "✥"
    kiss = list(a.split())
    EMOJI = random.choice(kiss)
    legend_caption = "**LegendBot Is Online**\n\n"
    legend_caption += f"**{EMOJI} Telethon version :** `{version.__version__}`\n"
    legend_caption += f"**{EMOJI} Legenduserbot Version :** `{legendversion}`\n"
    legend_caption += f"**{EMOJI} Python Version :** `{python_version()}`\n"
    legend_caption += f"**{EMOJI} Uptime :** {uptime}\n"
    legend_caption += f"**{EMOJI} Master:** {mention}\n"
    await event.reply(legend_caption, reply_to=reply_to_id)

@legend.on(CallbackQuery(data=re.compile(b"stats")))
async def on_plug_in_callback_query_handler(event):
    statstext = get_readable_time(time.time() - StartTime)  # Placeholder for actual functionality
    await event.answer(statstext, cache_time=0, alert=True)

# Running the client
with legend:
    legend.run_until_disconnected()