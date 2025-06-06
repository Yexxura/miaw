import os
import sys
import subprocess
import shutil
import webbrowser
import time

# Cek code-server di PATH user
code_server_path = shutil.which("code-server")

# Jika belum ada, install di user space (tanpa sudo)
if not code_server_path:
    print("[🌐] code-server belum ditemukan. Menginstall secara lokal (tanpa root)...")
    try:
        subprocess.check_call("curl -fsSL https://code-server.dev/install.sh | bash", shell=True)
    except subprocess.CalledProcessError:
        print("❌ Gagal menginstall code-server. Pastikan ada koneksi internet.")
        sys.exit(1)

    # Setelah install, coba cek ulang
    code_server_path = shutil.which("code-server")
    if not code_server_path:
        print("❌ code-server masih tidak ditemukan setelah instalasi.")
        print("💡 Coba tambahkan ~/.local/bin ke PATH, lalu jalankan ulang script ini.")
        sys.exit(1)

# Jalankan code-server (bind ke localhost)
print("[🚀] Menjalankan code-server di http://localhost:8080 ...")
subprocess.Popen([
    code_server_path,
    '--port', '8080',
    '--auth', 'none',
    '--bind-addr', '127.0.0.1:8080'
])

# Tunggu agar server siap
time.sleep(3)

# Buka browser
webbrowser.open("http://localhost:8080")
print("[🌐] Browser terbuka ke VSCode Web")
