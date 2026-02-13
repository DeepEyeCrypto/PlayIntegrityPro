#!/system/bin/sh
# check_strong_integrity.sh
# Checks for the presence of required components for Strong Play Integrity (YuriKey method)

echo "=== Strong Play Integrity Environment Check ==="

# 1. Check Root Manager
if [ -d "/data/adb/modules" ]; then
    echo "[*] Magisk/KernelSU modules directory found."
else
    echo "[!] /data/adb/modules not found. Are you rooted?"
    exit 1
fi

# 2. Check for Required Modules by folder name (common names)
MODULES_DIR="/data/adb/modules"

echo ""
echo "--- Checking Installed Modules ---"

# ZygiskNext
if [ -d "$MODULES_DIR/zygisk_next" ] || [ -d "$MODULES_DIR/ZygiskNext" ]; then
    echo "[+] ZygiskNext found."
else
    echo "[-] ZygiskNext NOT found (Recommended)."
fi

# Play Integrity Fix (Fork or Inject)
if [ -d "$MODULES_DIR/playintegrityfix" ]; then
    echo "[+] Play Integrity Fix found."
else
    echo "[-] Play Integrity Fix NOT found (Required)."
fi

# TrickyStore
if [ -d "$MODULES_DIR/trickystore" ] || [ -d "$MODULES_DIR/TrickyStore" ]; then
    echo "[+] TrickyStore found."
else
    echo "[-] TrickyStore NOT found (Required for Strong Integrity)."
fi

# YuriKey
if [ -d "$MODULES_DIR/yurikey" ] || [ -d "$MODULES_DIR/YuriKey" ]; then
    echo "[+] YuriKey module found."
else
    echo "[-] YuriKey module NOT found (Required for Keybox management)."
fi

# 3. Check for dependencies (curl/wget)
echo ""
echo "--- Checking Dependencies ---"

if command -v curl >/dev/null; then
    echo "[+] curl is installed."
elif command -v wget >/dev/null; then
    echo "[+] wget is installed."
else
    echo "[!] Neither curl nor wget found. YuriKey action will FAIL."
    echo "    -> Install BusyBox module or generic curl/wget."
fi

echo ""
echo "=== Check Complete ==="
echo "Recommended Order: ZygiskNext -> PIF -> TrickyStore -> YuriKey"
echo "Ref: docs/STRONG_INTEGRITY_GUIDE.md"
