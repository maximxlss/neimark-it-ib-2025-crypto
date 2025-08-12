from flask import Flask, send_from_directory
from Crypto.Cipher import AES
import os

app = Flask(__name__)

KEY = b"0123456709abcdef"
FLAG = "neimark{h3ll0_3cb_he11o_2f5383a}"


@app.route('/ecbcbcwtf/decrypt/<ciphertext>/')
def decrypt(ciphertext):
    ciphertext = bytes.fromhex(ciphertext)

    cipher = AES.new(KEY, AES.MODE_ECB)
    try:
        decrypted = cipher.decrypt(ciphertext)
    except ValueError as e:
        return {"error": str(e)}

    return {"plaintext": decrypted.hex()}


@app.route('/ecbcbcwtf/encrypt_flag/')
def encrypt_flag():
    iv = os.urandom(16)
    cipher = AES.new(KEY, AES.MODE_CBC, iv)
    encrypted = cipher.encrypt(FLAG.encode())
    ciphertext = iv.hex() + encrypted.hex()
    return {"ciphertext": ciphertext}

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def serve_static(path):
    static_dir = os.path.join(os.path.dirname(__file__), 'static')
    if path == '':
        path = 'ECB CBC WTF.html'  # Default file
    return send_from_directory(static_dir, path)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
