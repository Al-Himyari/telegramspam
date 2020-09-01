import requests
import json


def sendMessage(message1):
 requests.get("https://api.telegram.org/bot" + Token + "/sendMessage?chat_id=" + chat_id + "&text=" + message1)

def is_num(num):
 isinstance(int(num), int)
 
Token = ""
chat_id = ""
intro = """
       
     S___S
    S     S
   S       S
  S         S
 S___________S
"""
print(intro)            
pull_token = input("Please type the bot token: ")
check_token = requests.get("https://api.telegram.org/bot" + pull_token + "/getMe") 
dictionary_getMe_token = (json.loads(check_token.text))
is_ok = dictionary_getMe_token["ok"]
count = ""

while is_ok == False:
 pull_token = input("Wrong token, try again: ")
 check_token = requests.get("https://api.telegram.org/bot" + pull_token + "/getMe")
 dictionary_getMe_token = (json.loads(check_token.text))
 is_ok = dictionary_getMe_token["ok"]
if is_ok == True:
 name = dictionary_getMe_token["result"]["first_name"]
 username = dictionary_getMe_token["result"]["username"]
 ID = dictionary_getMe_token["result"]["id"]
 Token = pull_token
 r_chat_id = input("Please enter the chat ID: ")
 chat_id = r_chat_id
 pass
 message = input("whats the message?: ")
 count = input("how many messages?: ")
 w_n = ""
 while w_n == "" or w_n == True:
  try:
   is_num(count)
  except ValueError:
   w_n = True
   count = input("not accepted, try again: ")
  else:
   pass
   w_n = False
 if w_n == False:
  i = 0
 while i < int(count):
  sendMessage(message)
  i=i + 1 
  print(i)
print("Done")
