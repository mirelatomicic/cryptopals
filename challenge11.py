'''
Cryptopals Set 2 Challenge 11
'''
import os
from random import randint
from challenge10 import cbc_encryption
from challenge7 import encrypt_aec
from challenge8 import score_reps

ecb = 1
cbc = 2

#From any plaintext, adds bytes to the start and end, and randomly
#encrypts with either ecb or cbc, then guesses which method was used
def encryption_oracle(plaintext):
    #add random 5-10 bytes to start and end
    plaintext = os.urandom(randint(5,10)) + plaintext + os.urandom(randint(5,10))
    key = os.urandom(16)

    method = randint(1, 2)
    if method == ecb:
        ciphertext = encrypt_aec(plaintext, key)
    else:
        iv = os.urandom(16)
        ciphertext = cbc_encryption(plaintext, key, iv)

    if encryption_detect(ciphertext) == method:
        return "The oracle correctly guessed!"
    
    return "The oracle was wrong"

#sees whether it was encrypted with ECB or CBC
def encryption_detect(ciphertext):
    if score_reps(ciphertext) > 0: #use our ecb detection method
        return ecb
    
    return cbc

if __name__ == "__main__":
    print(encryption_oracle(b'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA'))