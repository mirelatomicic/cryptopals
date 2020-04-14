'''
Cryptopals Set 2 Challenge 9
'''

def pad_block(block, length):
    padding = length - len(block)
    padded_block = block
    for i in range(padding):
        padded_block += bytes([padding])
    
    return padded_block

def is_padded(plaintext):
    padding = plaintext[-plaintext[-1]:]
    return all(byte == len(padding) for byte in padding)

def unpad(plaintext):
    if is_padded(plaintext):
        return plaintext[:-plaintext[-1]]
    return plaintext

if __name__ == "__main__":
    print(pad_block(b'YELLOW SUBMARINE', 20))
    print(unpad(pad_block(b'YELLOW SUBMARINEEE', 20)))