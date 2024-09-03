import asyncio
import random
import os
import time
from datetime import datetime, timedelta

from telethon.sync import TelegramClient
from telethon.sessions import StringSession
from telethon import events

APP_ID = int(os.environ.get("APP_ID", 22030138))
API_HASH = os.environ.get("API_HASH", "c6c02e51a03f6b03dba9ad9a826dc2f1")
LEGEND_STRING = os.environ.get("LEGEND_STRING", "1BVtsOLoBuyROTmacKRT5RB46PvGIxc4YtJlg1xC1kXIDV737IVmtGEFLTWz7xtz8h-Nb1cB12b6WnXIi8ATFgouiUSrtlwmW4Vlyw03NZT_jGrr8NUZoxjEDVZC0P8iJdw6S2L4hER1epC6gAL-obNoARonp95X9LhfM5WnVCtuTcJ9BkyFb-56Krs9ndqyxX4qslKXxQ565lGvZCNfFNCn4uvzNOS728SR_KWpL8W7VvlTCJBZk9DtZdhpmZKcTI-KxEuPYs_qTr0yU2WJ7U6v0OkUZ1Jw6fPOAuHAptEw-tVrzij9FYKzHpumNHkeA6FQcJBXiP7WYxdX5xnHK4elj4uePKAQ=")
BOT_USERNAME = os.environ.get("BOT_USERNAME", "@Hehhvcbot")

mention = "@your_mention"
legendversion = "1.0"
StartTime = time.time()

# Session and client setup
session = StringSession(LEGEND_STRING) if LEGEND_STRING else None

client = TelegramClient(
    session=session,
    api_id=APP_ID,
    api_hash=API_HASH,
    auto_reconnect=True,
    connection_retries=None,
)

IPIC = "https://telegra.ph/file/6bb3994d5789d8e7f2c99.mp4"

async def ping(event):
    """To check ping"""
    type = event.pattern_match.group(1)
    reply_to_id = event.message.reply_to_msg_id
    uptime = str(timedelta(seconds=int(time.time() - StartTime)))
    start = datetime.now()
    if type == " -a":
        legendevent = await event.respond("`!....`")
        await asyncio.sleep(0.3)
        await legendevent.edit("`..!..`")
        await asyncio.sleep(0.3)
        await legendevent.edit("`....!`")
        end = datetime.now()
        tms = (end - start).microseconds / 1000
        ms = round((tms - 0.6) / 3, 3)
        await legendevent.edit(f"**👨‍💻 Average Pong!**\n➥ {ms} ms")
    else:
        legendevent = await event.respond("<b><i>⚡ Pong! ⚡</b></i>", parse_mode="html")
        end = datetime.now()
        ms = (end - start).microseconds / 1000
        ping_temp = (
            "__**☞ Pong**__\n➥ `{ping}` **ms**\n➥ __**Bot of **__{mention}"
        )
        caption = ping_temp.format(
            mention=mention,
            uptime=uptime,
            ping=ms,
        )
        # Send IPIC if it's set
        if IPIC:
            await event.client.send_file(
                event.chat_id,
                IPIC,
                caption=caption,
                reply_to=reply_to_id,
            )
            await legendevent.delete()
        else:
            await event.edit(caption)

# Start the client and add event handler
client.start()
client.add_event_handler(ping, events.NewMessage(pattern="ping( -a|$)"))
client.run_until_disconnected()