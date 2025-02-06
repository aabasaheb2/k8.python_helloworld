import base64

username = 'YWRtaW4='
password = 'YWRtaW5wYXNzd29yZA=='
decodedUsername = base64.b64decode(username)
decodedPassword = base64.b64decode(password)