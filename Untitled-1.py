import time
from colorama import *
print("_____|Rock-Paper-Scissors|____")
list=["Rock","Paper","Scissors","Shoot !!"]
print(Fore.RED+list[0])
time.sleep(1)
print(Fore.LIGHTRED_EX+list[1])
time.sleep(1)    
print(Fore.YELLOW+list[2])
time.sleep(1)        
print(Fore.GREEN+list[3])
time.sleep(2)
#Player1 input
x=input(Fore.BLUE+'Player1: ')
while(not(x in ["rock","paper","scissors"])):
        x=input('Player1: ')
print('\n\n\n\n\n\n\n\n')
#Player2 input
y=input(Fore.RED+'Player2: ')
while(not(x in ["rock","paper","scissors"])):
        y=input('Player2: ')
print('\n\n\n\n\n\n\n\n')
#result
if x==y:
    print(Fore.GREEN+"It's a Tie !!")
if x=='rock' and y=='paper':
    print(Fore.RED+"Paper covers rock!,Player 2 Won !!") 
if x=='rock' and y=='scissors':
    print(Fore.BLUE+"Rock smashes scissors!,Player 1 Won !!") 
if x=='paper' and y=='rock':
    print(Fore.BLUE+"Paper covers rock!,Player 1 Won !!") 
if x=='paper' and y=='scissors':
    print(Fore.RED+"Scissors cuts paper!,Player 2 Won !!") 
if x=='scissors' and y=='rock':
    print(Fore.RED+"Rock smashes scissors!,Player 2 Won !!") 
if x=='scissors' and y=='paper':
    print(Fore.BLUE+"Scissors cuts paper!,Player 1 Won !!")          