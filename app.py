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
check_token = requests.get("https://api.sMgram.org/bot" + pull_token + "/getMe") 
dictionary_getMe_token = (json.loads(check_token.text))
is_ok = dictionary_getMe_token["ok"]

if is_ok == False:
 print("False key, try again"),
else:
 name = dictionary_getMe_token["result"]["first_name"]
 username = dictionary_getMe_token["result"]["username"]
 ID = dictionary_getMe_token["result"]["id"]
 add_token = open("logs.py","w+")
 add_token.write("Token = " + "\"" + pull_token + "\"")
 print("Your key was added. \n  First name: " + name + "\n  Username: " + username + "\n  ID: " + str(ID) )
 add_token.close
if is_ok == True:
 r_chat_id = input("Please enter the chat ID: ")
 add_chat_id = open("logs.py","a")
 add_chat_id.write("\nchat_id = " + "\"" + r_chat_id + "\"")
 add_chat_id.close
 message = input("whats the message?: ")
 count = input("how many messages?: ")
 i = 0
 while i < int(count):
  sM.sendMessage(message)
  i+=1 
  print(i)
 print("Done")
