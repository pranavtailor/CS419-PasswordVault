
# hash function
def hash_code(key):
    a = 63689
    b = 378551
    hash = 0

    for i in range(len(key)):
        hash = hash * a + ord(key[i])
        a = a * b
    
    return str(hash % 11869930968749383363)


def encode_vigenere_cipher(text, key):
    encoded = ''

    for i in range(len(text)):
        encoded = encoded + chr((ord(text[i]) + ord(key[i % len(key)])) % 128)

    return encoded

def decode_vigenere_cipher(encoded, key):
    text = ''

    for i in range(len(encoded)):
        text = text + chr((ord(encoded[i]) + 128 - ord(key[i % len(key)])) % 128)

    return text