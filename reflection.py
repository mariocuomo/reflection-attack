import base64
import os
from cryptography.fernet import Fernet
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.hkdf import HKDF

password = b"password"
hkdf = HKDF(
     algorithm=hashes.MD5(),
     length=32,
     salt=None,
     info=None,
     backend=default_backend()
)
key = base64.urlsafe_b64encode(hkdf.derive(password))
f = Fernet(key)
token = f.encrypt(b"hello!")
print(token)
file = open('user.key', 'wb')
file.write(key)
file.close()
file = open('user.key', 'rb')
key = file.read()
file.close()
f = Fernet(key)

print(f.decrypt(token)) 
