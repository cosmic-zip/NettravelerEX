#! /bin/bash
echo "[x] Install packages"
set -e

# Check if docker exists
if ! docker info &>/dev/null; then
    echo "[+] Docker not found or not working, installing..."
    curl -fsSL https://get.docker.com -o get-docker.sh
    sudo sh ./get-docker.sh
    rm -f get-docker.sh
else
    echo "[+] Docker is already installed and working."
fi

# Ensure user is in docker group
if groups $USER | grep -q "\bdocker\b"; then
    echo "[+] User '$USER' is already in the docker group."
else
    echo "[+] Adding $USER to docker group..."
    sudo usermod -aG docker $USER
    echo ">>> You may need to log out and back in for the group change to take effect."
fi


script 2 install deps

sudo apt install -y \
    python3-pip p7zip-full build-essential chromium-browser coreutils curl dirb \
    dnsenum dnsutils file foremost freeglut3-dev git htop iproute2 iptables kakoune \
    libc-bin libatm1t64 libatomic1 libayatana-appindicator3-dev libclang-dev \
    libclang1-18 libglu1-mesa libimage-exiftool-perl libllvm15 liboss4-salsa-asound2 \
    libssl-dev libwebkit2gtk-4.1-dev libxdo-dev librsvg2-dev lsof lua5.4 ngrep nmap \
    openssh-server openssl pkg-config qemu-kvm ruby steghide tor traceroute tree \
    virt-manager wget whois xattr xxd bash qemu-system-gui pipx build-essential python3-dev
pipx ensurepath
pipx install nuitka