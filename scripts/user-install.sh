#!/usr/bin/env bash
set -e

# Create installation directory
sudo mkdir -p /opt/nettraveler-ex
sudo chown -R $USER:$USER /opt/nettraveler-ex

# Locate and extract tar.gz file
TAR_FILE=""
if [[ -f nettraveler_lite.tar.gz ]]; then
    TAR_FILE="nettraveler_lite.tar.gz"
elif [[ -f nettraveler_full.tar.gz ]]; then
    TAR_FILE="nettraveler_full.tar.gz"
else
    echo "[!] No NetTraveler tar.gz file found in current directory."
    exit 1
fi

echo "[+] Extracting $TAR_FILE to /opt/nettraveler-ex..."
tar -xzvf "$TAR_FILE" -C /opt/nettraveler-ex

# Move binary to /usr/local/bin (better than /bin)
sudo mv /opt/nettraveler-ex/dist/nettraveler /usr/local/bin/

# Environment instruction
echo "[+] Installation complete."
echo "Add the following to your shell configuration to set NT_DATAROOT:" 
echo "    export NT_DATAROOT=/opt/nettraveler-ex/dist/spellbook"
