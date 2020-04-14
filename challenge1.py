'''
Cryptopals Set 1 Challenge 1
Main point: Work directly on bytes
'''

encode_base64 = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"

#convert hex string to base64 string
def hex_to_base64(hex_str):
    b64_str = ""
    buffer = 0
    buffer_length = 0

    for char in hex_str:
        decimal = int(char, 16) #convert to 4 byte int

        if buffer_length == 0:
            buffer = decimal
            buffer_length = 4

        elif buffer_length == 4:
            buffer = (buffer << 2) | (decimal >> 2)
            b64_str += encode_base64[buffer]
            buffer = (decimal & 0x3)
            buffer_length = 2

        elif buffer_length == 2:
            buffer = (buffer << 4) | (decimal)
            b64_str += encode_base64[buffer] 
            buffer = 0
            buffer_length = 0

    if buffer_length == 2:
        buffer = (buffer << 4)
        b64_str += encode_base64[buffer]
        #b64_str += "=="

    elif buffer_length == 4:
        buffer = (buffer << 2)
        b64_str += encode_base64[buffer]
        #b64_str += "="

    return b64_str

if __name__ == "__main__":
    #given test
    assert hex_to_base64("49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d") \
            == "SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t"