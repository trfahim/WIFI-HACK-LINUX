import os

def is_root():
    return os.geteuid() == 0

if is_root():
    print("\n[+] You are running as root\n")
    os.system("apt update")
    os.system("apt install subprocess")
    os.system("apt install pyfiglet")
    os.system("apt install colorama")
    os.system("apt install gnome-terminal")
    os.system("apt install random string")

else:
    print("\n[+] You are not running as root\n")
    os.system("sudo apt update")
    os.system("sudo apt install subprocess")
    os.system("sudo apt install pyfiglet")
    os.system("sudo apt install colorama")
    os.system("sudo apt install gnome-terminal")
    os.system("sudo apt install random string")

print("\nAll package install suceessful")
print("Happy Hacking !!\n")
os._exit(0)

