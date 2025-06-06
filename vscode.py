import os
import sys
import subprocess
from flask import Flask, redirect

if os.geteuid() != 0:
    print("Script harus dijalankan sebagai root!")
    sys.exit(1)

app = Flask(__name__)

subprocess.Popen(['code-server', '--port', '8080', '--auth', 'none'])

@app.route('/')
def index():
    return redirect("http://localhost:8080")

if __name__ == '__main__':
    app.run(port=5000)
