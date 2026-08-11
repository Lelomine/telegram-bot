import asyncio
from flask import Flask
from threading import Thread
from telethon import TelegramClient, events

# Web Server Render akka hin cufamneef
app = Flask('')

@app.route('/')
def home():
    return "Bot is running 24/7!"

def run_web():
    app.run(host='0.0.0.0', port=8080)

# Telegram Details
API_ID = 27950357
API_HASH = '2a0f544e66ca93ebef00a0dbea2fd706'
SOURCE_CHANNEL = 'BurqaaIspoortii'
MY_CHANNEL = 'Lalosport'

client = TelegramClient('user_session', API_ID, API_HASH)

@client.on(events.NewMessage(chats=SOURCE_CHANNEL))
async def handler(event):
    text = event.raw_text or ""
    text = text.replace(f"@{SOURCE_CHANNEL}", f"@{MY_CHANNEL}")
    text = text.replace(SOURCE_CHANNEL, MY_CHANNEL)
    
    if event.media:
        await client.send_file(f"@{MY_CHANNEL}", event.media, caption=text)
    else:
        await client.send_message(f"@{MY_CHANNEL}", text)

async def start_bot():
    print("Bot-ni kee hojii jalqabeera...")
    await client.start()
    await client.run_until_disconnected()

if __name__ == '__main__':
    Thread(target=run_web).start()
    asyncio.run(start_bot())

