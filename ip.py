import socket
from pyrogram import Client

def get_ip_address():
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    return ip_address

# Replace api_id, api_hash, bot_token and chat_id with your own values
api_id = "24254966"
api_hash = "ef0f6eb46def4eef272f26e1907fa736"
bot_token = "6044349131:AAEe2vJF5K5ehytiMP9i4aPVPQi_yX0Sg_8"
chat_id = "1345158291"

app = Client("my_account", api_id=api_id, api_hash=api_hash, bot_token=bot_token)

with app:
    ip_address = get_ip_address()
    message = f"My server's IP address is: {ip_address}"
    app.send_message(chat_id=chat_id, text=message)
