'''
Cryptopals Set 2 Challenge 14
'''
import random
import os
import base64
from challenge7 import encrypt_aec
from challenge8 import score_reps

key = os.urandom(16)
unknown_string = base64.b64decode(open("challenge12.txt", 'r').read())
prefix = os.urandom(random.randint(1,100))

def oracle(plaintext):
    return encrypt_aec(prefix + plaintext + unknown_string, key)

def find_unknown_string():
    #find block size by adding characters until the length changes
    original_len = len(oracle(b'A'))
    i = 2
    while original_len == len(oracle(b'A' * i)):
        i += 1
    block_size = len(oracle(b'A' * i)) - original_len

    #find prefix offset (how many characters off a rounded 'block')
    #make the input 'A' for 2 full blocks, and insert an offset until 
    #a repetition is found in the encryption (the 2 groups of 'A' are now flush)
    prefix_offset = 0
    detect_rep = oracle(b'A' * 2 * block_size + b'A' * prefix_offset)
    while score_reps(detect_rep) == 0:
        prefix_offset += 1
        detect_rep = oracle(b'A' * 2 * block_size + b'A' * prefix_offset)

    #so now just need to find in which 'block' the repetition started
    rep_block = 0
    while detect_rep[rep_block*block_size:rep_block*block_size+block_size] != detect_rep[(rep_block+1)*block_size:(rep_block+1)*block_size+block_size]:
        rep_block += 1

    prefix_buff = b'A' * prefix_offset

    #find the string
    string = b''

    #amount of blocks when no input is put in
    blocks = int(len(oracle(b'')) / block_size)

    #get the blocks of the message one by one, working from the first block prefix doesn't affect
    for block in range(rep_block, blocks + 1):
        #loop the buffer to decrease in size, which resets when whole block is found
        for i in range(1, block_size + 1):
            buffer = prefix_buff + b'A' * (block_size - i) 
            #the 'actual' is the current block of interest of the ciphertext with the buffer as input
            actual = oracle(buffer)[block*block_size:block*block_size + block_size]

            #loop through all possible bytes
            for byte in range(0, 127):
                #we add our guessed byte to an input such that our input is (buffer + known_part_of_string + guessed_byte)
                #in our 'actual' the input can be seen as (buffer + known_part_of_string + unknown_byte)
                #if output(buffer + known_part_of_string + guessed_byte) == output(buffer + known_part_of_string + unknown_byte)
                #it is clear we have found the next byte of the string (guessed_byte == unknown_byte)
                if actual == oracle(buffer + string + bytes([byte]))[block*block_size:block*block_size + block_size]:
                    string += bytes([byte])
                    break

    return string

if __name__ == "__main__":  
    print(find_unknown_string())
    