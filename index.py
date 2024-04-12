import hashlib
from colorama import *

blue = Fore.BLUE
green = Fore.GREEN
red = Fore.RED
reset = Fore.RESET
white = Fore.WHITE

print(f"""
{white}
 ______ __                  __      __  __                           
/\__  _/\ \                /\ \  __/\ \/\ \      __                  
\/_/\ \\ \ \___      __    \ \ \/\ \ \ \ \ \___ /\_\  _____          
   \ \ \\ \  _ `\  /'__`\   \ \ \ \ \ \ \ \  _ `\/\ \/\ '__`\        
    \ \ \\ \ \ \ \/\  __/    \ \ \_/ \_\ \ \ \ \ \ \ \ \ \L\ \       
     \ \_\\ \_\ \_\ \____\    \ `\___x___/\ \_\ \_\ \_\ \ ,__/       
      \/_/ \/_/\/_/\/____/     '\/__//__/  \/_/\/_/\/_/\ \ \/        
                                                        \ \_\        
                                                         \/_/        

{blue} 1: Setup
{green} 2: Run
{red} 3: Info  
{reset}
      made by blxsted
      """)

mode = int(input('Enter Mode: '))
if mode == 1:
    file_path = input(f'{blue} File Containing Passwords: ')
    with open('settings.txt', 'w') as settings:
        settings.write(file_path)

if mode == 2:
    hash_to_crack = input(f'{blue} Hash to crack: ')
    with open('settings.txt', 'r') as settings:
        file_path = settings.read()
    def sha256_hash(line):
        line = line.strip()  
        if line:  
            hashed = hashlib.sha256(line.encode()).hexdigest()
            print(green, hashed, ':', line)
            if hashed == hash_to_crack:
                print(f'{blue} PASSWORD FOUND: {line}')
                exit('Reason for exit: found password')

    with open(file_path, 'r') as file:
        for line in file:
            sha256_hash(line)
if mode == 3:
    print('Made by blxsted, use it to hack people idfc, just do not get caught')

# feel free to fork this just give credit