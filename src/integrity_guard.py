import os
import subprocess
import time
import sys

LOGFILE = "/data/local/tmp/integrity_guard.log"

def log(msg):
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
    with open(LOGFILE, "a") as f:
        f.write(f"[{timestamp}] {msg}\n")
    print(msg)

def check_and_heal():
    log("[*] Running Integrity Guard check...")
    # Check if pif.json is being respected
    try:
        current_fp = subprocess.check_output(['getprop', 'ro.build.fingerprint'], text=True).strip()
        log(f"[*] Current Fingerprint: {current_fp}")
        
        # Check for DroidGuard errors in logcat (last 1000 lines)
        logcat = subprocess.check_output(['logcat', '-d', '-t', '1000'], text=True)
        if "DroidGuard" in logcat and ("fail" in logcat.lower() or "error" in logcat.lower()):
            log("[!] DroidGuard failure detected in logcat!")
            heal()
    except Exception as e:
        log(f"[!] Error during check: {e}")

def heal():
    log("[*] Triggering Auto-Heal cycle...")
    # 1. Surgical Cache Cleanup
    log("[*] Pruning GMS caches...")
    subprocess.run(['rm', '-rf', '/data/user/0/com.google.android.gms/cache/droidguard*'], check=False)
    subprocess.run(['rm', '-rf', '/data/user/0/com.google.android.gms/app_dg_cache/*'], check=False)
    
    # 2. Kill GMS to force reload
    log("[*] Restarting GMS...")
    subprocess.run(['killall', 'com.google.android.gms'], check=False)
    
    log("[✓] Auto-Heal complete. Monitoring resumed.")

if __name__ == "__main__":
    log("=== Play Integrity Pro: AI Guard Started ===")
    while True:
        check_and_heal()
        time.sleep(1800) # Check every 30 mins
