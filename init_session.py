from telethon.sync import TelegramClient, events

import datetime
import socks
import time

proxy_server = ''
proxy_port = 2434
proxy_secret = 'secret'
proxy_dc_id = 2  # This is usually 2 for MTProto proxies

proxy = (
    socks.SOCKS5,
    proxy_server,
    proxy_port,
    True,
    'username',
    'password'
)


api_id = 'id'
api_hash = 'hash'

# Dictionary to track the times when senders were last replied to
reply_times = {}

async with TelegramClient('anon', api_id, api_hash) as client:

#to use proxy:
#async with TelegramClient('anon', api_id, api_hash, proxy=proxy) as client:  
    
    @client.on(events.NewMessage())
    async def my_event_handler(event):
        sender = await event.get_sender()
        sender_id = sender.id
        sender_name = sender.first_name
        chat = await event.get_chat()
        chat_id = chat.id
        text = event.raw_text

            # Personal message
        if chat_id == sender_id and not sender.bot:
             # Check the last reply to this sender
            last_reply_time = reply_times.get(str(sender_id), None)
            if last_reply_time is None or time.time() - last_reply_time > 60*60*6:  # reply only if not replied in the last 6 hours
                response = f'Hello <a href="tg://user?id={sender_id}">{sender_name}</a>,\n I received your message and will reply as soon as possible. Thank you for your understanding.'
                await client.send_message(chat_id, response, parse_mode='HTML')
                reply_times[str(sender_id)] = time.time()  # update the last reply time

            # Group message
        elif '@Your_Username' in text: #edit Your Username
            last_reply_time = reply_times.get(str(str(chat_id)+str(sender_id)), None)
            if last_reply_time is None or time.time() - last_reply_time > 60*5:
                response = f'Hello <a href="tg://user?id={sender_id}">{sender_name}</a> @ <a href="https://t.me/c/{chat_id}">{chat.title}</a>,\n I received your message and will reply as soon as possible. Thank you for your understanding.'
                await client.send_message(chat_id, response, parse_mode='HTML')
                reply_times[str(str(chat_id)+str(sender_id))] = time.time()

   
    await client.run_until_disconnected()
