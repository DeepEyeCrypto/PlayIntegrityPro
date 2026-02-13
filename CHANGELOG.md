# Changelog

All notable changes to this project will be documented in this file.

## [v1.3.0] - 2026-02-13

- **Security Presets (Casual/Gamer/Elite)**: Quick-apply pre-configured stealth and performance profiles.
- **Deep System Integrity Audit**: Expanded scan for Magisk leaks, ADB status, and system property vulnerabilities.
- **KSU Installer Fix**: Properly extracts native prop engine assets on KernelSU.

## [v1.2.5] - 2026-02-13

- **AI Integrity Guard**: Resident background service that auto-heals DroidGuard failures.
- **Improved Stealth Props**: Native KernelSU injector now handles device serial numbers and bootloader states more aggressively.
- **Corrupted Module Sync Fixed**: Unified v1.2.5 across all module types.

## [v1.2.0] - 2026-02-13

- **Community Fingerprint Search**: Filter and apply fingerprints from GitHub repositories by device name.
- **Script Self-Update**: Automated mechanism to download and replace the orchestrator script with the latest version.
- **Improved Version Sync**: Unified v1.2.0 across all modules and scripts.

## [v1.1.5] - 2026-02-13

- **Export Working Stack**: Generate a recovery ZIP for backups.
- **Fingerprint Deep-Dive**: Forensic analysis of fingerprint stability.
- **Banking Stealth Tester**: Simulation of bank app environment checks.
- **Native Prop Injector v1.1.5**: Updated C binary for KSU with hardened props and 1.1.5 features.
- **Improved Documentation**: Cleaned README and updated Strong Integrity Guide.
- **Hardened Cleanup**: autopif4.sh now uses surgical cache pruning.

## [v1.1.0] - 2026-02-13

- **Strong Integrity Feasibility Analyzer**: Real-time scoring of device compatibility for "3 Greens".
- **Auto-Repair Engine**: Surgical recovery tool for GMS caches and missing modules.
- **Live Attestation Watcher**: Real-time monitoring of attestation handshakes via logcat.
- **Enforce Stealth Mode**: Aggressive prop hardening for bypass of modern detections.
- **Self-Dump Engine**: Export local hardware properties to a standard `pif.json`.
- **Surgical GMS Hygiene**: Replaced nuclear data clearing with precise cache cleanup.
- **Module Health Dashboard**: Real-time monitoring for TrickyStore and Zygisk.
- **Security Shield Audit**: Foreground scan for stealth leaks in build properties.

## [v1.0.0] - 2026-01-31

### Initial Implementation

- Initial release of Play Integrity Pro.
- Automated Termux fixer script with Nuclear Reset.
- Magisk and KernelSU module templates.
- Native `ksu-pi` C binary for KernelSU prop injection.
- Automated fingerprint rotation script (`autopif4.sh`).
- GitHub Actions for automated release building.

### Fixed

- Early-boot prop injection for hidden root state.
- GMS cache clearing logic.
