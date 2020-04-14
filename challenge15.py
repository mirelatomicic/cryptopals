'''
Cryptopals Set 2 Challenge 15
'''
from challenge9 import unpad, is_padded

def valid_pkcs7(plaintext):
    if not is_padded(plaintext):
        raise Exception("Invalid padding")
    return unpad(plaintext)
