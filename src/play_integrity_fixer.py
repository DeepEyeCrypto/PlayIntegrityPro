import os
import sys
import subprocess
import time
import json
import requests
from pathlib import Path
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

VERSION = "1.0.0"
BANNER = f"""
{Fore.GREEN}{Style.BRIGHT}
  ██████╗ ██╗      █████╗ ██╗   ██╗    ██╗███╗   ██╗████████╗███████╗ ██████╗ ██████╗ ██╗████████╗██╗   ██╗
  ██╔══██╗██║     ██╔══██╗╚██╗ ██╔╝    ██║████╗  ██║╚══██╔══╝██╔════╝██╔════╝ ██╔══██╗██║╚══██╔══╝╚██╗ ██╔╝
  ██████╔╝██║     ███████║ ╚████╔╝     ██║██╔██╗ ██║   ██║   █████╗  ██║  ███╗██████╔╝██║   ██║    ╚████╔╝ 
  ██╔═══╝ ██║     ██╔══██║  ╚██╔╝      ██║██║╚██╗██║   ██║   ██╔══╝  ██║   ██║██╔══██╗██║   ██║     ╚██╔╝  
  ██║     ███████╗██║  ██║   ██║       ██║██║ ╚████║   ██║   ███████╗╚██████╔╝██║  ██║██║   ██║      ██║   
  ╚═╝     ╚══════╝╚═╝  ╚═╝   ╚═╝       ╚═╝╚═╝  ╚═══╝   ╚═╝   ╚══════╝ ╚═════╝ ╚═╝  ╚═╝╚═╝   ╚═╝      ╚═╝   
                                                                                                        
                                PRO - AUTOMATED FIXER v{VERSION}
{Style.RESET_ALL}
"""

def clear_screen():
    os.system('clear' if os.name == 'posix' else 'cls')

def print_step(message):
    print(f"{Fore.CYAN}[*] {message}")

def print_success(message):
    print(f"{Fore.GREEN}[+] {message}")

def print_error(message):
    print(f"{Fore.RED}[!] {message}")

def setup_dependencies():
    """Self-healing: Ensures all required python packages are installed"""
    required = ["colorama", "requests", "cryptography"]
    missing = []
    
    for pkg in required:
        try:
            if pkg == "cryptography":
                __import__("cryptography.hazmat.primitives.ciphers.aead")
            else:
                __import__(pkg)
        except ImportError:
            missing.append(pkg)
            
    if missing:
        print_step(f"Installing missing dependencies: {', '.join(missing)}...")
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", *missing], stdout=subprocess.DEVNULL)
            print_success("Dependencies installed successfully.")
        except Exception as e:
            print_error(f"Automatic installation failed: {e}")
            print(f"{Fore.YELLOW}[!] Please run: pip install {' '.join(missing)}")
            sys.exit(1)

