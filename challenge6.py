'''
Cryptopals Set 1 Challenge 6
'''

import base64
from challenge3 import decrypt_single_byte_xor_cypher
from challenge5 import encrypt_repeating_xor

#calculates the hamming distance between two byte strings
#i.e. number of differing bits
def hamming_distance(a, b):
    xor = 0
    for byte_a, byte_b in zip(a, b):
        xor = (xor << 8) | (byte_a ^ byte_b)
    
    return bin(xor).count("1")

#finds repeating key from a base 64 file
def decrypt_b64_rpt_key(filename):
    #convert to bytes
    encrypted = base64.b64decode(open(filename, 'r').read())

    keysizes = []
    #find likely length of key
    #although this method is a little expensive, the more data is considered,
    #the more likely the length of key with the minimum distance is correct
    for ks in range(2, 41):
        dis = 0
        #take as many blocks of ks as possible, calculate the bit distance with all adjacent blocks
        max_blocks = len(encrypted) // ks - 2
        for i in range(max_blocks):
            dis += hamming_distance(encrypted[ks*i:ks*(i+1)], encrypted[ks*(i+1):ks*(i+2)]) / ks
        #append the ks and its average hammington distance
        keysizes.append((ks, dis / max_blocks))

    #sort and take the top keysizes
    keysizes.sort(key = lambda x: x[1])
    top_keysizes = [x[0] for x in keysizes[:3]]

    messages = []
    for t_ks in top_keysizes:
        blocks = []
        for i in range(t_ks):
            block = encrypted[i::t_ks] #take every t_ks-th byte from the i-th byte
            blocks.append(block)

        key = ""
        #construct the key by combining all single-byte keys from each block
        for block in blocks:
            key += decrypt_single_byte_xor_cypher(block)['key'] 
        
        #xor the key with the encryption to get the possible message
        message = encrypt_repeating_xor(key, encrypted).decode()
        messages.append((message, key))

    return messages

if __name__ == "__main__":
    assert hamming_distance(b"this is a test", b"wokka wokka!!!") == 37

    print(decrypt_b64_rpt_key('challenge6.txt')[0])