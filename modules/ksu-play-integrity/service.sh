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
else
    # Fallback to shell setprop
    setprop ro.boot.vbmeta.device_state locked
    setprop ro.boot.verifiedbootstate green
    setprop ro.boot.flash.locked 1
fi
