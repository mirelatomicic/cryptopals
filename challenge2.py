'''
Cryptopals Set 1 Challenge 2
'''
encode_hex = "0123456789abcdef"

def two_hex_string_xor(a, b):
    assert len(a) == len(b) 
    xor_str = ""

    for charA, charB in zip(a, b):
        xor_str += encode_hex[int(charA, 16) ^ int(charB, 16)]
    
    return xor_str

if __name__ == "__main__":
    assert two_hex_string_xor("1c0111001f010100061a024b53535009181c", "686974207468652062756c6c277320657965") == "746865206b696420646f6e277420706c6179"