#!/system/bin/sh
MODDIR=${0%/*}
LOGFILE=/data/local/tmp/pip.log

log() { 
  echo "[$(date '+%F %T')] $1" | tee -a $LOGFILE 
}

# Wait for boot
until [ "$(getprop sys.boot_completed)" = "1" ]; do sleep 1; done

log "=== Play Integrity Pro Starting ==="

# Find PIF module and apply fingerprint
for pifdir in /data/adb/modules/playintegrityfix* /data/adb/modules/PlayIntegrityFix* /data/adb/modules/pif-next*; do
  if [ -d "$pifdir" ]; then
    if [ -f "$pifdir/pif.prop" ]; then
      fp=$(grep '^ro.build.fingerprint=' "$pifdir/pif.prop" | cut -d= -f2-)
    elif [ -f "$pifdir/pif.json" ]; then
      fp=$(grep '"FINGERPRINT"' "$pifdir/pif.json" | head -1 | sed 's/.*"FINGERPRINT": "\([^"]*\)".*/\1/')
    fi
    
    if [ -n "$fp" ]; then
      resetprop ro.build.fingerprint "$fp"
      log "✅ Applied fingerprint: $fp"
      break
    fi
  fi
done

# Daily GMS hygiene (once per day)
STAMP=/data/local/tmp/pip_gms_stamp
if [ ! -f "$STAMP" ] || [ "$(cat $STAMP 2>/dev/null)" != "$(date +%F)" ]; then
  log "🧹 Clearing GMS data (daily)"
  pm clear com.google.android.gms >/dev/null 2>&1
  echo "$(date +%F)" > "$STAMP"
fi

log "✅ Service complete"
 # CAUTION: This can be nuclear. 
# Better: Just clear cache.
rm -rf /data/user/0/com.google.android.gms/cache/*

# Late prop sync if needed
# resetprop -n ...
