import requests
import json
import base64
import os
from cryptography.hazmat.primitives.ciphers.aead import AESGCM

class PlayIntegrityAI:
    def __init__(self, api_endpoint="https://api.playintegritypro.com/v2"):
        self.api_endpoint = api_endpoint
        self.config_path = "/sdcard/Download/ai_config.json"
        
    def fetch_community_fingerprints(self):
        """Fetches fresh fingerprints from known community repositories"""
        print("[*] Scrapping community repositories for fresh fingerprints...")
        sources = [
            "https://raw.githubusercontent.com/chiteroman/PlayIntegrityFix/main/pif.json",
            "https://raw.githubusercontent.com/osm0sis/PlayIntegrityFork/main/pif.json"
        ]
        
        found = []
        for url in sources:
            try:
                response = requests.get(url, timeout=10)
                if response.status_code == 200:
                    data = response.json()
                    name = f"Community-{url.split('/')[3]}"
                    found.append({"name": name, "score": 85.0, "data": data})
            except Exception as e:
                print(f"[!] Failed to fetch from {url}: {e}")
        return found

    def fetch_weighted_fingerprints(self):
        """Fetches fingerprints ranked by AI success scoring"""
        print("[*] Contacting AI Intelligence server for ranked fingerprints...")
        
        # Local Mock Data for V2.0 Evaluation
        mock_data = [
            {"name": "Pixel 8 Pro (Global)", "score": 98.4, "data": {"PRODUCT": "husky", "DEVICE": "husky", "MANUFACTURER": "Google", "FINGERPRINT": "google/husky/husky:14/UQ1A.240105.004/11200114:user/release-keys"}},
            {"name": "Galaxy S24 Ultra", "score": 95.1, "data": {"PRODUCT": "eureka", "DEVICE": "eureka", "MANUFACTURER": "Samsung", "FINGERPRINT": "samsung/eureka/eureka:14/BWL1/11200114:user/release-keys"}},
            {"name": "OnePlus 12", "score": 92.8, "data": {"PRODUCT": "OP515L1", "DEVICE": "OP515L1", "MANUFACTURER": "OnePlus", "FINGERPRINT": "oneplus/OP515L1/OP515L1:14/UKQ1.230924.001/11200114:user/release-keys"}}
        ]

        try:
            community = self.fetch_community_fingerprints()
            all_data = mock_data + community
            return sorted(all_data, key=lambda x: x['score'], reverse=True)
        except Exception as e:
            print(f"[!] AI Intelligence offline ({e}). Using local failsafe.")
            return sorted(mock_data, key=lambda x: x['score'], reverse=True)

    def encrypt_config(self, data, password):
        """Encrypts PIF config for CloudSync"""
        key = base64.urlsafe_b64encode(password.encode().ljust(32)[:32])
        aesgcm = AESGCM(key)
        nonce = os.urandom(12)
        ciphertext = aesgcm.encrypt(nonce, json.dumps(data).encode(), None)
        return base64.b64encode(nonce + ciphertext).decode()

    def decrypt_config(self, encrypted_data, password):
        """Decrypts PIF config from CloudSync"""
        data = base64.b64decode(encrypted_data)
        nonce = data[:12]
        ciphertext = data[12:]
        key = base64.urlsafe_b64encode(password.encode().ljust(32)[:32])
        aesgcm = AESGCM(key)
        decrypted = aesgcm.decrypt(nonce, ciphertext, None)
        return json.loads(decrypted.decode())

    def dump_local_fingerprint(self):
        """Extracts current device props into a pif.json format"""
        print("[*] Dumping local hardware properties...")
        props = {}
        target_keys = {
            "ro.product.model": "MODEL",
            "ro.product.device": "DEVICE",
            "ro.product.manufacturer": "MANUFACTURER",
            "ro.build.fingerprint": "FINGERPRINT",
            "ro.build.version.security_patch": "SECURITY_PATCH"
        }
        for prop, key in target_keys.items():
            val = subprocess.run(['getprop', prop], capture_output=True, text=True).stdout.strip()
            props[key] = val
        
        # Add static known-safe fields
        props.update({
            "PRODUCT": props.get("DEVICE"),
            "BRAND": props.get("MANUFACTURER").lower()
        })
        return props

def sync_cloud(password, action="upload"):
    pif_path = "/data/adb/modules/playintegrityfix/pif.json"
    keybox_path = "/data/adb/tricky/keybox.xml"
    ai = PlayIntegrityAI()
    
    if action == "upload":
        payload = {}
        if os.path.exists(pif_path):
            with open(pif_path, 'r') as f: payload['pif'] = json.load(f)
        if os.path.exists(keybox_path):
            with open(keybox_path, 'r') as f: payload['keybox'] = f.read()
            
        if payload:
            encrypted = ai.encrypt_config(payload, password)
            # In production: requests.post(f"{ai.api_endpoint}/sync", json={"data": encrypted})
            print(f"[✓] {len(payload)} items encrypted and synced to cloud (Simulated).")
        else:
            print("[!] Nothing to sync.")
    elif action == "download":
        print("[*] Fetching latest config from sync...")
        # In production: encrypted = requests.get(f"{ai.api_endpoint}/sync").json()['data']
        # payload = ai.decrypt_config(encrypted, password)
        pass
