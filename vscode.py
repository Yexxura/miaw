import os
import sys
import subprocess
import shutil
from flask import Flask, redirect

# Cek apakah dijalankan sebagai root
if os.geteuid() != 0:
    print("❌ Script ini harus dijalankan sebagai root (gunakan sudo)")
    sys.exit(1)

# Cek apakah code-server tersedia
code_server_path = shutil.which("code-server")
if not code_server_path:
    print("[🌐] code-server belum terinstall. Menginstall via script resmi...")
    try:
        subprocess.check_call("curl -fsSL https://code-server.dev/install.sh | sh", shell=True)
    except subprocess.CalledProcessError:
        print("❌ Gagal menginstall code-server. Pastikan ada koneksi internet dan akses root.")
        sys.exit(1)

    code_server_path = shutil.which("code-server")
    if not code_server_path:
        print("❌ code-server masih tidak ditemukan setelah instalasi.")
        sys.exit(1)

# Jalankan code-server
print("[🚀] Menjalankan code-server di http://localhost:8080 ...")
subprocess.Popen([code_server_path, '--port', '8080', '--auth', 'none'])

# Setup Flask redirect
app = Flask(__name__)

@app.route('/')
def index():
    return redirect("http://localhost:8080")

if __name__ == '__main__':
    print("[🌐] Flask aktif di http://localhost:5000 (redirect ke VSCode Web)")
    app.run(port=5000)
