import hashlib
import os

Pass = input("Enter Your password : ")
Pass = Pass.encode()
salt = os.urandom(16)
password_hash = hashlib.pbkdf2_hmac("sha256", Pass, salt, 100000)

print(password_hash)
