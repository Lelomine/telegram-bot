import asyncio
from flask import Flask
from threading import Thread
from telethon import TelegramClient, events
from telethon.sessions import StringSession

app = Flask('')

@app.route('/')
def home():
    return "Bot is running 24/7!"

def run_web():
    app.run(host='0.0.0.0', port=8080)

API_ID = 27950357
API_HASH = '2a0f544e66ca93ebef00a0dbea2fd706'

# String Session haaraa sana asitti marsee (quote '') keessa galchi:
SESSION_STRING = '1BJWap1sBu6lRIQ-748U60WTrvBDBWGK4NveDf0cvVS5rZ0e2fSygIDDf6rE9siM9lSQTw2zXwMOGlq0nBjl0GQXyL_WsVnS414ai8GqapuJjP1uO7eyoHsD0aJ6RxwXEihjjfQ2rkPHRsfcgiKwOTI8jzrhkPD0hHQWocWKtW-IPgitywF5o26laPuucrkWSsJg5sBHd-5sV3ZnxlEwQYDVj37UWpdpDdGHPT_W3hcQWhdMFjNpLJsiodo8FcHPEnry5zMp5wft7sOdDT9zBhrP9AwUUAs6V3JKz47Va2-rxE9DQTs3ZdkS0JkAIykpJJW5m9usU6sMPz56d0u4G25yBeg_6N8c='

SOURCE_CHANNEL = 'BurqaaIspoortii'
MY_CHANNEL = 'Lalosport'

client = TelegramClient(StringSession(SESSION_STRING), API_ID, API_HASH)

@client.on(events.NewMessage(chats=SOURCE_CHANNEL))
async def handler(event):
    text = event.raw_text or ""
    text = text.replace(f"@{SOURCE_CHANNEL}", f"@{MY_CHANNEL}")
    text = text.replace(SOURCE_CHANNEL, MY_CHANNEL)
    
    footer = f"\n\n📢 Join & Share: @{MY_CHANNEL}"
    full_text = text + footer
    
    if event.media:
        await client.send_file(f"@{MY_CHANNEL}", event.media, caption=full_text)
    else:
        await client.send_message(f"@{MY_CHANNEL}", full_text)

async def start_bot():
    print("Bot-ni kee hojii jalqabeera...")
    await client.start()
    await client.run_until_disconnected()

if __name__ == '__main__':
    Thread(target=run_web).start()
    asyncio.run(start_bot())
