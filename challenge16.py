'''
Cryptopals Set 2 Challenge 16
'''

import os
from challenge10 import cbc_encryption, cbc_decryption

key = os.urandom(16)
iv = os.urandom(16)

def encrypt_info(plaintext):
    prefix = b"comment1=cooking%20MCs;userdata="
    postfix = b";comment2=%20like%20a%20pound%20of%20bacon"
    plaintext = plaintext.replace(b';', b'')
    plaintext = plaintext.replace(b'=', b'')
    return cbc_encryption(prefix + plaintext + postfix, key, iv)

def find_admin_true(ciphertext):
    plaintext = cbc_decryption(ciphertext, key, iv)
    #print(plaintext)
    return b";admin=true;" in plaintext
'''
#sets bit at position pos to val, assuming the bit
#already in that location is the opposite
def set_bit(byte, pos, val):
    mask = 1 << pos
    if val == 1:
        return byte | mask
    elif val == 0:
        return byte & (~mask)

#returns value of bit at position pos
def get_bit(byte, pos):
    mask = 1 << pos
    if mask & byte == 0:
        return 0
    else:
        return 1

#control - sets the rules for which bits to flip
#byte - bit of byte gets flipped when corresponding bit of control is 1
def flip_byte(byte, ctrl):
    for i in range(8):
        if get_bit(ctrl, i) == 1:
            if get_bit(byte, i) == 1:
                byte = set_bit(byte, i, 0)
            else:
                byte = set_bit(byte, i, 1)
    
    return byte
'''
if __name__ == "__main__":
    #cast to bytearray to allow assignment
    #use \x00 for ease: we just have to flip the bits in the ciphertext
    #corresponding to the '1's of our desired inserted character
    #such that the bits of the \x00 gets flipped to become our chosen char
    #which is essentially an xor
    asdf = bytearray(encrypt_info(b'\x00admin\x00true'))

    #asdf[16] = flip_byte(asdf[16], ord(';'))
    #asdf[38 - 16] = flip_byte(asdf[38 - 16], ord('='))

    asdf[16] = asdf[16] ^ ord(';')
    asdf[22] = asdf[22] ^ ord('=')
    assert find_admin_true(asdf)