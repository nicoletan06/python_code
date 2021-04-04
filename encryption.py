def caesar_encrypt(plaintext, shift_amt):
    ciphertext = ''
    for ch in plaintext:
        if ch.isupper():
            ciphertext += chr((ord(ch) - ord('A') + shift_amt) % 26 + ord('A'))
        elif ch.islower():
            ciphertext += chr((ord(ch) - ord('a') + shift_amt) % 26 + ord('a'))
        else:
            ciphertext += ch
    return ciphertext

def caesar_decrypt(ciphertext, shift_amt):
    plaintext = ''
    for ch in ciphertext:
        if ch.isupper():
            plaintext += chr((ord(ch) - ord('A') - shift_amt + 26) % 26 + ord('A'))
        elif ch.islower():
            plaintext += chr((ord(ch) - ord('a') - shift_amt + 26) % 26 + ord('a'))
        else:
            plaintext += ch
    return plaintext

ct = caesar_encrypt('Stony Brook', 2)
print(ct)
pt = caesar_decrypt('Uvqpa Dtqqm', 2)
print(pt)