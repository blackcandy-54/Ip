import socket

def get_ip_address():
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    return ip_address

# Telegram Bot code to send the IP address to a chat
import telegram

bot_token = ''
chat_id = ''

bot = telegram.Bot(token=bot_token)
ip_address = get_ip_address()

message = f"My server's IP address is: {ip_address}"
bot.send_message(chat_id=chat_id, text=message)
