import hashlib

s = "Python Bootcamp"
hashed_str = hashlib.sha256(s.encode('utf-8')).hexdigest()

print(hashed_str)
