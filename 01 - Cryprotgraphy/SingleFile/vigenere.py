#Vigenere Cipher function - brute force approach with a plaintext and a given key, modulo the key length also
def vigenereCipher(plainText, key):
    cipherText = ""
    for i in range(len(plainText)):
        if plainText[i].isupper():
            cipherText += chr((ord(plainText[i]) + ord(key[i % len(key)]) - 65) % 26 + 65) #65 is the ASCII value of 'A' and 26 is the number of letters in the alphabet
        else:
            cipherText += chr((ord(plainText[i]) + ord(key[i % len(key)]) - 97) % 26 + 97) #97 is the ASCII value of 'a' and 26 is the number of letters in the alphabet
    return cipherText

#Driver code
print(vigenereCipher("Hello World", "key"))

#Vigenere Cipher Decoder function - brute force approach with a ciphertext and a given key, modulo the key length also
def vigenereCipherDecoder(cipherText, key):
    plainText = ""
    for i in range(len(cipherText)):
        if cipherText[i].isupper():
            plainText += chr((ord(cipherText[i]) - ord(key[i % len(key)]) - 65) % 26 + 65) #65 is the ASCII value of 'A' and 26 is the number of letters in the alphabet
        else:
            plainText += chr((ord(cipherText[i]) - ord(key[i % len(key)]) - 97) % 26 + 97) #97 is the ASCII value of 'a' and 26 is the number of letters in the alphabet
    return plainText