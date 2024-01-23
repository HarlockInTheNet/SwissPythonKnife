#XOR Function Between 2 Numbers - They must be of the same length
def xor(a, b):
    if len(a) != len(b):
        raise Exception('Error in rule 1')
    return ''.join([str(int(a[i]) ^ int(b[i])) for i in range(len(a))])

#Driver code
print(xor('1010', '0101')) # 1111
#Remember that the XOR function is commutative, so the order doesn't matter
#Also, we can't XOR strings, so we have to convert them to binary

#XOR example between two words (already converted)
#key = ' '.join([chr(ord(x) ^ ord(y)) for x, y in zip(original_data, enc_data)])
