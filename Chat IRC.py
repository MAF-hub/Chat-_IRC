from colorama import Fore, init
import os
import time 
import socket
#program written by Meretec
name = input(Fore.BLUE + "<<<<<First, put your nickname: >>>>>> ")
print(Fore.RED + f"Hi {name}!")
print("Use [help] for a help")
join = input(Fore.GREEN + "<<<<Now, join a group: >>>>>> ")
if join == "Rules":
    print("Welcome to the group Rules!")
    rules = input("Are you sure you will follow the rules? (Yes or No)")
    if rules == "Yes":
        print("You must fulfill them!")
        print("General Rules") 
        print("1. Do not offend others")
        print("2. Be yourself")
        print("3. NO CP")
        print("4. Enjoy!")
    elif rules == "No":
        print("You will be removed from the program in 5 seconds")
        time.sleep(1)
        print("5")
        time.sleep(1)
        print("4")
        time.sleep(1)
        print("3")
        time.sleep(1)
        print("2")
        time.sleep(1)
        print("1")
        time.sleep(1)
        print("Taken from the program")
        print("Exiting now...")
    else:
        print(f"The command '{rules}' is not recognized")
        print("Exiting now...")
    
elif join == "commands":
    print("1. commands")
    print("2. Rules")  
    print("3. Join (-h for help)")
    print("4. Help")
    print("5. Back")
elif join == "Join":
    print("Use [Join -h] for more help")
    print("Doomers")
    print("MINECRAFT_LIVE")
    print("Tu Covid favorito")
    group = input("What group do you want to be in? ")
    if group == "Doomers":
        print("You're in the group of Doomers")
        print("Enjoy!")
    elif group == "Minecraft_LIVE":
        print("You're in the group of Minecraft LIVE")
        print("Enjoy!")
    elif group == "Tu Covid favorito":
        print("You're in the group of [Tu Covid favorito]")
        print("Enjoy!")
    else:
        print("Put the command well!")
elif join == "help":
    print("-h: It shows you help for each command.")
    print("Rules: It shows you the rules of a group, if that group does not have rules it will not tell you anything.")
    print("commands: Shows you the all commands for use, there are secret commands, sshhh.")
    print("Join: Use Join to join a group [Join -h] for more help.")
    print("Talk alone: You speak alone, while the program repeats what you have written")

elif join == "Talk alone":
    alone = input(f"<<<<<<Hello again {name}, This is a mini test of an IRC chat (not online): ")
    print(alone)
    alone1 = input("Put a text>>>>>")
    print(alone1)
    if alone1 == "s3cr3t":
        print("You have discovered a secret command! Use s3cr3t to know the ip address of a web")
        secret = input("Put the command [s3cr3t]: ")
        if secret == "s3cr3t":
            host=input("Ingresa el host > ")
            hostip=socket.gethostbyname(host)
            print("---------")
            print(hostip)
            print("----------")
        else:
            print("you must put the secret command right!")
    else:
        print("you must put the secret command right!")





    
else:
    print("Put the command well!!")


input()





              
    


