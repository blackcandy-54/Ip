import socket

def get_ip_address():
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    return ip_address

# Telegram Bot code to send the IP address to a chat
import telegram

bot_token = '6044349131:AAEe2vJF5K5ehytiMP9i4aPVPQi_yX0Sg_8'
chat_id = '1345158291'

bot = telegram.Bot(token=bot_token)
ip_address = get_ip_address()

message = f"My server's IP address is: {ip_address}"
bot.send_message(chat_id=chat_id, text=message)
