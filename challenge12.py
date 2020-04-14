'''
Cryptopals Set 2 Challenge 12
'''
import os
import base64
from challenge7 import encrypt_aec
from challenge8 import score_reps

key = os.urandom(16)
unknown_string = base64.b64decode(open("challenge12.txt", 'r').read())

def unknown_encryption(plaintext):
    return encrypt_aec(plaintext + unknown_string, key)

#find the unknown string with repeated calls to the encryption
def find_unknown_string():
    #find block size by adding characters until the length changes
    original_len = len(unknown_encryption(b'A'))
    i = 2
    while original_len == len(unknown_encryption(b'A' * i)):
        i += 1
    block_size = len(unknown_encryption(b'A' * i)) - original_len

    #confirm it is ECB
    if score_reps(unknown_encryption(b'A' * 2 * block_size)) == 0:
        return -1

    #find the string
    string = b''

    #amount of blocks in original message
    blocks = int(len(unknown_encryption(b'')) / block_size)

    #get the blocks of the message one by one
    for block in range(blocks):
        #loop the buffer to decrease in size, which resets when whole block is found
        for i in range(1, block_size + 1):
            buffer = b'A' * (block_size - i) 
            #the 'actual' is the current block of interest of the ciphertext with the buffer as input
            actual = unknown_encryption(buffer)[block*block_size:block*block_size + block_size]

            #loop through all possible bytes
            for byte in range(0, 127):
                #we add our guessed byte to an input such that our input is (buffer + known_part_of_string + guessed_byte)
                #in our 'actual' the input can be seen as (buffer + known_part_of_string + unknown_byte)
                #if output(buffer + known_part_of_string + guessed_byte) == output(buffer + known_part_of_string + unknown_byte)
                #it is clear we have found the next byte of the string (guessed_byte == unknown_byte)
                if actual == unknown_encryption(buffer + string + bytes([byte]))[block*block_size:block*block_size + block_size]:
                    string += bytes([byte])
                    break

    return string    

if __name__ == "__main__":
    print(find_unknown_string())