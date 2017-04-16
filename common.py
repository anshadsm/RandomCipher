code hided 






































































































from Crypto.Cipher import AES
from datetime import datetime

key = '1234567891234567'
message = 'your_message'
cipher = AES.new(key)

def pad(s):
    return s + ((16-len(s)%16) * '{')

def encrypt(plaintext):
    global cipher
    return cipher.encrypt(plaintext)

def decrypt(ciphertext):
    global cipher
    dec = cipher.decrypt(ciphertext)
    l= dec.count('{')
    return dec[:len(dec)-l-(len_time+1)]


print("message :", message)
message=pad(message)
encrypted = encrypt(message)
decrypted = decrypt(encrypted)
print("Encrypted :",encrypted)
print("Decrypted :",decrypted)

