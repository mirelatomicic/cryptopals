'''
Cryptopals Set 2 Challenge 13
'''
import os
from challenge7 import encrypt_aec, decrypt_aec
from challenge9 import pad_block
block_size = 16
key = os.urandom(block_size)

def parse(cookie):
    data = {}
    elems = cookie.split('&')
    for elem in elems:
        info = elem.split('=')
        data[info[0]] = info[1]

    return data

#
def profile_for(email):
    email = email.replace('&', '')
    email = email.replace('=', '')

    u_id = 10
    role = "user"
    profile = "email=" + email + "&u_id=" + str(u_id) + "&role=" + role
    return encrypt_aec(str.encode(profile), key)

def get_profile_info(profile):
    return(parse(decrypt_aec(profile, key).decode()))


if __name__ == "__main__":
    #first, get the encryption such that ...role=|... 
    #then cut off the last block
    to_modify = profile_for("fake@fke.com")[:block_size*2]
    #get a block [admin+padding]
    admin_block = pad_block(b'admin', block_size).decode()
    # ...role=|(adminblock encrypted)|
    to_modify += profile_for("fake@email" + admin_block)[block_size:block_size*2]
    #success!
    print(get_profile_info(to_modify))