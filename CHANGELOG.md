# Changelog

All notable changes to this project will be documented in this file.

## [v1.1.0] - 2026-02-13

### Added

- **Strong Integrity Feasibility Analyzer**: Real-time scoring of device compatibility for "3 Greens".
- **Auto-Repair Engine**: Surgical recovery tool for GMS caches and missing modules.
- **Live Attestation Watcher**: Real-time monitoring of attestation handshakes via logcat.
- **Self-Dump Engine**: Export local hardware properties to a standard `pif.json`.
- **AI & Community Scrapper**: Integrated community-verified fingerprint fetching from GitHub.
- **Surgical GMS Hygiene**: Replaced nuclear data clearing with precise cache cleanup to avoid logouts.
- **DeepEye Integrity Diagnostic**: Advanced verification of fingerprint injection and TEE hooks.
- **Release Automation**: Unified build script for Magisk and KSU modules.
- **Debug Playbook**: Comprehensive troubleshooting matrix for 2026 security landscape.

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
