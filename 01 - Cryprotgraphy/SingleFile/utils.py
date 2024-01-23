#Frequency Analysis function - useful when we have no information about the cipher text
def frequencyAnalysis(cipherText):
    freq = {}
    for i in cipherText:
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1
    return freq

#Driver code
print(frequencyAnalysis("Hello World"))


#Opening a file (no matter the extension) and reading it
def openfile(filename):
    with open(filename, 'r') as file: #alternatively, we can use 'rb' for binary files
        data = file.read().replace('\n', '') # read the file and replace the new line character with nothing
    return data

#Driver Code
#openfile('test.txt')


#Base64 Decoder function - useful in many instances

import base64
def base64Decoder(cipherText):
    plainText = base64.b64decode(cipherText).decode('utf-8', errors='ignore')
    return plainText

#Driver code
print(base64Decoder("SGVsbG8gV29ybGQ="))