##########################################################################################
#
# KernelSU Module Installer Script
#
##########################################################################################

print_modname() {
  ui_print "*******************************"
  ui_print "      KSU Play Integrity       "
  ui_print "      Native Prop Fix          "
  ui_print "*******************************"
}

on_install() {
  ui_print "- Extracting module files"
  unzip -o "$ZIPFILE" 'service.sh' -d "$MODPATH" >&2
}

set_permissions() {
  set_perm "$MODPATH/service.sh" 0 0 0755
}
