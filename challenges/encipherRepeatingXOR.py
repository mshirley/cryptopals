import binascii

def encipherRepXOR(plaintext, key):
    result = bytearray()
    key_index = 0
    key_max_index = len(key) - 1
    print key_max_index
    while key_index < key_max_index:
        print key_index
        for b in plaintext:
            result.append(b ^ key[key_index])    
        key_index += 1
    return result

if __name__ == "__main__":
    plaintext = bytearray("Burning 'em, if you ain't quick and nimble I go crazy when I hear a cymbal")
    key = bytearray("ICE")
    print binascii.b2a_hex(encipherRepXOR(plaintext, key))
