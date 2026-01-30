#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/system_properties.h>
#include <unistd.h>

/**
 * ksu-pi: Native Property Injector for KernelSU
 * Designed to bypass userspace detection by using native setprop calls
 * and handling sensitive props at the earliest possible boot stage.
 */

void set_prop(const char *name, const char *value) {
  if (__system_property_set(name, value) == 0) {
    printf("[+] %s -> %s\n", name, value);
  } else {
    printf("[!] Failed to set %s\n", name);
  }
}

int main(int argc, char *argv[]) {
  if (getuid() != 0) {
    fprintf(stderr, "[!] Root access required. Run via KSU/Magisk su.\n");
    return 1;
  }

  printf("[*] Play Integrity Pro: Native Prop Injector v1.0\n");

  // 1. Core Integrity Props
  set_prop("ro.boot.vbmeta.device_state", "locked");
  set_prop("ro.boot.verifiedbootstate", "green");
  set_prop("ro.boot.flash.locked", "1");
  set_prop("ro.boot.veritymode", "enforcing");
  set_prop("ro.boot.warranty_bit", "0");
  set_prop("ro.warranty_bit", "0");

  // 2. Hide Bootloader & Release Props
  set_prop("ro.boot.bootloader", "locked");
  set_prop("ro.build.tags", "release-keys");
  set_prop("ro.build.type", "user");
  set_prop("ro.debuggable", "0");
  set_prop("ro.secure", "1");

  // 3. Optional: GMS specific props if needed
  // set_prop("ro.com.google.clientidbase", "android-google");

  printf("[✓] Native property synchronization complete.\n");
  return 0;
}
