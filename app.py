import requests
import json
import sM


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
 add_token = open("logs.py","w+")
 add_token.write("Token = " + "\"" + pull_token + "\"")
 print("Your key was added. \n  First name: " + name + "\n  Username: " + username + "\n  ID: " + str(ID) )
 add_token.close
 r_chat_id = input("Please enter the chat ID: ")
 add_chat_id = open("logs.py","a")
 add_chat_id.write("\nchat_id = " + "\"" + r_chat_id + "\"")
 add_chat_id.close
 message = input("whats the message?: ")
 count = input("how many messages?: ")
 w_n = ""
 while w_n == "" or w_n == True:
  try:
   sM.is_num(count)
  except ValueError:
   w_n = True
   count = input("Please enter a number and try again: ")
  else:
   pass
   w_n = False
 if w_n == False:
  i = 0
 while i < int(count):
  sM.sendMessage(message)
  i=i + 1 
  print(i)
print("Done")
