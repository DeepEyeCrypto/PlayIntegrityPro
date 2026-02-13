import os
import zipfile
import shutil
from pathlib import Path

def create_zip(source_dir, output_filename):
    print(f"[*] Packaging {output_filename}...")
    with zipfile.ZipFile(output_filename, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(source_dir):
            for file in files:
                file_path = os.path.join(root, file)
                arcname = os.path.relpath(file_path, source_dir)
                zipf.write(file_path, arcname)
    print(f"[+] Created {output_filename}")

def main():
    # Setup paths
    base_dir = Path(__file__).parent
    modules_dir = base_dir / "modules"
    dist_dir = base_dir / "dist"
    
    # Ensure dist exists
    dist_dir.mkdir(exist_ok=True)
    
    # Package Magisk Module
    magisk_src = modules_dir / "PlayIntegrityPro"
    create_zip(magisk_src, dist_dir / "PlayIntegrityPro-v1.1.5.zip")
    
    # Package KernelSU Module
    ksu_src = modules_dir / "ksu-play-integrity"
    create_zip(ksu_src, dist_dir / "ksu-play-integrity-v1.1.5.zip")
    
    print("\n[!] Release builds are ready in the 'dist' directory.")

if __name__ == "__main__":
    main()
