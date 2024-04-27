import jwt 

with open('../additional files/rh2.pem', 'r') as f:
    PUBLIC_KEY = f.read()

PUBLIC_KEY = "\n".join(PUBLIC_KEY.splitlines())
PUBLIC_KEY = PUBLIC_KEY.encode() + b'\n'

encoded = jwt.encode({'username': 'kriska', 'admin': True}, PUBLIC_KEY, algorithm='HS256')

print(encoded)
    