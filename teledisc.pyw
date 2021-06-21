  
from telethon import TelegramClient, events, sync, utils
from telethon.sessions import StringSession
import requests

def SendMessageToAlwaysWin(message):
    if '/USDT' in message:
        message= "<@&834911692303237172>\n" + message
    mUrl = "https://ptb.discord.com/api/webhooks/838079506660851762/7-lpGNlqWGGlO08XZJ3RwAvSXpWGDf5J6Z4ro5bsdtogYGGXovVfmYGmCb3Jvr1RvtWG"
    data = {"content": message}
    response = requests.post(mUrl, json=data)

def StartTelegramForwarding():
    api_id = 5747368
    api_hash = '19f6d3c9d8d4e6540bce79c3b9223fbe'
    stringsesh = '1BVtsOLYBu524ThiNeAkmK_bCr13hue-pxnoqIINLtYe4B6g7Rzq7uLtBfZv-3JDhl1R1JFdEhyjx6KAxFvOEaa1Mnlegji1hiIP5zW0qmWCrQsbVII47Zh3uul_oWPtCAKMCjlAmYcvmppnyRZMrizSH4G5hahXgLb6FuSvmP0RR7zLg6C7ZTYrQSonmLv0UTUOMHi9P6_0-9_VKlIhGwn8OEBLaiVl3Gjx4XbgtB8-gjz0k7L7dxkYpu4SQ7mNMi4rFZlz-XxQJPIlQ6CUwdy0v0K0qdLJ1bWmCesO0TlwPFntVKB1eSnDh8UhYDDlXVAqTTn4H3_4-HzcrPgRtBwsuEBZp4MQ='
    client = TelegramClient(StringSession(stringsesh), api_id, api_hash)
    
    @client.on(events.NewMessage()) 
    async def my_event_handler(event):
        sender = await event.get_sender()
        chat = await event.get_chat()
        sender_id = str(sender.id)
        channel_name = utils.get_display_name(sender)
        msg = "Channel name: " + channel_name + " | ID: " + sender_id
        if sender_id == "1375168387":
            #SendMessageToAlwaysWin(event.raw_text)
            pass
        elif chat.id == 1899129008:
            print("Robot Section ---")
            if str(event.raw_text) == '/stop':
              print('Exiting....')
              await client.disconnect()

    print("Starting telegram scraper")
    client.start()
    client.get_dialogs()
    client.run_until_disconnected()

StartTelegramForwarding()
