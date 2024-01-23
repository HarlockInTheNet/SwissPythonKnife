# CyberSec

---

## Cryptograpy

### Legend
- Vigenere: The Vigenère cipher is a method of encrypting alphabetic text where each letter of the plaintext is encoded with a different Caesar cipher, whose increment is determined by the corresponding letter of another text, the key.

### Files
- crypto.py:  full file with all the function in the single file
- cesar.py
    - Simple Caesar Cipher function - brute force approach with a plaintext and a given shift
    - Caesar Cipher Decoding function - brute force approach with a ciphertext and a given shift
- vigenere.py
    - Vigenere Cipher function - brute force approach with a plaintext and a given key, modulo the key length also
    - Vigenere Cipher Decoder function - brute force approach with a ciphertext and a given key, modulo the key length also
- des.py
    - DES Encyption and Decryption Function - useful to implement the DES given a text, a key and a mode
        - Binary to text and text to binary
        - Split into 2 6bit blocks
        - Expand the block from 6 to 8 bits
        - XOR function between two binary strings and return the result as 8 bit binary string
        - Create S1 and S2
        - Encryption Function
        - Decrypt Function
- xor.py
    - XOR Function Between 2 Numbers - They must be of the same length
- md5hash.py
    - MD5 Hashing Algorithm
    - MD5 Reverse Hashing Algorithm - It probably won't work, cause its a bruteforce
- utils.py
    - Frequency Analysis function - useful when we have no information about the cipher text
    - Opening a file (no matter the extension) and reading it
    - Base64 Decoder function - useful in many instances

--- 

## Web Security

### Legend

### Files
- web.txt
    - Browser
    - Wireshark:
    - Fetch (usando curl):
    - SQL injection
---

## Reverse Engineering and Pwning

### Legend

### Files
