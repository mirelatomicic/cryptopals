'''
Cryptopals Set 1 Challenge 4
'''
from challenge3 import decrypt_single_byte_xor_cypher

def find_xor_cypher_str(filename):
    file1 = open(filename, 'r') 
    encrypted_strs = file1.readlines() 
    decyrpted_strs = []

    for encrypted_str in encrypted_strs:
        #need to strip newlines
        decyrpted_strs.append(decrypt_single_byte_xor_cypher(bytes.fromhex(encrypted_str.strip())))

    return sorted(decyrpted_strs, key = lambda i: i['score'], reverse=True)[0]

if __name__ == "__main__":
    print(find_xor_cypher_str('challenge4.txt'))