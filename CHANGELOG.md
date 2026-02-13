# Changelog

All notable changes to this project will be documented in this file.

## [v1.1.5] - 2026-02-13

- **Export Working Stack**: Generate a recovery ZIP for backups.
- **Fingerprint Deep-Dive**: Forensic analysis of fingerprint stability.
- **Banking Stealth Tester**: Simulation of bank app environment checks.
- **Improved README**: Fixed linting and simplified documentation.
- **Hardened Cleanup**: autopif4.sh now uses surgical cache pruning.

## [v1.1.0] - 2026-02-13

### Added

- **Strong Integrity Feasibility Analyzer**: Real-time scoring of device compatibility for "3 Greens".
- **Auto-Repair Engine**: Surgical recovery tool for GMS caches and missing modules.
- **Live Attestation Watcher**: Real-time monitoring of attestation handshakes via logcat.
- **Fingerprint Quality Deep-Dive**: Analysis of `pif.json` for known detection triggers.
- **Banking App Stealth Tester**: Advanced environment check simulation for high-security apps.
- **Enforce Stealth Mode**: Aggressive prop hardening for bypass of modern detections.
- **Self-Dump Engine**: Export local hardware properties to a standard `pif.json`.
- **Surgical GMS Hygiene**: Replaced nuclear data clearing with precise cache cleanup.
- **Native Prop Injector v1.1.0**: Updated C binary for KSU with hardened props.

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
