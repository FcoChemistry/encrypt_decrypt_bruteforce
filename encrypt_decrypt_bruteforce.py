def chyper (plaintext, k):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    ciphertext = []
    for c in plaintext:
        i = alphabet.index(c)
        j = (i + k) % len(alphabet)
        ciphertext.append(alphabet[j])
    return "".join(ciphertext)

def decrypt(ciphertext, k):
    return chyper(ciphertext, -k)

def brute_forece(ciphertext):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for k in range(0,26):
        brute = chyper(ciphertext,-k)
        print(brute + " " + str(k))
    return
