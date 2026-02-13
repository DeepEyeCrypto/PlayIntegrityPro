#!/system/bin/sh
# ksu-play-integrity - Boot Service
MODDIR=${0%/*}

log() { echo "[$(date '+%T')] KSU-PI: $1" >> /data/local/tmp/ksu_pip.log; }

# Wait for boot
while [ "$(getprop sys.boot_completed)" != "1" ]; do
    sleep 2
done

# Hardened Stealth Props (Native Shell Injection)
log "Injecting Hardened Stealth Props..."
resetprop ro.debuggable 0
resetprop ro.secure 1
resetprop ro.adb.secure 1
resetprop ro.build.type user
resetprop ro.build.tags release-keys
resetprop ro.boot.verifiedbootstate green
resetprop ro.boot.flash.locked 1
resetprop ro.boot.vbmeta.device_state locked
resetprop ro.boot.veritymode enforcing
resetprop ro.serialno DEEPEYE2026PRO
resetprop ro.boot.serialno DEEPEYE2026PRO

# Apply Fingerprint from PIF module
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
  log "Pruning GMS caches..."
  rm -rf /data/user/0/com.google.android.gms/cache/droidguard*
  rm -rf /data/user/0/com.google.android.gms/app_dg_cache/*
  rm -rf /data/user/0/com.android.vending/cache/*
  echo "$(date +%F)" > "$STAMP"
fi

log "✅ Boot synchronization complete"
