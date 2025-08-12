from flask import Flask, send_from_directory
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
import os

app = Flask(__name__)

KEY = b"0123456709abcdef"
FLAG = "neimark{c00l3r_3cb_2f2b57d9c644}"


@app.route('/ecb_oracle/encrypt/<plaintext>/')
def encrypt(plaintext):
    plaintext = bytes.fromhex(plaintext)

    padded = pad(plaintext + FLAG.encode(), 16)
    cipher = AES.new(KEY, AES.MODE_ECB)
    try:
        encrypted = cipher.encrypt(padded)
    except ValueError as e:
        return {"error": str(e)}

    return {"ciphertext": encrypted.hex()}

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def serve_static(path):
    static_dir = os.path.join(os.path.dirname(__file__), 'static')
    if path == '':
        path = 'ECB Oracle.html'  # Default file
    return send_from_directory(static_dir, path)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
