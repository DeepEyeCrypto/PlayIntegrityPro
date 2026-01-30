##########################################################################################
#
# Magisk Module Installer Script
#
##########################################################################################

# Set to true if you need to enable Zygisk
ZYGISK_MOD=true

# Set to true if you want to skip mount
SKIPMOUNT=false

# Set to true if you want to use the common/system folder
PROPFILE=true
POSTFSDATA=true
LATESTARTSERVICE=true

print_modname() {
  ui_print "*******************************"
  ui_print "      Play Integrity Pro       "
  ui_print "      By: enayat               "
  ui_print "*******************************"
}

on_install() {
  ui_print "- Extracting module files"
  unzip -o "$ZIPFILE" 'system/*' -d "$MODPATH" >&2
}

set_permissions() {
  set_perm_recursive "$MODPATH" 0 0 0755 0644
  set_perm "$MODPATH/service.sh" 0 0 0755
  set_perm "$MODPATH/post-fs-data.sh" 0 0 0755
}
