#!/usr/bin/env bash
set -e

# URLs for NetTraveler versions
URL_LITE="http://example.com/nettraveler_lite.tar.gz"
URL_FULL="http://example.com/nettraveler_full.tar.gz"

# Prompt user for version
echo "Select NetTraveler version to install:"
echo "1) Lite"
echo "2) Full"
read -rp "Enter choice [1 or 2]: " VERSION_CHOICE

case "$VERSION_CHOICE" in
    1)
        TAR_FILE="nettraveler_lite.tar.gz"
        DOWNLOAD_URL="$URL_LITE"
        ;;
    2)
        TAR_FILE="nettraveler_full.tar.gz"
        DOWNLOAD_URL="$URL_FULL"
        ;;
    *)
        echo "Invalid choice. Exiting."
        exit 1
        ;;
esac

# Download if not already present
if [[ ! -f "$TAR_FILE" ]]; then
    echo "[+] Downloading $TAR_FILE from $DOWNLOAD_URL..."
    curl -fsSL -o "$TAR_FILE" "$DOWNLOAD_URL"
fi

# Create installation directory
sudo mkdir -p /opt/nettraveler-ex
sudo chown -R $USER:$USER /opt/nettraveler-ex

# Extract tar.gz
echo "[+] Extracting $TAR_FILE to /opt/nettraveler-ex..."
tar -xzvf "$TAR_FILE" -C /opt/nettraveler-ex

# Move binary to /usr/local/bin
sudo mv /opt/nettraveler-ex/dist/nettraveler /usr/local/bin/

# Instructions for NT_DATAROOT
echo "[+] Installation complete."
echo "Add the following to your shell configuration to set NT_DATAROOT:"
echo "    export NT_DATAROOT=/opt/nettraveler-ex/dist/spellbook"
