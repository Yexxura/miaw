import os
import sys
import subprocess
import shutil
import webbrowser
import time

HOME = os.path.expanduser("~")
LOCAL_BIN = os.path.join(HOME, ".local", "bin")
CODE_SERVER = shutil.which("code-server")

# Pastikan ~/.local/bin ada di PATH (untuk sesi ini saja)
os.environ["PATH"] += os.pathsep + LOCAL_BIN

if not CODE_SERVER:
    print("[📦] code-server belum ditemukan. Menginstall secara lokal (tanpa root)...")
    install_cmd = "curl -fsSL https://code-server.dev/install.sh | bash"
    try:
        subprocess.check_call(install_cmd, shell=True, executable="/bin/bash")
    except subprocess.CalledProcessError:
        print("❌ Gagal menginstall code-server.")
        sys.exit(1)
    CODE_SERVER = shutil.which("code-server")
    if not CODE_SERVER:
        print("❌ Instalasi selesai, tapi code-server tidak ditemukan.")
        print("💡 Tambahkan ini ke shell kamu:\nexport PATH=\"$HOME/.local/bin:$PATH\"")
        sys.exit(1)

print("[🚀] Menjalankan code-server di http://localhost:8080 ...")
subprocess.Popen([
    CODE_SERVER,
    '--port', '8080',
    '--auth', 'none',
    '--bind-addr', '127.0.0.1:8080'
])

time.sleep(3)
webbrowser.open("http://localhost:8080")
print("[🌐] VSCode Web siap digunakan.")
