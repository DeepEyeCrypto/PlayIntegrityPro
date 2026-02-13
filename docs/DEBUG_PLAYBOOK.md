# 🛠️ Play Integrity Pro: Debug Playbook (2026 Edition)

If you have installed the full stack but are still seeing **STRONG RED** or experiencing app failures (Google Wallet, Banking Apps), follow this decision matrix to identify and fix the root cause.

---

## 🚦 Troubleshooting Matrix

| Symptom | Detection Command (Termux) | Likely Root Cause | Recommended Fix |
| :--- | :--- | :--- | :--- |
| **BASIC RED** | `su -c 'which magisk'` | Root hiding is broken or Zygisk failed. | Ensure **ZygiskNext** is active. Disable Magisk's "Enforce Denylist" (let Shamiko handle it). |
| **STRONG RED** (Device Green) | `ls /data/adb/tricky/keybox.xml` | Keybox is revoked or misconfigured. | Use **Option 10** (YuriKey Action) to rotate your keybox. Check if `target.txt` includes GMS. |
| **3 GREENS** but **Wallet Fails** | `logcat | grep -i "attestation"` | GMS has cached a previous "Fail" state. | Use **Option 1** (Nuclear Reset) to wipe GMS/Play Store data. Reboot and wait 20 mins. |
| **"No Keybox Found"** | `ls /data/adb/tricky/` | TrickyStore pathing error. | Ensure keybox.xml is in `/data/adb/tricky/` with 644 permissions. Re-run YuriAction. |
| **Bootloop after Install** | `n/a` | Module conflict (e.g. old SafetyNetFix). | Boot to Safe Mode and use **Option 1** to clear old integrity modules. |

---

## 🧪 Advanced Diagnostics

### 1. Verification of TrickyStore

TrickyStore is the core driver for Strong Integrity. To verify it is intercepting Keystore calls:

```bash
su -c 'logcat | grep -i "TrickyStore"'
```

If you see `Handle attestation key successfully`, your Keybox is working.

### 2. Security Patch Alignment

Google checks if the hardware-reported patch matches your system props.

* **Check Prop:** `getprop ro.build.version.security_patch`
* **Action:** If `STRONG` is red, ensure this date matches the one expected by your current Keybox (YuriKey handles this automatically for curated keys).

### 3. RKP (Remote Key Provisioning) Interference

On Android 14+, Google may force RKP.

* **Check:** `getprop remote_provisioning.status`
* **If 'active':** Google may override your local Keybox. This requires the "RKP Bypass" strategy included in the latest **Play Integrity Pro** stack.

---

## 🚫 Structural "No-Go" Scenarios

In some cases, Strong Integrity is **impossible** via software:

1. **Samsung Knox (0x1)**: If Knox is tripped, hardware attestation is often permanently disabled in the TEE.
2. **Broken Keymaster**: Some Custom ROMs have legacy/broken TEE implementations that cannot handle modern KeyMint certificates.
3. **Blacklisted Serials**: If your device ID itself is blacklisted by Google (rare).

---
*Reference: [Strong Play Integrity Guide](STRONG_INTEGRITY_GUIDE.md)*
