import subprocess
import os
import json
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

class StrongIntegrityAnalyzer:
    def __init__(self):
        self.props = {}
        self._load_props()

    def _load_props(self):
        """Load system properties via getprop"""
        try:
            # Using su to ensure we get all props, though many are public
            result = subprocess.run(['su', '-c', 'getprop'], capture_output=True, text=True, timeout=5)
            for line in result.stdout.splitlines():
                if ":" in line:
                    parts = line.split(":", 1)
                    key = parts[0].strip(" []")
                    val = parts[1].strip(" []")
                    self.props[key] = val
        except Exception as e:
            print(f"{Fore.RED}[!] Error loading properties: {e}")

    def get_prop(self, key, default="unknown"):
        return self.props.get(key, default)

    def analyze(self):
        score = 100
        reasons = []

        print(f"\n{Fore.CYAN}{Style.BRIGHT}--- STRONG INTEGRITY FEASIBILITY REPORT (v2026) ---")
        
        # 1. Check Bootloader Status
        bl_state = self.get_prop("ro.boot.verifiedbootstate")
        bl_locked = self.get_prop("ro.boot.flash.locked")
        
        if bl_state == "orange" or bl_locked == "0":
            score -= 30
            reasons.append(f"{Fore.YELLOW}[!] Bootloader is UNLOCKED ({bl_state}/{bl_locked})")
        else:
            reasons.append(f"{Fore.GREEN}[+] Bootloader appears LOCKED state ({bl_state})")

        # 2. Check TEE / KeyMint Version
        km_version = self.get_prop("ro.hardware.keystore_desede")
        if "KeyMint" in km_version or "keymint" in km_version.lower():
            reasons.append(f"{Fore.CYAN}[*] Modern KeyMint TEE detected (Requires active spoofing)")
        elif km_version != "unknown":
            reasons.append(f"{Fore.CYAN}[*] Legacy Keymaster TEE detected ({km_version})")

        # 3. Check for TrickyStore
        if os.path.exists("/data/adb/modules/trickystore") or os.path.exists("/data/adb/modules/TrickyStore"):
            score += 20
            reasons.append(f"{Fore.GREEN}[+] TrickyStore Module Installed (+20)")
        else:
            score -= 60
            reasons.append(f"{Fore.RED}[!] TrickyStore Missing (-60). STRONG is impossible without it.")

        # 4. Check for Keybox (Root-aware)
        keybox_paths = [
            "/data/adb/tricky/keybox.xml",
            "/data/adb/modules/trickystore/keybox.xml"
        ]
        keybox_found = False
        keybox_valid = False
        for p in keybox_paths:
            check = subprocess.run(['su', '-c', f'[ -f {p} ] && ls -l {p}'], capture_output=True, text=True)
            if check.returncode == 0:
                keybox_found = True
                # Extract size from ls -l output (usually 5th field)
                try:
                    size = int(check.stdout.split()[4])
                    if size > 500: keybox_valid = True
                except: pass
                break

        if keybox_valid:
            score += 30
            reasons.append(f"{Fore.GREEN}[+] Valid Keybox.xml detected (+30)")
        elif keybox_found:
            score += 10
            reasons.append(f"{Fore.YELLOW}[!] Keybox.xml found but looks empty/small (+10)")
        else:
            score -= 40
            reasons.append(f"{Fore.RED}[!] No keybox.xml found. STRONG will FAIL (-40)")

        # 5. RKP Status
        rkp_status = self.get_prop("remote_provisioning.status", "unknown")
        if rkp_status == "active":
            reasons.append(f"{Fore.YELLOW}[!] RKP is ACTIVE. Server-side enforcement may override local keyboxes.")

        # Display analysis
        for r in reasons:
            print(f" {r}")
        
        print(f"\n{Fore.WHITE}{Style.BRIGHT}Calculated Score: {score}/100")
        
        if score >= 80:
            print(f"{Fore.GREEN}{Style.BRIGHT}Verdict: HIGH FEASIBILITY")
            print("Environment is primed for 3-Green success.")
        elif score >= 50:
            print(f"{Fore.YELLOW}{Style.BRIGHT}Verdict: MEDIUM FEASIBILITY")
            print("Technically possible, but requires manual keybox tuning.")
        else:
            print(f"{Fore.RED}{Style.BRIGHT}Verdict: LOW FEASIBILITY")
            print("Strong Integrity is likely unreachable on this configuration.")
        
        print(f"\n{Fore.CYAN}[*] Suggestion: Use 'YuriKey Action' to sync keybox if score is low.")

if __name__ == "__main__":
    analyzer = StrongIntegrityAnalyzer()
    analyzer.analyze()
