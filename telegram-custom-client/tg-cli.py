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
        newname = '' + datetime.now().strftime("%H:%M")
        print(newname)
        time.sleep(1)
        await client(UpdateUsernameRequest(newname))
        print(newname)
        time.sleep(60)
    print(time.asctime(), ' ', 'Starting...')
    client.start(phone, password)
    client.run_until_disconnected()
    print(time.asctime(), ' ', 'Stopped!')
