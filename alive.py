import os, time

def loop():
    os.system("cls||clear")
    os.system("python3 alive.py||python alive.py")

try:
    import requests
except:
    print("\n Installing requests...\n\n")
    try:
        os.system("pip3 install requests")
    except:
        os.system("pip install requests")
    

def banner():
    print(" █████╗ ██╗     ██╗██╗   ██╗███████╗██████╗ ")
    print("██╔══██╗██║     ██║██║   ██║██╔════╝╚════██╗")
    print("███████║██║     ██║██║   ██║█████╗    ▄███╔╝")
    print("██╔══██║██║     ██║╚██╗ ██╔╝██╔══╝    ▀▀══╝ ")
    print("██║  ██║███████╗██║ ╚████╔╝ ███████╗  ██╗  ")
    print("╚═╝  ╚═╝╚══════╝╚═╝  ╚═══╝  ╚══════╝  ╚═╝ ")
    print("\n           Made by LunarStone292")

os.system("cls||clear")


banner()

print("\n\n Select the mode:")
print("\n\n    1. Loop")
print("\n    2. only check")
print("\n    3. exit")

scelta = int(input("\n\n Mode => "))

os.system("clear||cls")

banner()

if(scelta < 3):
    sito = input("\n Enter the URL: ")

if(scelta == 1):
    while(True):
        try:
            r = requests.get(sito)
            if(r.status_code == 200):
                print(" Host is alive")
            elif(r.status_code == 403):
                print(" Connection refused!")
            time.sleep(.5)
        except KeyboardInterrupt:
            exit()
        except:
            print(" Server seems down!!!")
            time.sleep(.5)
elif(scelta == 2):
    try:
        r = requests.get(sito)
        if(r.status_code == 200):
            print(" Host is alive")
        elif(r.status_code == 403):
            print(" Connection refused!")
        time.sleep(2)
    except:
        print(" Server seems down!!!")
elif(scelta == 3):
    exit()

loop()