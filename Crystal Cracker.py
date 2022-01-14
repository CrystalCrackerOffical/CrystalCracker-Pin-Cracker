import requests
import re
import string
import time
import os

pingEveryone = True
print('')
print('Enter your cookie below:')
cookie = input()
os.system("cls")
print('')
print('Enter your webhook below:')
webhook = input()
os.system("cls")
print('')
print('Should we ping Everyone?: ( y / n )')
pingEveryone = input()
os.system("cls")
if pingEveryone.lower == 'y' or pingEveryone == 'yes':
    ping = '@everyone'
else:
    ping = '***Pin Cracked!***'
os.system("cls")

print('')


   _____                _        _  _____                _             
  / ____|              | |      | |/ ____|              | |            
 | |     _ __ _   _ ___| |_ __ _| | |     _ __ __ _  ___| | _____ _ __ 
 | |    | '__| | | / __| __/ _` | | |    | '__/ _` |/ __| |/ / _ \ '__|
 | |____| |  | |_| \__ \ || (_| | | |____| | | (_| | (__|   <  __/ |   
  \_____|_|   \__, |___/\__\__,_|_|\_____|_|  \__,_|\___|_|\_\___|_|   
               __/ |                                                   
              |___/                                                    
