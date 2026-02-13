# 🛠️ Play Integrity Pro: Debug Playbook (2026 Edition)

If you have installed the full stack but are still seeing **STRONG RED** or experiencing app failures (Google Wallet, Banking Apps), follow this decision matrix to identify and fix the root cause.

## 🚦 Troubleshooting Matrix

| Symptom | Detection Command (Termux) | Likely Root Cause | Recommended Fix |
| :--- | :--- | :--- | :--- |
| **BASIC RED** | `su -c 'which magisk'` | Root hiding broken. | Ensure **ZygiskNext** is active. |
| **STRONG RED** | `ls /data/adb/tricky/keybox.xml` | Keybox revoked. | Use **Option 10** to rotate keybox. |
| **3 GREENS** fail | `logcat \| grep -i "attestation"` | GMS cache issue. | Use **Option 1** (Nuclear Reset). |
| **No Keybox** | `ls /data/adb/tricky/` | Pathing error. | Check permissions (644). |
| **Bootloop** | `n/a` | Module conflict. | Use Safe Mode to uninstall. |

---

## 🏗️ Phase 4: Stealth Mode (Hardened Props)

If you have 3 Greens but a specific app (e.g., highly secured Banking, Work Profile apps) still fails:

1. **Run Option 19** in the tool.
2. This will:
    * Inject `ro.adb.secure=1` (Disables hidden ADB triggers).
    * Sanitize `ro.build.tags` and `ro.build.type`.
    * Freeze GMS Chimera services that track hardware mismatches.
3. **Warning:** Some ROMs may experience push notification delays with Chimera frozen. If this happens, use Option 15 to Repair.

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
* **Action:** If `STRONG` is red, ensure this date matches the one expected by your current Keybox.

### 3. RKP (Remote Key Provisioning) Interference

On Android 14+, Google may force RKP.

* **Check:** `getprop remote_provisioning.status`
* **If 'active':** Google may override your local Keybox. This requires the "RKP Bypass" strategy included in our stack.

---

## 🚫 Structural "No-Go" Scenarios

In some cases, Strong Integrity is **impossible** via software:

1. **Samsung Knox (0x1)**: If Knox is tripped, hardware attestation is often permanently disabled.
2. **Broken Keymaster**: Some Custom ROMs have legacy/broken TEE implementations.
3. **Blacklisted Serials**: If your device ID itself is blacklisted by Google.

---

*Reference: [Strong Play Integrity Guide](STRONG_INTEGRITY_GUIDE.md)*
