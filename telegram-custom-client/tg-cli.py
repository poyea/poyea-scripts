import time
from datetime import datetime
from telethon import TelegramClient, events
from telethon.tl.functions.account import UpdateUsernameRequest

# tg desktop api id
api_id = 17349
api_hash = '344583e45741c457fe1862106095a5eb'

phone = ''
session_file = '' 
password = ''

if __name__ == '__main__':
    client = TelegramClient(session_file, api_id, api_hash, sequential_updates=True)

    @client.on(events.NewMessage(incoming=True))
    async def handle_new_message(event):
        about_str = 'Running'
        if 'UrRanDOmid' in event.raw_text:
                reply = random.choice(['A', 'B'])
                await event.reply(reply)
        time.sleep(1)
        await client(UpdateProfileRequest(about=about_str))
        time.sleep(30)
    print(time.asctime(), ' ', 'Starting...')
    client.start(phone, password)
    client.run_until_disconnected()
    print(time.asctime(), ' ', 'Stopped!')
