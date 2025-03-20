import os
import subprocess

def check_zphisher():
    """Check if Zphisher is already installed"""
    if os.path.exists("Zphisher"):
        print("[+] Zphisher is already installed.")
    else:
        print("[+] Cloning Zphisher...")
        subprocess.run(["git", "clone", "https://github.com/htr-tech/zphisher.git"], check=True)

def give_permissions():
    """Give execute permissions to zphisher.sh"""
    print("[+] Setting execute permissions...")
    subprocess.run(["chmod", "+777", "Zphisher/zphisher.sh"], check=True)

def run_zphisher():
    """Run Zphisher script"""
    print("[+] Running Zphisher...")
    subprocess.run(["bash", "Zphisher/zphisher.sh"], check=True)

if __name__ == "__main__":
    check_zphisher()
    give_permissions()
    run_zphisher()
