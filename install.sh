#!/bin/bash

# Track Scammer installer - Termux Only
# by CELI-SANITNEL

set -e

G='\033[0;32m'
R='\033[0;31m'
Y='\033[0;33m'
C='\033[0;36m'
N='\033[0m'

ok()   { echo -e "${G}[+]${N} $1"; }
err()  { echo -e "${R}[-]${N} $1"; }
warn() { echo -e "${Y}[!]${N} $1"; }
info() { echo -e "${C}[*]${N} $1"; }

# Cek Termux
if [ -z "$PREFIX" ] || [ ! -d "$PREFIX" ] || ! echo "$PREFIX" | grep -q "com.termux"; then
    err "Script ini cuma buat Termux!"
    exit 1
fi

info "Termux detected"
info "Arch: $(uname -m)"

# Update repo
info "Update repo..."
pkg update -y >/dev/null 2>&1 || warn "update gagal"
ok "repo updated"

# Install Python
if ! command -v python3 >/dev/null 2>&1; then
    info "Install python..."
    pkg install -y python
fi

if command -v python3 >/dev/null 2>&1; then
    ok "python3: $(python3 --version 2>&1)"
else
    err "python gagal install"
    exit 1
fi

# Install pip
if ! python3 -m pip --version >/dev/null 2>&1; then
    info "Install pip..."
    pkg install -y python-pip
fi

if python3 -m pip --version >/dev/null 2>&1; then
    ok "pip ready"
else
    warn "pip gak terdeteksi"
fi

# Install dependencies python
info "Install dependencies..."

for pkg in rich flask flask-cors requests waitress; do
    if python3 -c "import ${pkg//-/_}" >/dev/null 2>&1; then
        ok "  $pkg (already)"
    else
        python3 -m pip install --quiet --upgrade "$pkg" >/dev/null 2>&1 && \
            ok "  $pkg installed" || \
            warn "  $pkg gagal"
    fi
done

# Cek SSH (buat tunnel)
if command -v ssh >/dev/null 2>&1; then
    ok "ssh: $(ssh -V 2>&1 | head -1)"
else
    info "Install openssh..."
    pkg install -y openssh
    ok "ssh installed"
fi

# Cek curl
if command -v curl >/dev/null 2>&1; then
    ok "curl ready"
else
    info "Install curl..."
    pkg install -y curl
    ok "curl installed"
fi

# === Termux API untuk auto-buka browser ===
info "Setup termux-api (untuk auto-buka browser di menu 04)..."

if command -v termux-open-url >/dev/null 2>&1; then
    ok "termux-open-url ready"
    # test
    if termux-open-url "about:blank" >/dev/null 2>&1; then
        ok "  auto-buka browser aktif"
    else
        warn "  termux-open-url ada tapi gagal panggil browser"
        warn "  Install app 'Termux:API' dari F-Droid/Play Store"
    fi
else
    info "Install termux-api package..."
    pkg install -y termux-api 2>/dev/null && \
        ok "  termux-api package installed" || \
        warn "  termux-api gagal install"

    info "Cek lagi..."
    if command -v termux-open-url >/dev/null 2>&1; then
        ok "  termux-open-url sekarang ready"
        if termux-open-url "about:blank" >/dev/null 2>&1; then
            ok "  auto-buka browser aktif"
        else
            warn "  Install app 'Termux:API' dari F-Droid/Play Store"
            warn "  Link: https://f-droid.org/packages/com.termux.api/"
        fi
    else
        warn "termux-open-url masih tidak ada"
        warn "Buka menu 04 akan tampilkan URL manual (copy-paste ke browser)"
    fi
fi

# === Final check ===
echo ""
echo "=== Verifikasi ==="
echo ""

python3 --version >/dev/null 2>&1 && echo "  python3     ok" || echo "  python3     MISSING"
python3 -c "import rich" >/dev/null 2>&1 && echo "  rich        ok" || echo "  rich        MISSING"
python3 -c "import flask" >/dev/null 2>&1 && echo "  flask       ok" || echo "  flask       MISSING"
python3 -c "import flask_cors" >/dev/null 2>&1 && echo "  flask-cors  ok" || echo "  flask-cors  MISSING"
python3 -c "import requests" >/dev/null 2>&1 && echo "  requests    ok" || echo "  requests    MISSING"
python3 -c "import waitress" >/dev/null 2>&1 && echo "  waitress    ok" || echo "  waitress    MISSING"
command -v ssh >/dev/null 2>&1 && echo "  ssh         ok" || echo "  ssh         MISSING"
command -v curl >/dev/null 2>&1 && echo "  curl        ok" || echo "  curl        MISSING"
command -v termux-open-url >/dev/null 2>&1 && echo "  termux-api  ok" || echo "  termux-api  MISSING (opsional)"

echo ""
echo "=== Install selesai ==="
echo ""
echo "Cara pakai:"
echo ""
echo "  Terminal 1:"
echo "    cd ~/TrackScammer"
echo "    python3 track.py"
echo ""
echo "  Terminal 2:"
echo "    ssh -o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null -R 80:localhost:8080 nokey@localhost.run"
echo ""
echo "  Menu 04 - lihat hasil:"
echo "    - kalau termux-api aktif: browser otomatis kebuka"
echo "    - kalau tidak: copy URL http://localhost:8080/view ke browser"
echo ""
