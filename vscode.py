import subprocess
import shutil
import webbrowser
import time
import sys
import os

# Cegah root user
if os.geteuid() == 0:
    print("❌ Jangan jalankan script ini sebagai root.")
    sys.exit(1)

# Cek apakah code-server tersedia di PATH
code_server_path = shutil.which("code-server")
if not code_server_path:
    print("❌ 'code-server' tidak ditemukan di PATH.")
    print("➡️  Silakan install manual tanpa sudo lalu pastikan masuk ke PATH.")
    sys.exit(1)

# Jalankan code-server
print(f"🚀 Menjalankan code-server dari: {code_server_path}")
subprocess.Popen([
    code_server_path,
    "--port", "8080",
    "--auth", "none",
    "--bind-addr", "127.0.0.1:8080"
])

# Tunggu server hidup
time.sleep(3)

# Buka browser
webbrowser.open("http://localhost:8080")
print("🌐 VSCode Web terbuka di browser.")
