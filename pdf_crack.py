import os
import subprocess

# Paths
pdf_path = "/path/to/your.pdf"  # Change to the actual PDF file path
hash_file = "/path/to/output_hash.txt"
output_file = "/path/to/cracked_password.txt"

def check_john_installed():
    """Check if John the Ripper is installed"""
    result = subprocess.run(["ls"], capture_output=True, text=True)
    if "john" in result.stdout:
        print("[+] John the Ripper is available.")
        return True
    else:
        print("[-] John the Ripper not found.")
        return False

def extract_pdf_hash():
    """Extract hash from PDF"""
    try:
        command = f"./pdf2john.pl {pdf_path} > {hash_file}"
        subprocess.run(command, shell=True, check=True)
        print("[+] Hash extracted successfully.")
    except subprocess.CalledProcessError:
        print("[-] Failed to extract hash.")

def crack_password():
    """Crack the PDF password"""
    try:
        command = f"john --format=pdf {hash_file}"
        subprocess.run(command, shell=True, check=True)
        print("[+] Cracking process started.")

        # Get the cracked password
        result = subprocess.run(["john", "--show", hash_file], capture_output=True, text=True)
        with open(output_file, "w") as file:
            file.write(result.stdout)

        print("[+] Password saved in:", output_file)
    except subprocess.CalledProcessError:
        print("[-] Failed to crack the password.")

if __name__ == "__main__":
    if check_john_installed():
        extract_pdf_hash()
        crack_password()
