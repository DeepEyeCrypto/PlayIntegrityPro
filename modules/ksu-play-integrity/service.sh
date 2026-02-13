#!/system/bin/sh
# ksu-play-integrity - Boot Service
MODDIR=${0%/*}

# Wait for boot
while [ "$(getprop sys.boot_completed)" != "1" ]; do
    sleep 2
done

# Native prop injection (Preferred)
if [ -f "$MODDIR/system/bin/ksu-pi" ]; then
    chmod 755 "$MODDIR/system/bin/ksu-pi"
    "$MODDIR/system/bin/ksu-pi"
fi

# Apply Fingerprint from PIF module
log() { echo "[$(date '+%T')] KSU-PI: $1" >> /data/local/tmp/ksu_pip.log; }

for pifdir in /data/adb/modules/playintegrityfix* /data/adb/modules/pif-next*; do
  if [ -d "$pifdir" ]; then
    fp=""
    [ -f "$pifdir/pif.prop" ] && fp=$(grep '^ro.build.fingerprint=' "$pifdir/pif.prop" | cut -d= -f2-)
    [ -z "$fp" ] && [ -f "$pifdir/pif.json" ] && fp=$(grep '"FINGERPRINT"' "$pifdir/pif.json" | head -1 | sed 's/.*"FINGERPRINT": "\([^"]*\)".*/\1/')
    
    if [ -n "$fp" ]; then
      resetprop ro.build.fingerprint "$fp"
      log "Applied fingerprint: $fp"
      break
    fi
  fi
done

# Surgical GMS hygiene (once per day)
STAMP=/data/local/tmp/ksu_pip_gms_stamp
if [ ! -f "$STAMP" ] || [ "$(cat $STAMP 2>/dev/null)" != "$(date +%F)" ]; then
  rm -rf /data/user/0/com.google.android.gms/cache/droidguard*
  rm -rf /data/user/0/com.google.android.gms/app_dg_cache/*
  rm -rf /data/user/0/com.android.vending/cache/*
  echo "$(date +%F)" > "$STAMP"
fi
