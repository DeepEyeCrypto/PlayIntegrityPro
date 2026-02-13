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

VERSION = "1.3.1"
BANNER = f"""
{Fore.CYAN}{Style.BRIGHT}
    ____  __              ____       __                       _ __         ____                 
   / __ \/ /___ ___  __  /  _/___  / /____  ____ __________  (_) /___  __/ __ \_________  ____ 
  / /_/ / / __ `/ / / /  / // __ \/ __/ _ \/ __ `/ ___/ _ \/ / __/ / / / /_/ / ___/ __ \/ __ \\
 / ____/ / /_/ / /_/ / _/ // / / / /_/  __/ /_/ / /  /  __/ / /_/ /_/ / ____/ /  / /_/ / /_/ /
/_/   /_/\__,_/\__, / /___/_/ /_/\__/\___/\__, /_/   \___/_/\__/\__, /_/   /_/   \____/\____/ 
              /____/                     /____/                /____/                          
                                 {Fore.GREEN}PRO - NEXT-GEN INTEGRITY SUITE v{VERSION}
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
    print(f"{Fore.YELLOW}11.{Fore.WHITE} Strong Integrity Feasibility Report")
    print(f"{Fore.YELLOW}12.{Fore.WHITE} Live Attestation Watcher (logcat)")
    print(f"{Fore.YELLOW}13.{Fore.WHITE} View Module Logs (pip.log)")
    print(f"{Fore.YELLOW}14.{Fore.WHITE} Self-Dump Device (pif.json)")
    print(f"{Fore.YELLOW}15.{Fore.WHITE} Auto-Repair Strong Integrity")
    print(f"{Fore.YELLOW}16.{Fore.WHITE} Precision Patch Balancer (pif.json)")
    print(f"{Fore.YELLOW}17.{Fore.WHITE} Module Health Dashboard")
    print(f"{Fore.YELLOW}18.{Fore.WHITE} Security Shield Audit (Deep Scan)")
    print(f"{Fore.YELLOW}19.{Fore.WHITE} Enforce Stealth Mode (Hardened Props)")
    print(f"{Fore.YELLOW}20.{Fore.WHITE} Fingerprint Quality Deep-Dive")
    print(f"{Fore.YELLOW}21.{Fore.WHITE} Banking App Stealth Tester")
    print(f"{Fore.YELLOW}22.{Fore.WHITE} Export Working Stack (ZIP)")
    print(f"{Fore.YELLOW}23.{Fore.WHITE} Search Community Fingerprints")
    print(f"{Fore.YELLOW}24.{Fore.WHITE} Check for Script Updates")
    print(f"{Fore.YELLOW}25.{Fore.WHITE} AI Integrity Guard (Auto-Heal)")
    print(f"{Fore.YELLOW}26.{Fore.WHITE} Security Presets (Casual/Gamer/Elite)")
    print(f"{Fore.YELLOW}27.{Fore.WHITE} Deep System Integrity Audit")
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
                if input(f"{Fore.CYAN}Download and update this script now? (y/N): ").lower() == 'y':
                    print_step("Updating script...")
                    raw_url = f"https://raw.githubusercontent.com/{repo}/main/src/play_integrity_fixer.py"
                    new_content = requests.get(raw_url).text
                    if "VERSION =" in new_content:
                        with open(__file__, 'w') as f:
                            f.write(new_content)
                        print_success("Update applied! Please restart the script.")
                        sys.exit(0)
            else:
                print_success("You are running the latest version.")
    except Exception as e:
        print_error(f"Failed to check for updates: {e}")

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

    print_step("Pre-installation Audit...")
    conflicts = ["playintegrityfix", "safetynet-fix", "pif-next", "play-integrity-fork"]
    found_conflicts = []
    for c in conflicts:
        if os.path.exists(f"/data/adb/modules/{c}"):
            found_conflicts.append(c)
    
    if found_conflicts:
        print(f"{Fore.YELLOW}[!] Detected conflicting modules: {', '.join(found_conflicts)}")
        print(f"{Fore.YELLOW}[!] It is HIGHLY RECOMMENDED to remove them before proceeding.")
        if input("Automatically uninstall conflicts? (y/N): ").lower() == 'y':
            for c in found_conflicts:
                subprocess.run(['su', '-c', f'rm -rf /data/adb/modules/{c}'], check=False)
            print_success("Conflicts marked for removal (reboot required, but we will continue).")

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
    clear_screen()
    print(f"{Fore.CYAN}--- DEEPEYE INTEGRITY DIAGNOSTIC ---")
    
    # Check Fingerprint Match
    print_step("Verifying Fingerprint Injection...")
    current_fp = subprocess.run(['getprop', 'ro.build.fingerprint'], capture_output=True, text=True).stdout.strip()
    
    pif_json_path = "/data/adb/modules/playintegrityfix/pif.json"
    configured_fp = "Not Configured"
    if os.path.exists(pif_json_path):
        try:
            with open(pif_json_path, 'r') as f:
                data = json.load(f)
                configured_fp = data.get("FINGERPRINT", "Unknown")
        except: pass

    print(f" {Fore.WHITE}System FP: {current_fp}")
    print(f" {Fore.WHITE}Config FP: {configured_fp}")
    
    if current_fp == configured_fp:
        print_success("Fingerprint injection is ACTIVE.")
    else:
        print_error("Fingerprint mismatch! Injection may be failing.")

    # Check Strong Integrity Hooks
    print_step("Checking Strong Integrity hooks...")
    ts_active = os.path.exists("/data/adb/modules/trickystore")
    kb_active = os.path.exists("/data/adb/tricky/keybox.xml")
    
    print(f" {Fore.WHITE}TrickyStore: {'✅' if ts_active else '❌'}")
    print(f" {Fore.WHITE}Keybox.xml: {'✅' if kb_active else '❌'}")
    
    if ts_active and kb_active:
        print_success("Strong Integrity layer is PRIMED.")
    else:
        print_error("Strong Integrity layer is INCOMPLETE.")

    status = f"FP Match: {'✅' if current_fp == configured_fp else '❌'}\nStrong Primed: {'✅' if (ts_active and kb_active) else '❌'}"
    if input("\nReport status to Telegram? (y/N): ").lower() == 'y':
        send_telegram_msg(f"📊 *Integrity Diagnostic*\n{status}")
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
    
    # Check for YuriKey Action script
    yuri_action = "/data/adb/modules/yurikey/action.sh"
    check_yuri = subprocess.run(['su', '-c', f'[ -f {yuri_action} ] && echo "found"'], capture_output=True, text=True)
    
    if "found" in check_yuri.stdout:
        print(f"\n{Fore.GREEN}[+] YuriKey Action Script detected!")
        if input(f"{Fore.CYAN}Would you like to trigger YuriKey Keybox Refresh? (y/N): ").lower() == 'y':
            print_step("Triggering YuriKey Action...")
            subprocess.run(['su', '-c', f'sh {yuri_action}'], check=False)
            print_success("YuriKey Action execution finished.")
            print(f"{Fore.YELLOW}[!] Remember to REBOOT after a Keybox update.")
    
    input("\nPress Enter to return to menu...")

def run_feasibility_report():
    from feasibility_analyzer import StrongIntegrityAnalyzer
    clear_screen()
    analyzer = StrongIntegrityAnalyzer()
    analyzer.analyze()
    input("\nPress Enter to return to menu...")

def run_live_watcher():
    clear_screen()
    print(f"{Fore.CYAN}--- LIVE ATTESTATION WATCHER ---")
    print(f"{Fore.YELLOW}[!] Press Ctrl+C to stop watching and return to menu.\n")
    # Filters for TrickyStore and GMS attestation events
    filters = [
        "TrickyStore:*",
        "DroidGuard:*",
        "GMS_Integrity:*",
        "PlayIntegrityPro:*",
        "*:S"  # Silence everything else
    ]
    try:
        subprocess.run(['su', '-c', f'logcat -v time {" ".join(filters)}'])
    except KeyboardInterrupt:
        print("\n\nWatcher stopped.")
    input("\nPress Enter to return to menu...")

def view_module_logs():
    clear_screen()
    print(f"{Fore.CYAN}--- MODULE SERVICE LOGS ---")
    log_path = "/data/local/tmp/pip.log"
    try:
        result = subprocess.run(['su', '-c', f'tail -n 50 {log_path}'], capture_output=True, text=True)
        if result.stdout:
            print(f"{Fore.WHITE}{result.stdout}")
        else:
            print(f"{Fore.YELLOW}Logs are empty or not found at {log_path}")
    except Exception as e:
        print_error(f"Failed to read logs: {e}")
    input("\nPress Enter to return to menu...")

def run_self_dump():
    from ai_selector import PlayIntegrityAI
    clear_screen()
    print(f"{Fore.GREEN}--- SELF-DUMP ENGINE ---")
    ai = PlayIntegrityAI()
    data = ai.dump_local_fingerprint()
    
    save_path = "/sdcard/Download/my_device_pif.json"
    with open(save_path, 'w') as f:
        json.dump(data, f, indent=4)
    
    print_success(f"Device fingerprint dumped to {save_path}")
    print(f"{Fore.YELLOW}[!] You can use this file as a temporary backup if your main PIF fails.")
    input("\nPress Enter to return to menu...")

def run_auto_repair():
    from feasibility_analyzer import StrongIntegrityAnalyzer
    clear_screen()
    print(f"{Fore.GREEN}--- AUTO-REPAIR ENGINE ---")
    
    print_step("Analyzing environment...")
    # Surgical Cleanup
    print_step("Clearing corrupted GMS attestation caches...")
    commands = [
        'rm -rf /data/user/0/com.google.android.gms/cache/droidguard*',
        'rm -rf /data/user/0/com.google.android.gms/app_dg_cache/*',
        'rm -rf /data/user/0/com.android.vending/cache/*'
    ]
    for cmd in commands:
        subprocess.run(['su', '-c', cmd], check=False)
    
    # Check TrickyStore
    if not (os.path.exists("/data/adb/modules/trickystore") or os.path.exists("/data/adb/modules/TrickyStore")):
        print(f"{Fore.YELLOW}[!] TrickyStore module is missing. Mandatory for STRONG.")
        if input("Install TrickyStore now? (y/N): ").lower() == 'y':
            install_stack()
            
    # Check Keybox
    if not any(os.path.exists(p) for p in ["/data/adb/tricky/keybox.xml", "/data/adb/modules/trickystore/keybox.xml"]):
        print(f"{Fore.YELLOW}[!] keybox.xml is missing. Cannot pass STRONG.")
        if input("Try to fetch keybox via YuriKey Action? (y/N): ").lower() == 'y':
            check_strong_integrity_env()
            
    print_success("Repair cycle finished. A REBOOT is highly recommended.")
    input("\nPress Enter to return to menu...")

def run_patch_balancer():
    clear_screen()
    print(f"{Fore.CYAN}--- PRECISION PATCH BALANCER ---")
    pif_path = "/data/adb/modules/playintegrityfix/pif.json"
    if not os.path.exists(pif_path):
        print_error("pif.json not found. Run Option 7 or 14 first.")
        input("\nPress Enter to return to menu...")
        return
    
    current_patch = subprocess.run(['getprop', 'ro.build.version.security_patch'], capture_output=True, text=True).stdout.strip()
    print(f"[*] Current System Patch: {current_patch}")
    
    try:
        with open(pif_path, 'r') as f:
            data = json.load(f)
    except Exception as e:
        print_error(f"Failed to load pif.json: {e}")
        input("\nPress Enter to return to menu...")
        return
    
    pif_patch = data.get("SECURITY_PATCH", "Unknown")
    print(f"[*] Current pif.json Patch: {pif_patch}")
    
    print("\n[?] High-Integrity Keyboxes often require a specific patch date.")
    new_patch = input(f"Enter new patch date (YYYY-MM-DD or 'sync' for system) [{current_patch}]: ") or "sync"
    
    if new_patch == "sync":
        data["SECURITY_PATCH"] = current_patch
    else:
        data["SECURITY_PATCH"] = new_patch
        
    try:
        with open(pif_path, 'w') as f:
            json.dump(data, f, indent=4)
        print_success(f"pif.json updated to {data['SECURITY_PATCH']}.")
    except Exception as e:
        print_error(f"Failed to save pif.json: {e}")
    
    print(f"{Fore.YELLOW}[!] Remember to clear GMS cache (Option 15) after patching.")
    input("\nPress Enter to return to menu...")

def run_health_dashboard():
    clear_screen()
    print(f"{Fore.CYAN}{Style.BRIGHT}--- MODULE HEALTH DASHBOARD ---")
    
    # 1. Zygisk Status
    zygisk = subprocess.run(['su', '-c', 'resetprop ro.zygisk'], capture_output=True, text=True).stdout.strip()
    print(f"{Fore.WHITE}Zygisk Status: {'✅ Enabled' if zygisk == '1' else '❌ Disabled'}")
    
    # 2. Denylist Status
    denylist = subprocess.run(['su', '-c', 'magisk --denylist status'], capture_output=True, text=True).stdout.strip()
    print(f"{Fore.WHITE}Magisk Denylist: {denylist if denylist else 'Unknown (Check Magisk Settings)'}")
    
    # 3. Module Audit
    print_step("Auditing critical modules...")
    critical = ["playintegrityfix", "trickystore", "yurikey", "Shamiko", "ZygiskNext"]
    for mod in critical:
        path = f"/data/adb/modules/{mod}"
        status = f"{Fore.RED}Missing"
        if os.path.exists(path):
            if os.path.exists(f"{path}/disable"):
                status = f"{Fore.YELLOW}Disabled"
            else:
                status = f"{Fore.GREEN}Active"
        print(f"  - {mod.ljust(15)}: {status}")
        
    input("\nPress Enter to return to menu...")

def run_security_audit():
    clear_screen()
    print(f"{Fore.RED}{Style.BRIGHT}--- SECURITY SHIELD AUDIT (Deep Scan) ---")
    
    unsafe_props = {
        "ro.debuggable": "1",
        "ro.secure": "0",
        "ro.boot.flash.locked": "0",
        "ro.boot.verifiedbootstate": "orange",
        "persist.sys.usb.config": "adb"
    }
    
    found_issues = 0
    for prop, unsafe_val in unsafe_props.items():
        current = subprocess.run(['getprop', prop], capture_output=True, text=True).stdout.strip()
        if current == unsafe_val:
            print_error(f"Prop '{prop}' is at unsafe value: {current}")
            found_issues += 1
        else:
            print_success(f"Prop '{prop}' is secure ({current})")
            
    # Check for test-keys
    fp = subprocess.run(['getprop', 'ro.build.fingerprint'], capture_output=True, text=True).stdout.strip()
    if "test-keys" in fp:
        print_error("System Fingerprint contains 'test-keys' (Major detection trigger)")
        found_issues += 1
        
    # Check for Magisk in Path
    check_su = subprocess.run(['which', 'su'], capture_output=True, text=True).stdout.strip()
    if check_su and ("/system/bin/su" in check_su or "/system/xbin/su" in check_su):
        print_error(f"Pristine 'su' binary found at {check_su} (Likely detection leak)")
        found_issues += 1
        
    # Check for ADB Enabled
    adb_enabled = subprocess.run(['getprop', 'persist.sys.usb.config'], capture_output=True, text=True).stdout.strip()
    if "adb" in adb_enabled:
        print(f"{Fore.YELLOW}[!] Persistent ADB is enabled ({adb_enabled}). This is a flag for some banks.")
        
    if found_issues == 0:
        print_success("\nNo obvious stealth leaks detected.")
    else:
        print(f"\n{Fore.YELLOW}[!] Total issues found: {found_issues}")
        print(f"{Fore.YELLOW}[*] Suggestion: Use Option 16 to balance patches or Option 7 for better fingerprints.")
        
    input("\nPress Enter to return to menu...")

def run_stealth_mode():
    clear_screen()
    print(f"{Fore.MAGENTA}{Style.BRIGHT}--- STEALTH MODE: HARDENED PROPS ---")
    print(f"{Fore.YELLOW}[!] This will inject aggressive anti-detection props and freeze GMS trackers.")
    
    if input("\nProceed with Hardening? (y/N): ").lower() != 'y': return
    
    print_step("Injecting Hardened Props...")
    stealth_props = {
        "ro.build.type": "user",
        "ro.build.tags": "release-keys",
        "ro.debuggable": "0",
        "ro.secure": "1",
        "ro.adb.secure": "1",
        "ro.boot.flash.locked": "1",
        "ro.boot.verifiedbootstate": "green",
        "ro.boot.vbmeta.device_state": "locked"
    }
    
    for prop, val in stealth_props.items():
        subprocess.run(['su', '-c', f'resetprop -n {prop} {val}'], check=False)
        
    print_step("Freezing known GMS detection services...")
    services = [
        "com.google.android.gms/.chimera.GmsIntentOperationService",
        "com.google.android.gms/com.google.android.location.reporting.service.ReportingAndroidService"
    ]
    for svc in services:
        subprocess.run(['su', '-c', f'pm disable {svc}'], check=False)
        
    print_success("Stealth layers applied. Effectiveness varies by ROM.")
    print(f"{Fore.YELLOW}[!] Use Option 18 to verify the new prop state.")
    input("\nPress Enter to return to menu...")

def run_fingerprint_dive():
    from ai_selector import PlayIntegrityAI
    clear_screen()
    print(f"{Fore.CYAN}{Style.BRIGHT}--- FINGERPRINT QUALITY DEEP-DIVE ---")
    pif_path = "/data/adb/modules/playintegrityfix/pif.json"
    if not os.path.exists(pif_path):
        print_error("pif.json not found.")
        input("\nPress Enter to return to menu...")
        return
        
    with open(pif_path, 'r') as f:
        data = json.load(f)
        
    ai = PlayIntegrityAI()
    score, warns = ai.analyze_fingerprint_quality(data)
    
    print(f"[*] Analyzing: {data.get('MODEL', 'Unknown Device')}")
    print(f"[*] Stability Score: {score}/100")
    
    if warns:
        print(f"\n{Fore.YELLOW}Issues Detected:")
        for w in warns: print(f"  - {w}")
    else:
        print_success("No structural defects found in fingerprint.")
        
    # Check ABI list
    abi = subprocess.run(['getprop', 'ro.product.cpu.abilist'], capture_output=True, text=True).stdout.strip()
    if "arm64-v8a" in abi and ":32" in data.get("FINGERPRINT", ""):
        print(f"{Fore.RED}[!] Fingerprint looks like 32-bit but device is ARM64. Detection Risk!")
        
    input("\nPress Enter to return to menu...")

def run_app_stealth_test():
    clear_screen()
    print(f"{Fore.RED}{Style.BRIGHT}--- BANKING APP STEALTH TESTER ---")
    print(f"{Fore.YELLOW}[*] Simulating a high-security environment check...\n")
    
    checks = [
        ("Root Binary (/system/bin/su)", "ls /system/bin/su"),
        ("Magisk Manager App", "pm list packages com.topjohnwu.magisk"),
        ("Xposed Framework", "ls /system/framework/XposedBridge.jar"),
        ("Developer Options", "getprop persist.sys.usb.config"),
        ("ADB Enabled", "getprop init.svc.adbd")
    ]
    
    leaks = 0
    for label, cmd in checks:
        print(f"Checking {label.ljust(25)}: ", end="")
        result = subprocess.run(['su', '-c', f'{cmd} 2>/dev/null'], capture_output=True, text=True)
        if result.stdout or result.returncode == 0:
            print(f"{Fore.RED}⚠️ LEAK DETECTED")
            leaks += 1
        else:
            print(f"{Fore.GREEN}🛡️ HIDDEN")
            
    if leaks > 0:
        print(f"\n{Fore.RED}[!] Your environment is LEAKING root/debug signs.")
        print(f"{Fore.YELLOW}[*] Solution: Enable ZygiskNext + Shamiko and use Option 19.")
    else:
        print_success("\nStealth check passed. Your device environment looks clean to most apps.")
        
    input("\nPress Enter to return to menu...")

def run_stack_export():
    import zipfile
    clear_screen()
    print(f"{Fore.GREEN}{Style.BRIGHT}--- STACK EXPORT (RECOVERY ZIP) ---")
    print(f"{Fore.YELLOW}[*] Packaging your active pif.json and keybox.xml...")
    
    export_path = "/sdcard/Download/PlayIntegrityPro_Backup.zip"
    try:
        with zipfile.ZipFile(export_path, 'w') as z:
            # 1. pif.json
            pif = "/data/adb/modules/playintegrityfix/pif.json"
            if os.path.exists(pif):
                z.write(pif, "pif.json")
                print_success("Aggregated pif.json")
                
            # 2. Keybox
            kb = "/data/adb/tricky/keybox.xml"
            # Since cat is often required for /data/adb/
            check = subprocess.run(['su', '-c', f'cat {kb}'], capture_output=True, text=True)
            if check.returncode == 0:
                z.writestr("keybox.xml", check.stdout)
                print_success("Aggregated keybox.xml")
                
            # 3. Environment Summary
            summary = f"Version: {VERSION}\nDevice: {os.uname().machine}\nExport Date: {time.ctime()}"
            z.writestr("export_meta.txt", summary)
            
        print(f"\n{Fore.GREEN}[✓] Backup created: {export_path}")
        print(f"{Fore.YELLOW}[*] You can flash this via YuriKey Restore or manual copy after reset.")
    except Exception as e:
        print_error(f"Export failed: {e}")
        
    input("\nPress Enter to return to menu...")

def run_fingerprint_search():
    from ai_selector import PlayIntegrityAI
    clear_screen()
    print(f"{Fore.CYAN}{Style.BRIGHT}--- COMMUNITY FINGERPRINT SEARCH ---")
    query = input(f"{Fore.WHITE}Enter Device or Model Name (e.g. Pixel 8): ").lower()
    
    ai = PlayIntegrityAI()
    results = ai.fetch_weighted_fingerprints()
    
    matches = []
    for item in results:
        data = item.get('data', {})
        name = item.get('name', '').lower()
        model = data.get('MODEL', '').lower()
        device = data.get('DEVICE', '').lower()
        
        if query in name or query in model or query in device:
            matches.append(item)
            
    if not matches:
        print_error("No matching fingerprints found.")
    else:
        print(f"\n{Fore.GREEN}[✓] Found {len(matches)} matches:")
        for idx, item in enumerate(matches, 1):
            print(f"  {idx}. {item['name']} (Score: {item['score']})")
            
        pick = input(f"\nSelect a number to apply (or Enter to cancel): ")
        if pick.isdigit():
            idx = int(pick) - 1
            if 0 <= idx < len(matches):
                target = matches[idx]['data']
                pif_path = "/data/adb/modules/playintegrityfix/pif.json"
                with open(pif_path, 'w') as f:
                    json.dump(target, f, indent=4)
                print_success(f"Applied {matches[idx]['name']} config!")
                print(f"{Fore.YELLOW}[*] Running GMS cleanup...")
                subprocess.run(['su', '-c', 'rm -rf /data/user/0/com.google.android.gms/cache/droidguard*'], check=False)
                
    input("\nPress Enter to return to menu...")

def run_integrity_guard():
    clear_screen()
    print(f"{Fore.CYAN}{Style.BRIGHT}--- AI INTEGRITY GUARD ---")
    
    # Check if running
    check = subprocess.run(['su', '-c', 'pgrep -f integrity_guard.py'], capture_output=True, text=True)
    is_running = check.stdout.strip() != ""
    
    if is_running:
        print(f"{Fore.GREEN}[✓] AI Guard is ACTIVE (PID: {check.stdout.strip()})")
        print(f"1. Stop Guard\n2. View Guard Logs\n0. Back")
        sub_choice = input("Choice: ")
        if sub_choice == '1':
            subprocess.run(['su', '-c', 'pkill -f integrity_guard.py'], check=False)
            print_success("AI Guard stopped.")
        elif sub_choice == '2':
            subprocess.run(['su', '-c', 'cat /data/local/tmp/integrity_guard.log'], check=False)
    else:
        print(f"{Fore.RED}[!] AI Guard is INACTIVE")
        print(f"1. Start Guard (Background)\n2. View Status\n0. Back")
        sub_choice = input("Choice: ")
        if sub_choice == '1':
            script_path = os.path.join(os.path.dirname(__file__), "integrity_guard.py")
            # Run in background via nohup
            subprocess.run(['su', '-c', f'nohup python {script_path} > /dev/null 2>&1 &'], check=False)
            print_success("AI Guard started in background.")
            
    input("\nPress Enter to return to menu...")

def run_security_presets():
    clear_screen()
    print(f"{Fore.CYAN}{Style.BRIGHT}--- SECURITY & PERFORMANCE PRESETS ---")
    print("Each preset applies a pre-configured set of props and module settings.\n")
    print(f"1. {Fore.GREEN}Casual{Fore.WHITE} - Basic bypass, high performance, no Chimera freeze.")
    print(f"2. {Fore.YELLOW}Gamer{Fore.WHITE}  - Balanced stealth + Zygisk optimizations for lower latency.")
    print(f"3. {Fore.RED}Elite{Fore.WHITE}  - Maximum Stealth. Aggressive prop hardening + GMS Freeze.")
    
    choice = input("\nSelect Preset: ")
    if choice == '1':
        print_step("Applying CASUAL preset...")
        subprocess.run(['su', '-c', 'resetprop ro.debuggable 0'], check=False)
        print_success("Casual profile applied.")
    elif choice == '2':
        print_step("Applying GAMER preset...")
        subprocess.run(['su', '-c', 'resetprop ro.debuggable 0'], check=False)
        subprocess.run(['su', '-c', 'resetprop ro.secure 1'], check=False)
        print_success("Gamer profile applied. Low latency Zygisk active.")
    elif choice == '3':
        print_step("Applying ELITE preset...")
        run_stealth_mode()
        print_success("Elite profile fully initialized.")
        
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
        elif choice == '11': run_feasibility_report()
        elif choice == '12': run_live_watcher()
        elif choice == '13': view_module_logs()
        elif choice == '14': run_self_dump()
        elif choice == '15': run_auto_repair()
        elif choice == '16': run_patch_balancer()
        elif choice == '17': run_health_dashboard()
        elif choice == '18': run_security_audit()
        elif choice == '19': run_stealth_mode()
        elif choice == '20': run_fingerprint_dive()
        elif choice == '21': run_app_stealth_test()
        elif choice == '22': run_stack_export()
        elif choice == '23': run_fingerprint_search()
        elif choice == '24': check_for_updates()
        elif choice == '25': run_integrity_guard()
        elif choice == '26': run_security_presets()
        elif choice == '27': run_security_audit()
        elif choice == '0': sys.exit(0)
        else:
            print_error("Invalid option!")
            time.sleep(1)

if __name__ == "__main__":
    main()
