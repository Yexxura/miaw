import os
import sys
import subprocess

# Cek dan install flask jika belum ada
try:
    from flask import Flask, redirect
except ImportError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "flask"])
    from flask import Flask, redirect

# Cek apakah dijalankan sebagai root
if os.geteuid() != 0:
    print("Script ini harus dijalankan sebagai root.")
    sys.exit(1)

# Jalankan code-server di background (port 8080)
subprocess.Popen(['code-server', '--port', '8080', '--auth', 'none'])

# Setup Flask redirect ke code-server
app = Flask(__name__)

@app.route('/')
def index():
    return redirect("http://localhost:8080")

if __name__ == '__main__':
    app.run(port=5000)
