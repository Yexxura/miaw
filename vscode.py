import subprocess
from flask import Flask, redirect

app = Flask(__name__)

# Jalankan code-server (VSCode web) di port 8080
subprocess.Popen(['code-server', '--port', '8080', '--auth', 'none'])

@app.route('/')
def index():
    # Redirect ke code-server di port 8080
    return redirect("http://localhost:8080")

if __name__ == '__main__':
    app.run(port=5000)
