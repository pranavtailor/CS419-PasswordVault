
# hash function
def hash_code(key):
    return ''

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