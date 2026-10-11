# 🎯 Track Scammer

**GPS Phishing Tracker — Standalone Tools**

Tools phishing GPS untuk **research**, **educational**, dan **authorized pentest**.
Display data di terminal, tanpa bot Telegram, portable di Termux +
[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://python.org)
[![Platform](https://img.shields.io/badge/Platform-Termux%20%7C%20Nethunter%20%7C%20Linux-green)](https://termux.com)
[![License](https://img.shields.io/badge/License-MIT-yellow)](LICENSE)

---

## 📋 Daftar Isi

- Fitur
- Persyaratan
- Instalasi
- Cara Pakai
- Fitur 03 — Stop Server
- Fitur 04 — Lihat Hasil (Auto Browser)
- Template Phishing
- Data yang Di-capture
- Struktur Folder
- Cara Kerja
- Troubleshooting
- FAQ
- Legal Disclaimer
- License

---

## ✨ Kelebihan Utama

**Semua berjalan dalam satu proses:** server Flask (port 8080) + tunnel SSH + tampilan terminal + HTML report di browser. Tidak butuh multi-terminal, tidak butuh bot Telegram.

### Perbandingan dengan Tools Lain

| Aspek | Tools Lain | Track Scammer |
|---|---|---|
| Terminal | 3+ terminal | 2 terminal saja |
| Perintah Start | 3+ perintah | 1 perintah |
| Pengaturan | Manual tiap bagian | Otomatis |
| Monitoring | Buka terminal lain | Terintegrasi + HTML |
| Bot | Butuh token | Tidak butuh |
| Notifikasi | Telegram/HTTP | Terminal + Browser |
| View hasil | Manual JSON | **Browser otomatis** |

---

## ✨ Fitur

### 🎣 Phishing Engine
- **6 Template Realistis** — Google Drive, WhatsApp, Telegram, Zoom, Cloudflare, Bank
- **Fake Cloudflare Check** — mirip asli, user tidak curiga
- **Fake reCAPTCHA** — checkbox + animasi loading
- **SVG Logo Asli** — bukan emoji, kelihatan profesional
- **Responsive** — support HP + desktop

### 📍 Data Capture
- **IP Address** — jaringan + publik + WebRTC
- **Geolokasi** — negara, kota, wilayah, ISP, timezone
- **GPS Koordinat** — latitude, longitude, akurasi
- **Reverse Geocode** — alamat lengkap dari koordinat
- **Device Fingerprint** — platform, OS, CPU, RAM, resolusi
- **Battery Info** — level + charging status
- **Incognito Detection** — deteksi mode private
- **Camera Capture** — foto depan (640x480 JPEG)

### 🌐 Networking
- **SSH Tunnel** — link publik gratis via localhost.run
- **Flask Server** — port 8080
- **Waitress Production** — stabil

### 💾 Data Management
- **Auto-save JSON** — ke folder hasil/
- **Display Terminal** — panel rich rapi
- **HTML Report** — kartu korban + foto + GPS
- **Auto-open Browser** — menu 04 langsung buka Chrome (via termux-api)
- **Tanpa Telegram** — tidak butuh bot token

### 🔧 Platform
- **Termux Support** — Android
- **Nethunter Support** — Kali Linux ARM
- **Linux Support** — Ubuntu, Debian, Arch
- **Cross-Platform** — auto-detect

## Cara Menjalankan Track Scammer

<img src="https://raw.githubusercontent.com/NdikzDatabase/Database/main/uploads/23778a3f-fc9d-493f-a3a2-f3da327b31c8.jpeg"/>

<img src="https://raw.githubusercontent.com/NdikzDatabase/Database/main/uploads/47dfb9a0-0728-4404-ae89-de7dc4bdcf84.jpeg"/>

<img src="https://raw.githubusercontent.com/NdikzDatabase/Database/main/uploads/d6f972c1-813c-4bbc-aab6-53d7e2f112d9.jpeg"/>

<img src="https://raw.githubusercontent.com/NdikzDatabase/Database/main/uploads/a320d6c3-f4b8-4356-aa18-3e3f8765c41c.jpeg"/>

---

## 📸 Screenshot

### Menu Utama

<img src="https://raw.githubusercontent.com/NdikzDatabase/Database/main/uploads/a2a8eacd-ffa0-4d38-80a4-96649f5ba12a.jpeg"/>

### Hasil Capture

<img src="https://raw.githubusercontent.com/NdikzDatabase/Database/main/uploads/4547881c-409c-4c2f-a957-39385431e75d.jpeg"/>

---

## 📦 Persyaratan

| Komponen | Versi |
|---|---|
| Python | 3.8+ |
| Termux | Latest (F-Droid) |
| RAM | 1 GB+ |
| Storage | 100 MB |
| Koneksi | Internet (untuk tunnel) |

**Dependencies Python:**
- rich — tampilan terminal
- flask — web server
- flask-cors — CORS support
- requests — HTTP client
- waitress — production WSGI server

**SSH** — sudah ada di Termux/Linux by default.

**Termux:API** (opsional) — untuk auto-buka browser di menu 04.

---

## 🚀 Instalasi

### Quick Install (Termux)

```bash
pkg update && pkg upgrade -y
pkg install python -y
pip install rich flask flask-cors requests waitress
