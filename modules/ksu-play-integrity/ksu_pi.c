#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/system_properties.h>
#include <unistd.h>

/**
 * ksu-pi: Native Property Injector for KernelSU v1.2.0
 */

#define SERVICE_VERSION "v1.2.0"

void set_prop(const char *name, const char *value) {
  if (__system_property_set(name, value) == 0) {
    printf("[+] %s -> %s\n", name, value);
  } else {
    printf("[!] Failed to set %s\n", name);
  }
}

void inject_hardened_props() {
  // Standard Hardening
  set_prop("ro.debuggable", "0");
  set_prop("ro.secure", "1");
  set_prop("ro.adb.secure", "1");
  set_prop("ro.build.type", "user");
  set_prop("ro.build.tags", "release-keys");

  // Privacy / Fingerprint Hardening
  set_prop("ro.boot.verifiedbootstate", "green");
  set_prop("ro.boot.flash.locked", "1");
  set_prop("ro.boot.vbmeta.device_state", "locked");
  set_prop("ro.boot.veritymode", "enforcing");

  // Experimental: Serial Masking
  set_prop("ro.serialno", "DEEPEYE2026PRO");
  set_prop("ro.boot.serialno", "DEEPEYE2026PRO");
}

int main(int argc, char *argv[]) {
  if (getuid() != 0) {
    fprintf(stderr, "[!] Root access required.\n");
    return 1;
  }

  printf("--- KSU Play Integrity PRO [%s] ---\n", SERVICE_VERSION);
  printf("[*] Initializing Native Prop Injector...\n");

  inject_hardened_props();

  printf("[✓] Native property synchronization complete.\n");
  return 0;
}
