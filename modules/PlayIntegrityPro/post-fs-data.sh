#!/system/bin/sh
# PlayIntegrityPro - Early Prop Injection
MODDIR=${0%/*}

# Set early props to spoof non-rooted state
resetprop -n ro.boot.vbmeta.device_state locked
resetprop -n ro.boot.verifiedbootstate green
resetprop -n ro.boot.flash.locked 1
resetprop -n ro.boot.veritymode enforcing
resetprop -n ro.boot.warranty_bit 0
resetprop -n ro.warranty_bit 0

# Hide bootloader unlock signs
resetprop -n ro.boot.bootloader locked
resetprop -n ro.build.tags release-keys
resetprop -n ro.build.type user
