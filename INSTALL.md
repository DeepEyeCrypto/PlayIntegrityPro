# 📖 Installation Guide

## Prerequisites

- Rooted Android (Magisk 27+ / KernelSU)
- Termux OR Magisk Manager
- Android 13+

---

## Method 1: Termux (Recommended - 2 Minutes)

This method automates the entire process, including dependency installation and module configuration.

```bash
# 1. Update packages and install python
pkg update && pkg install python git -y

# 2. Run fixer
curl -sSL https://raw.githubusercontent.com/DeepEyeCrypto/PlayIntegrityPro/main/src/play_integrity_fixer.py | python
```

### Installation Steps in Script

1. **Setup Dependencies**: The script will automatically install `requests`, `colorama`, and `cryptography`.
2. **Nuclear Cleanup**: Select Option 1 to wipe GMS/Play Store data for a fresh start.
3. **Stack Install**: Select Option 2 to download and install ZygiskNext, PIF-NEXT, TrickyStore, and Shamiko.
4. **Reboot**: Restart your device to apply changes.
5. **AI Fingerprint**: Run the script again and select Option 7 for an AI-optimized fingerprint.

---

## Method 2: Magisk Modules (Manual)

If you prefer to flash files manually via the Magisk app:

1. Download both ZIPs from the [Releases](https://github.com/DeepEyeCrypto/PlayIntegrityPro/releases) page:
   - `PlayIntegrityPro-v1.0.zip`
   - `ksu-play-integrity-v1.0.zip` (Required for KernelSU users)

2. **Open Magisk App** → Modules → Install from storage.
3. Select the downloaded ZIP(s).
4. **Reboot** → Open an integrity checker to verify "3 Greens".

---

## Method 3: Recovery Flash

For those who prefer TWRP/OrangeFox:

```bash
adb push PlayIntegrityPro-v1.0.zip /sdcard/
# Reboot to recovery
# Install -> Select PlayIntegrityPro-v1.0.zip
# Reboot System
```

---

## 🔧 Troubleshooting

| Issue | Solution |
|-------|----------|
| **"No working fingerprint"** | Run Option 3 (`autopif4.sh`) in the Termux script. |
| **"1 Green only"** | Use the Nuclear Reset (Option 1) to clear GMS cache. |
| **"Banking app crash"** | Run Option 9 to configure the Shamiko whitelist. |
| **"KernelSU not working"** | Ensure the `ksu-pi` binary has execution permissions. |

## 📊 Verification Tools

Use these apps to confirm your status:

- **YASNAC** (Play Integrity/SafetyNet tester)
- **Play Integrity API Checker**
- **Google Wallet / Payment Apps**
