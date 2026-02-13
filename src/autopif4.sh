#!/system/bin/sh
# autopif4.sh - Automated Play Integrity Fingerprint Finder/Updater
# Credits: osm0sis & the PIF community

MODDIR="/data/adb/modules/playintegrityfix"
PIF_JSON="$MODDIR/pif.json"
TEMP_JSON="/data/local/tmp/pif.json"

echo "[*] Checking for Play Integrity Fix module..."
if [ ! -d "$MODDIR" ]; then
    echo "[!] Play Integrity Fix module not found at $MODDIR"
    exit 1
fi

echo "[*] Fetching latest fingerprints from community source..."
# Using a reliable community source for fingerprints
URL="https://raw.githubusercontent.com/chiteroman/PlayIntegrityFix/main/pif.json"

if command -v curl >/dev/null; then
    curl -sL "$URL" -o "$TEMP_JSON"
elif command -v wget >/dev/null; then
    wget -q "$URL" -O "$TEMP_JSON"
else
    echo "[!] Neither curl nor wget found. Cannot download fingerprints."
    exit 1
fi

if [ -s "$TEMP_JSON" ]; then
    echo "[+] Fingerprints downloaded successfully."
    mv "$TEMP_JSON" "$PIF_JSON"
    chmod 644 "$PIF_JSON"
    chown root:root "$PIF_JSON"
    echo "[+] Updated $PIF_JSON"
    
    # Surgical GMS cleanup to apply changes without logout
    echo "[*] Performing surgical GMS cache cleanup..."
    rm -rf /data/user/0/com.google.android.gms/cache/droidguard*
    rm -rf /data/user/0/com.google.android.gms/app_dg_cache/*
    # Play Store cache
    rm -rf /data/user/0/com.android.vending/cache/*
    
    echo "[+] Done. A reboot is recommended, but cached integrity should clear shortly."
else
    echo "[!] Downloaded file is empty. Update failed."
    exit 1
fi
