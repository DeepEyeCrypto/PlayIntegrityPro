# 📖 Installation Guide (v1.3.0)

## ⚡ Prerequisites

- **Rooted Android**: Magisk 27+ / KernelSU / APatch.
- **Environment**: Termux (for Automation) OR custom recovery for manual flashing.
- **Android Version**: Android 13, 14, 15, and 16 Preview.

---

## 🚀 Method 1: Termux Automation (Recommended)

This is the fastest "Elite" setup. It installs the python dependencies and triggers the orchestrator.

```bash
# 1. Update Termux and install dependencies
pkg update && pkg install python git -y

# 2. Fire the orchestrator
curl -sSL https://raw.githubusercontent.com/DeepEyeCrypto/PlayIntegrityPro/main/src/play_integrity_fixer.py | python
```

### 🛠️ Execution Roadmap

1. **Select Option 1**: (Nuclear Reset) To sanitize your GMS/Play Store environment.
2. **Select Option 2**: (Install Stack) This deploys ZygiskNext, TrickyStore, Shamiko, and the Core module.
3. **REBOOT**.
4. **Select Option 10**: (YuriKey Action) If aiming for **STRONG** integrity.
5. **Select Option 19**: (Stealth Mode) If banking apps still detect root after 3 Greens.

---

## 📦 Method 2: Manual Flash (Magisk / KernelSU)

Download the production-ready ZIPs from the [Official Releases](https://github.com/DeepEyeCrypto/PlayIntegrityPro/releases).

1. **Magisk**: Flash `PlayIntegrityPro-v1.3.0.zip`.
2. **KernelSU**: Flash `ksu-play-integrity-v1.3.0.zip`.
3. **Post-Install**:
    - Restart into Android.
    - Open Termux and run the `Option 17 (Health Dashboard)` to verify all layers are active.

---

## 🔧 Pro Troubleshooting Matrix

| Issue | Solution (Tool Option) |
| :--- | :--- |
| **Basic Red (Integrity Fail)** | Use **Option 15** (Auto-Repair) or **Option 1** (Nuclear). |
| **Strong Red / Hardware Fail** | Use **Option 11** (Feasibility) then **Option 10** (Keybox). |
| **Banking App Detects Root** | Use **Option 19** (Stealth) + **Option 9** (Whitelist). |
| **Bootloop / System UI Hang** | Boot to Safe Mode and use **Option 22** to export backup. |
| **Stale Detection** | Use **Option 12** (Watcher) and check for Keystore/TEE leaks. |

---

## 🏆 Achieving "3 Greens" (Strong Integrity)

For the ultimate success, combine **TrickyStore** + a valid **Keybox.xml** + **Play Integrity Pro v1.1.5**.

If **Option 18 (Security Audit)** reports structural leaks (orange bootloader state, debug props), use **Option 19** to harden your system properties before running a Play Integrity check.

---
Made with ❤️ by DeepEyeCrypto
