import hashlib
from colorama import *
import secrets
import string
import os
import time

blue = Fore.BLUE
green = Fore.GREEN
red = Fore.RED
megenta = Fore.MAGENTA
yellow = Fore.LIGHTYELLOW_EX
reset = Fore.RESET
white = Fore.WHITE
lightcyan = Fore.LIGHTCYAN_EX

print(f"""
{lightcyan}
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
{Fore.LIGHTBLACK_EX}            OTHER FEATURES:
{megenta} 4: Password generator
{yellow} 5: Salter
{reset}
      made by blxsted
      """)


mode = int(input('Enter Mode: '))
if mode == 1:
    file_path = input(f'{blue} File Containing Passwords: ')
    with open('settings.txt', 'w') as settings:
        settings.write(file_path)

if mode == 2:
    setup = True
    
    hash_to_crack = input(f'{blue} Hash to crack: ')
    try:
        
    
        with open('settings.txt', 'r') as settings:
            file_path = settings.read()
        alg_choice = input(f"""
            {yellow}    1: SHA256
                {megenta} 2: MD5  
                {yellow} 3: SHA1
                {megenta} 4: SHA224
                {yellow} 5: SHA512
                {megenta} 6: SHA384 
                {reset}         
                        """)
        
        
                        

        def sha256_hash(line):
            line = line.strip()  
            if line:  
                hashed = hashlib.sha256(line.encode()).hexdigest()
                print(green, hashed, ':', line)
                if hashed == hash_to_crack:
                    print(f'{blue} PASSWORD FOUND: {line}')
                    exit('Reason for exit: found password')

        def sha1_hash(line):
            line = line.strip()  
            if line:  
                hashed = hashlib.sha1(line.encode()).hexdigest()
                print(green, hashed, ':', line)
                if hashed == hash_to_crack:
                    print(f'{blue} PASSWORD FOUND: {line}')
                    exit('Reason for exit: found password')

        def sha384_hash(line):
            line = line.strip()  
            if line:  
                hashed = hashlib.sha384(line.encode()).hexdigest()
                print(green, hashed, ':', line)
                if hashed == hash_to_crack:
                    print(f'{blue} PASSWORD FOUND: {line}')
                    exit('Reason for exit: found password')

        def sha512_hash(line):
            line = line.strip()  
            if line:  
                hashed = hashlib.sha512(line.encode()).hexdigest()
                print(green, hashed, ':', line)
                if hashed == hash_to_crack:
                    print(f'{blue} PASSWORD FOUND: {line}')
                    exit('Reason for exit: found password')

        def sha224_hash(line):
            line = line.strip()  
            if line:  
                hashed = hashlib.sha224(line.encode()).hexdigest()
                print(green, hashed, ':', line)
                if hashed == hash_to_crack:
                    print(f'{blue} PASSWORD FOUND: {line}')
                    exit('Reason for exit: found password')

        def MD5_hash(line):
            line = line.strip()  
            if line:  
                hashed = hashlib.md5(line.encode()).hexdigest()
                print(green, hashed, ':', line)
                if hashed == hash_to_crack:
                    print(f'{blue} PASSWORD FOUND: {line}')
                    exit('Reason for exit: found password')

        with open(file_path, 'r') as file:
            for line in file:
                if alg_choice == '1':
                    sha256_hash(line)
                if alg_choice == '2':
                    MD5_hash(line)
                if alg_choice == '3':
                    sha1_hash(line)
                if alg_choice == '4':
                    sha224_hash(line)
                if alg_choice == '5':
                    sha512_hash(line)
                if alg_choice == '6':
                    sha384_hash(line)
                
    except FileNotFoundError as e:
        print(f'{yellow}settings.txt not found. Please use setup or input 1 before running.', reset)
if mode == 3:
    print('Made by blxsted, use it to hack people idfc, just do not get caught')


if mode == 4:
    chars = string.ascii_letters + string.digits
    random_string = ''.join(secrets.choice(chars) for _ in range(15))
    print(random_string)

if mode == 5:
    chars = string.ascii_letters + string.digits
    salts = ''.join(secrets.choice(chars) for _ in range(15)); salts_other = ''.join(secrets.choice(chars) for _ in range(15))
    hash_input = input('Hash to salt: ')
    salted_hash = f'{salts}{hash_input}{salts_other}'
    print(salted_hash)


