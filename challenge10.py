'''
Cryptopals Set 2 Challenge 10
'''
import base64
from challenge7 import encrypt_aec, decrypt_aec
from challenge9 import pad_block, unpad

#setting block size
block_size = 16

#xors two byte arrays
def xor_bytes(a, b):
    xor = b''
    for byte_a, byte_b in zip(a, b):
        xor += bytes([byte_a ^ byte_b])
    return xor

#encrypts using aec in cbc mode
def cbc_encryption(plaintext, key, i_iv):
    iv = i_iv
    ciphertext = b''

    for i in range(0, len(plaintext), block_size):
        #always pad the block, pad will do nothing if block is
        #of correct size (16)
        block = pad_block(plaintext[i:i+block_size], block_size)

        #encrypting the xor of the iv and the block
        iv = encrypt_aec(xor_bytes(iv, block), key)
        #what is the iv for the next block and what is added
        #to the ciphertext is the same
        ciphertext += iv

    return ciphertext

#decrypts using aec in cbc mode
def cbc_decryption(ciphertext, key, i_iv):
    iv = i_iv
    plaintext = b''

    for i in range(0, len(ciphertext), block_size):
        block = ciphertext[i:i+block_size]
        #decrypt, then xor with iv, then add to plaintext
        plaintext += unpad(xor_bytes(iv, decrypt_aec(block, key)))
        #iv for the next block is the original previous ciphertext
        iv = block

    return plaintext

if __name__ == "__main__":
    iv = b'\x00' * block_size
    encrypted = base64.b64decode(open("challenge10.txt", 'r').read())
    decrypted = cbc_decryption(encrypted, b'YELLOW SUBMARINE', iv)
    print(decrypted)
    #checking encryption function
    assert encrypted == cbc_encryption(decrypted, b'YELLOW SUBMARINE', iv)