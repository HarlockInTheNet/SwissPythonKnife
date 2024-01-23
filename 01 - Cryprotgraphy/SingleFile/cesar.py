#Simple Caesar Cipher function - brute force approach with a plaintext and a given shift

def caesarCipher(plainText, shift):
    cipherText = ""
    for i in range(len(plainText)):
        if plainText[i].isupper():
            cipherText += chr((ord(plainText[i]) + shift - 65) % 26 + 65) #65 is the ASCII value of 'A' and 26 is the number of letters in the alphabet
        else:
            cipherText += chr((ord(plainText[i]) + shift - 97) % 26 + 97) #97 is the ASCII value of 'a' and 26 is the number of letters in the alphabet
    return cipherText

#Driver code
print(caesarCipher("Hello World", 5))

#Caesar Cipher Decoding function - brute force approach with a ciphertext and a given shift
def caesarCipherDecoder(cipherText, shift):
    plainText = ""
    for i in range(len(cipherText)):
        if cipherText[i].isupper():
            plainText += chr((ord(cipherText[i]) - shift - 65) % 26 + 65) #65 is the ASCII value of 'A' and 26 is the number of letters in the alphabet
        else:
            plainText += chr((ord(cipherText[i]) - shift - 97) % 26 + 97) #97 is the ASCII value of 'a' and 26 is the number of letters in the alphabet
    return plainText