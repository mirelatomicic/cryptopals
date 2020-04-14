'''
Cryptopals Set 1 Challenge 8
'''

#Score based on how many blocks are repeated
def score_reps(msg):
    score = 0
    for i in range(0, len(msg), 16):
        to_match = msg[i:i+16]
        for j in range(0, len(msg), 16):
            if (msg[j:j+16] == to_match) and (i != j):
                score += 1

    return score

#Finds from a file which hex string is likely to be ECB encrypted
def find_ecb_encoding(filename):
    with open(filename) as f:
        encryptions = f.read().splitlines()  

    scores = []

    for encryption in encryptions:
        msg = bytearray.fromhex(encryption)
        scores.append((score_reps(msg), encryption))    

    scores.sort(key = lambda x: x[0])

    return scores[-1]


if __name__ == "__main__":
    print(find_ecb_encoding("challenge8.txt"))

