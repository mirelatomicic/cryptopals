'''
Cryptopals Set 1 Challenge 7
'''
#this tutorial was used
#https://techtutorialsx.com/2018/04/09/python-pycrypto-using-aes-128-in-ecb-mode/ 

import base64
from Crypto.Cipher import AES
from challenge9 import pad_block, unpad

def decrypt_aec(encrypted, key):
    decipher = AES.new(key, AES.MODE_ECB)
    return unpad(decipher.decrypt(encrypted))

def encrypt_aec(message, key):
    cipher = AES.new(key, AES.MODE_ECB)
    #pad if length of message is suitable for blocks of 16
    if len(message) % 16 != 0:
        message = pad_block(message, len(message) + 16 - len(message) % 16)
    return cipher.encrypt(message)

if __name__ == "__main__":
    encrypted = base64.b64decode(open("challenge7.txt", 'r').read())
    key = b"YELLOW SUBMARINE"
    print(decrypt_aec(encrypted, key))
    print(decrypt_aec(encrypt_aec(b'Hi', key), key))

