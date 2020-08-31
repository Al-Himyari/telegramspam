import requests
import logs
def sendMessage(message1):
 requests.get("https://api.telegram.org/bot" + logs.Token + "/sendMessage?chat_id=" + logs.chat_id + "&text=" + message1)

def is_num(num):
 isinstance(int(num), int)
