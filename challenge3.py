'''
Cryptopals Set 1 Challenge 3
'''
#originally used frequencies taken from wikipedia...
'''
FREQ = {'a' : 0.08167, 'b' : 0.01492, 'c' : 0.02202, 'd' : 0.04353,
        'e' : 0.12702, 'f' : 0.02228, 'g' : 0.02015, 'h' : 0.06094,  
        'i' : 0.06966, 'j' : 0.00153, 'k' : 0.01292, 'l' : 0.04025,
        'm' : 0.02406, 'n' : 0.06749, 'o' : 0.07507, 'p' : 0.01929,
        'q' : 0.00095, 'r' : 0.05987, 's' : 0.06327, 't' : 0.09356,
        'u' : 0.02758, 'v' : 0.00978, 'w' : 0.02560, 'x' : 0.00150,
        'y' : 0.01994, 'z' : 0.00077     
        }
'''
#...but needed spaces, otherwise long strings of gibberish vowels tended to win
FREQ = {
    'a': 0.0651738, 'b': 0.0124248, 'c': 0.0217339, 'd': 0.0349835,
    'e': 0.1041442, 'f': 0.0197881, 'g': 0.0158610, 'h': 0.0492888,
    'i': 0.0558094, 'j': 0.0009033, 'k': 0.0050529, 'l': 0.0331490,
    'm': 0.0202124, 'n': 0.0564513, 'o': 0.0596302, 'p': 0.0137645,
    'q': 0.0008606, 'r': 0.0497563, 's': 0.0515760, 't': 0.0729357,
    'u': 0.0225134, 'v': 0.0082903, 'w': 0.0171272, 'x': 0.0013692,
    'y': 0.0145984, 'z': 0.0007836, ' ': 0.1918182 
}

#Returns the most likely message decryption of a 
#byte array that has been xor'd against a single byte,
#along with it's respective key and score 
def decrypt_single_byte_xor_cypher(byte_array):
    '''
    try: 
        byte_array = bytes.fromhex(hex_str)
    except:
        return -1
    '''

    decryptions = {}
    for key in range(256):
        decrypted = b''
        for byte in byte_array:
            #note to self: a byte in a byte array is of type int
            #conversion from int to byte is bytes([an_int])
            decrypted += bytes([byte ^ key])

        decryptions[key] = score_by_freq(decrypted)

    top_result = sorted(decryptions.items(), key=lambda x_y: x_y[1]['score'], reverse=True)[0]

    return {
        'key' : chr(top_result[0]),
        'message' : top_result[1]['message'],
        'score' : top_result[1]['score']
    }
    
 

#Returns the score and the acccompanying message as a string
#together in a dictionary. Scoring using char frequencies.          
def score_by_freq(msg):
    score = 0
    msg_str = ""
    for byte in msg:
        try:  #try block incase character isn't covered by freq table
            score += FREQ[chr(byte).lower()]
            msg_str += chr(byte)
        except:
            msg_str += chr(byte)
    return {'score' : score, 'message': msg_str}    

if __name__ == "__main__":
    print(decrypt_single_byte_xor_cypher(bytes.fromhex("1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736")))