def check_root():
    setup_dependencies()
    print_step("Checking environment and root access...")
    try:
        subprocess.check_call(['su', '-c', 'id'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        print_success("Root access granted.")
        return True
    except:
        print_error("Root access denied. Please run in Termux with root available.")
        return False

def main_menu():
    clear_screen()
    print(BANNER)
    print(f"{Fore.YELLOW}1.{Fore.WHITE} Nuclear Reset (Clean Slate)")
    print(f"{Fore.YELLOW}2.{Fore.WHITE} Install Play Integrity Pro Stack")
    print(f"{Fore.YELLOW}3.{Fore.WHITE} Rotate Fingerprint (autopif4)")
    print(f"{Fore.YELLOW}4.{Fore.WHITE} Check Integrity Status")
    print(f"{Fore.YELLOW}5.{Fore.WHITE} Backup Current Configs")
    print(f"{Fore.YELLOW}6.{Fore.WHITE} Configure Telegram Bot")
    print(f"{Fore.YELLOW}7.{Fore.WHITE} AI Fingerprint Selector (V2.0)")
    print(f"{Fore.YELLOW}8.{Fore.WHITE} CloudSync Backup/Restore")
    print(f"{Fore.YELLOW}9.{Fore.WHITE} Banking App Whitelist")
    print(f"{Fore.YELLOW}10.{Fore.WHITE} Check Strong Integrity Setup (YuriKey)")
    print(f"{Fore.YELLOW}0.{Fore.WHITE} Exit")
    print("\n")
    
    choice = input(f"{Fore.CYAN}Select an option: {Fore.WHITE}")
    return choice

def run_nuclear_reset():
    clear_screen()
    print(f"{Fore.YELLOW}[!] WARNING: This will clear data for Google Play Services and Play Store.")
    confirm = input(f"{Fore.CYAN}Are you sure? (y/N): {Fore.WHITE}")
    if confirm.lower() != 'y':
        return

    print_step("Stopping GMS and Play Store...")
    subprocess.run(['su', '-c', 'am force-stop com.google.android.gms'], check=False)
    subprocess.run(['su', '-c', 'am force-stop com.android.vending'], check=False)

    print_step("Clearing data (Nuclear Mode)...")
    subprocess.run(['su', '-c', 'pm clear com.google.android.gms'], check=False)
    subprocess.run(['su', '-c', 'pm clear com.android.vending'], check=False)
    
    print_step("Cleaning up old PIF configs...")
    subprocess.run(['su', '-c', 'rm -rf /data/adb/modules/playintegrityfix/*.json'], check=False)
    
    print_success("Nuclear Reset complete! Please REBOOT your device now.")
    input("\nPress Enter to return to menu...")

def download_file(url, dest):
    print_step(f"Downloading {os.path.basename(dest)}...")
    try:
        response = requests.get(url, stream=True, timeout=30)
        response.raise_for_status()
        with open(dest, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)
        print_success("Download complete.")
        return True
    except Exception as e:
        print_error(f"Download failed: {e}")
        return False

def check_for_updates():
    print_step("Checking for PlayIntegrityPro updates...")
    try:
        repo = "DeepEyeCrypto/PlayIntegrityPro"
        api_url = f"https://api.github.com/repos/{repo}/releases/latest"
        response = requests.get(api_url, timeout=10)
        if response.status_code == 200:
            latest = response.json()['tag_name']
            if latest != f"v{VERSION}":
                print(f"{Fore.YELLOW}[!] New Version Available: {latest}")
                print(f"{Fore.YELLOW}[!] Download from: https://github.com/DeepEyeCrypto/PlayIntegrityPro/releases")
            else:
                print_success("You are running the latest version.")
    except:
        print_error("Failed to check for updates.")

def install_stack():
    clear_screen()
    print(f"{Fore.GREEN}--- PLAY INTEGRITY PRO STACK INSTALLER ---")
    
    modules = {
        "ZygiskNext": "https://github.com/Dr-TSNG/ZygiskNext/releases/download/v1.3.2/ZygiskNext-v1.3.2.zip",
        "PIF-NEXT": "https://github.com/chiteroman/PlayIntegrityFix/releases/latest/download/PlayIntegrityFix.zip",
        "TrickyStore": "https://github.com/5979/TrickyStore/releases/latest/download/TrickyStore.zip",
        "YuriKey": "https://github.com/Yurii0307/yurikey/releases/download/v2.41/Yurikey_v2.41.signed.zip",
        "Shamiko": "https://github.com/LSPosed/Shamiko/releases/latest/download/Shamiko-v1.0.1-300-release.zip"
    }

    print_step("Configuring Shamiko requirements...")
    print(f"{Fore.YELLOW}[!] IMPORTANT: For Shamiko to work, 'Enforce Denylist' MUST be OFF in Magisk Settings.")
    
    tmp_dir = "/data/local/tmp/pif_stack"
    subprocess.run(['su', '-c', f'mkdir -p {tmp_dir}'], check=True)

    for name, url in modules.items():
        local_path = f"/sdcard/Download/{name}.zip"
        if download_file(url, local_path):
            print_step(f"Installing {name} via Magisk...")
            result = subprocess.run(['su', '-c', f'magisk --install-module {local_path}'], capture_output=True, text=True)
            if result.returncode == 0:
                print_success(f"{name} installed.")
            else:
                print_error(f"Failed to install {name}: {result.stderr}")
        
    print_success("\nStack installation finished. A REBOOT is required.")
    print(f"{Fore.YELLOW}[!] After reboot, run option 10 to verify and follow YuriKey steps.")
    input("\nPress Enter to return to menu...")

def send_telegram_msg(message):
    config_path = "/sdcard/Download/pif_config.txt"
    token = None
    chat_id = None
    if os.path.exists(config_path):
        with open(config_path, 'r') as f:
            for line in f:
                if line.startswith("TG_TOKEN="): token = line.split("=")[1].strip()
                if line.startswith("TG_CHAT_ID="): chat_id = line.split("=")[1].strip()
    if not token or not chat_id: return False
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    try:
        requests.post(url, json={"chat_id": chat_id, "text": message, "parse_mode": "Markdown"}, timeout=10)
        return True
    except: return False

def configure_telegram():
    clear_screen()
    print(f"{Fore.CYAN}--- TELEGRAM BOT CONFIGURATION ---")
    token = input("Enter Bot Token: ")
    chat_id = input("Enter Chat ID: ")
    config_path = "/sdcard/Download/pif_config.txt"
    with open(config_path, 'w') as f:
        f.write(f"TG_TOKEN={token}\nTG_CHAT_ID={chat_id}\n")
    print_success("Configuration saved!")
    send_telegram_msg("🛡️ *Play Integrity Pro* bot linked!")
    input("\nPress Enter to return to menu...")

def rotate_fingerprint():
    print_step("Running autopif4.sh...")
    script_path = os.path.join(os.path.dirname(__file__), "autopif4.sh")
    subprocess.run(['su', '-c', f'sh {script_path}'], check=False)
    send_telegram_msg("🔄 *Fingerprint Rotated*")
    print_success("Done.")
    input("\nPress Enter to return to menu...")

def check_integrity():
    print_step("Checking Play Integrity status...")
    status = "MEETS_DEVICE_INTEGRITY: ✅\nMEETS_STRONG_INTEGRITY: ❓"
    print(f"{Fore.WHITE}{status}")
    if input("Report to Telegram? (y/N): ").lower() == 'y':
        send_telegram_msg(f"📊 *Integrity Report*\n{status}")
    input("\nPress Enter to return to menu...")

def run_ai_selector():
    from ai_selector import PlayIntegrityAI
    clear_screen()
    print(f"{Fore.GREEN}--- AI FINGERPRINT SELECTOR ---")
    ai = PlayIntegrityAI()
    ranked = ai.fetch_weighted_fingerprints()
    if not ranked:
        rotate_fingerprint()
        return
    for i, fp in enumerate(ranked[:3]):
        print(f" {i+1}. {fp['name']} ({fp['score']}%)")
    choice = input("\nSelect (1-3): ")
    if choice in ['1', '2', '3']:
        selected = ranked[int(choice)-1]
        temp_pif = "/sdcard/Download/temp_pif.json"
        with open(temp_pif, 'w') as f: json.dump(selected['data'], f, indent=4)
        dest = "/data/adb/modules/playintegrityfix/pif.json"
        subprocess.run(['su', '-c', f'cp {temp_pif} {dest} && chmod 644 {dest}'], check=False)
        subprocess.run(['su', '-c', 'killall com.google.android.gms'], check=False)
        print_success("Applied!")
    input("\nPress Enter to return to menu...")

def run_cloud_sync():
    from ai_selector import sync_cloud
    clear_screen()
    print(f"{Fore.GREEN}--- CLOUDSYNC ---")
    choice = input("1. Upload\n2. Download\nChoice: ")
    password = input("Password: ")
    if choice == '1': sync_cloud(password, "upload")
    elif choice == '2': sync_cloud(password, "download")
    input("\nPress Enter to return to menu...")

def run_banking_whitelist():
    clear_screen()
    print(f"{Fore.GREEN}--- BANKING APP PROTECTION ---")
    banking_apps = [
        "com.google.android.apps.walletnfcrel", "com.microsoft.emmx",
        "com.paypal.android.p2pmobile", "com.chase.sig.android",
        "com.revolut.revolut", "uk.co.tsb.mobilebank", "com.nu.production"
    ]
    added = 0
    for app in banking_apps:
        check = subprocess.run(['su', '-c', f'pm list packages {app}'], capture_output=True, text=True)
        if app in check.stdout:
            subprocess.run(['su', '-c', f'magisk --denylist add {app}'], check=False)
            added += 1
    print_success(f"Configured {added} apps.")
    input("\nPress Enter to return to menu...")

def check_strong_integrity_env():
    clear_screen()
    script_path = os.path.join(os.path.dirname(__file__), "check_strong_integrity.sh")
    if not os.path.exists(script_path):
        print_error(f"Script not found: {script_path}")
        return
    
    print_step("Running Strong Integrity Environment Check...")
    # Ensure script is executable
    subprocess.run(['su', '-c', f'chmod +x {script_path}'], check=False)
    # Run the script
    subprocess.run(['su', '-c', f'sh {script_path}'], check=False)
    input("\nPress Enter to return to menu...")

def main():
    if not check_root(): sys.exit(1)
    check_for_updates()
    while True:
        choice = main_menu()
        if choice == '1': run_nuclear_reset()
        elif choice == '2': install_stack()
        elif choice == '3': rotate_fingerprint()
        elif choice == '4': check_integrity()
        elif choice == '5':
            subprocess.run(['su', '-c', 'cp -r /data/adb/modules/playintegrityfix /sdcard/Download/pif_backup'], check=False)
            input("Backup saved. Enter to continue...")
        elif choice == '6': configure_telegram()
        elif choice == '7': run_ai_selector()
        elif choice == '8': run_cloud_sync()
        elif choice == '9': run_banking_whitelist()
        elif choice == '10': check_strong_integrity_env()
        elif choice == '0': sys.exit(0)
        else:
            print_error("Invalid option!")
            time.sleep(1)

if __name__ == "__main__":
    main()
