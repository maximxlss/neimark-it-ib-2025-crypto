from flask import Flask, send_from_directory
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import os
from datetime import datetime, timedelta

app = Flask(__name__)

KEY = b"0123456709abcdef"
FLAG = "neimark{5up3r_n1c3_1c060df5}"


@app.route('/flipping_cookie/check_admin/<cookie>/<iv>/')
def check_admin(cookie, iv):
    cookie = bytes.fromhex(cookie)
    iv = bytes.fromhex(iv)

    try:
        cipher = AES.new(KEY, AES.MODE_CBC, iv)
        decrypted = cipher.decrypt(cookie)
        unpadded = unpad(decrypted, 16)
    except ValueError as e:
        return {"error": str(e)}

    if b"admin=True" in unpadded.split(b";"):
        return {"flag": FLAG}
    else:
        return {"error": "Only admin can read the flag"}


@app.route('/flipping_cookie/get_cookie/')
def get_cookie():
    expires_at = (datetime.today() + timedelta(days=1)).strftime("%s")
    cookie = f"admin=False;expiry={expires_at}".encode()

    iv = os.urandom(16)
    padded = pad(cookie, 16)
    cipher = AES.new(KEY, AES.MODE_CBC, iv)
    encrypted = cipher.encrypt(padded)
    ciphertext = iv.hex() + encrypted.hex()

    return {"cookie": ciphertext}

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def serve_static(path):
    static_dir = os.path.join(os.path.dirname(__file__), 'static')
    if path == '':
        path = 'Flipping Cookie.html'  # Default file
    return send_from_directory(static_dir, path)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
