import encryption as enc
import decryption as dec

e = enc.Enc()
d = dec.Dec()

plaintext = "10111010"
cipherKey = "1011100110"
print("\nPlain Text: ", plaintext)
print("\nCipher Key: ", cipherKey)

cipher = e.encrypt(plaintext, cipherKey)

print("\nEncrypted Cipher Text: ", cipher)

decrypted = d.decrypt(cipher, cipherKey)

print("\nDecrypted Plain Text: ", decrypted)