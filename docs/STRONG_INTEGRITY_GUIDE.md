# 🛡️ Strong Play Integrity (3 Green) Guide (2026 Edition)

Achieving `MEETS_STRONG_INTEGRITY` (3 Green checkmarks) requires a perfect synchronization of specialized modules. This guide covers both the manual "Deep-Dive" and the **Play Integrity Pro** automated method.

---

## ⚡ 1. The "Golden Stack" (Prerequisites)

To pass **STRONG**, your device must convince Google that it is unrooted, has a locked bootloader, and possesses a valid, unrevoked hardware Keybox.

### Required Components

1. **ZygiskNext**: The foundation for root masking and Zygisk module support.
2. **PlayIntegrityFix (PIF)**: For userspace fingerprint spoofing (Basic/Device integrity).
3. **TrickyStore**: The driver that intercepts Keystore calls to spoof bootloader status.
4. **Keybox.xml**: A set of unique hardware certificates (provided via YuriKey actions).

---

## 🚀 2. The Elite Method: Play Integrity Pro (Recommended)

Instead of manual flashing and terminal commands, use the **Play Integrity Pro** orchestrator.

1. **Installer**:

    ```bash
    curl -sSL https://raw.githubusercontent.com/DeepEyeCrypto/PlayIntegrityPro/main/src/play_integrity_fixer.py | python
    ```

2. **Steps**:
    * **Option 2 (Install Stack)**: Installs the entire logic (ZygiskNext, TrickyStore, etc) in one go.
    * **Option 10 (YuriAction)**: Triggers the Keybox fetcher directly and configures TrickyStore automatically.
    * **Option 11 (Feasibility)**: Checks if your bootloader/TEE is actually capable of Strong integrity.
    * **Option 19 (Stealth)**: Hides root flags that lingering apps might see even with 3 Greens.

---

## 🏗️ 3. Manual Installation Order

If you prefer the manual route via Magisk/KernelSU:

### Phase A: The Foundation

1. **Reboot** once to ensure a clean state.
2. **Flash ZygiskNext**. **Reboot**.
3. **Flash PlayIntegrityFix**. (Required for Basic/Device levels).

### Phase B: The Strong Layer

4. **Flash TrickyStore**.
2. **Flash YuriKey Manager**.
3. **Reboot**.
4. **Run Action**: Magisk -> Modules -> YuriKey -> **Action Button**. (This fetches your `keybox.xml`).
5. **Final Reboot**.

---

## 🩺 4. Diagnostic Checklist

If you are still seeing **STRONG RED**:

1. **Check Fingerprint Stability**: Use **Option 20** (Deep-Dive) in our tool. 32-bit fingerprints on 64-bit-only hardware are common failure points in 2026.
2. **Wipe GMS Data**: Use **Option 15** (Auto-Repair) to clear the attestation cache. Google caches "FAIL" states for up to 24 hours.
3. **Patch Alignment**: Ensure your `ro.build.version.security_patch` in `pif.json` matches what the Play Integrity API expects for your chosen fingerprint. Use **Option 16** (Balancer) to sync them.
4. **Stealth Leaks**: Even with 3 Greens, apps like JPM or Chase might fail if they see `ro.debuggable=1`. Run **Option 18** (Security Audit) to find these leaks.

---

## 📊 5. Verification Tools

| App | Purpose |
| :--- | :--- |
| **Play Integrity API Checker** | The ultimate source of truth for 3 Greens. |
| **YASNAC** | Quick check for Basic Integrity and SafetyNet. |
| **Key Attestation Tester** | Deep-dive into TEE properties (Keymaster/KeyMint). |

---

## 🛑 Structural "No-Go" Scenarios

* **Samsung Knox (0x1)**: If tripped, your TEE is permanently physically restricted from reporting a valid hardware state. **STRONG** may be impossible.
* **Legacy TEE**: Some pre-2018 devices lack the hardware modules required for hardware-backed attestation.

***
*Credits: Yurii0307, Osm0sis, Chiteroman, and the DeepEyeCrypto team.*
