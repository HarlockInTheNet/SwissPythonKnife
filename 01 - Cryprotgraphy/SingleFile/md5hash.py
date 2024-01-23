#MD5 Hashing Algorithm
import hashlib
def md5hashing(text):
    hash_object = hashlib.md5(text.encode())
    print(hash_object.hexdigest())

#Driver Code
md5hashing('Min0n!')

#MD5 Reverse Hashing Algorithm - It probably won't work, cause its a bruteforce
#of all the possible combinations of characters on a hash, so it can be an infinite runtime
import hashlib
def md5reversehashing(text):
    for i in range(0, 100000000): # 100000000 is the number of possible combinations
        hash_object = hashlib.md5(str(i).encode()) # convert the number to a string and encode it
        if hash_object.hexdigest() == text: # if the hash is equal to the text
            print(i) # print the number
            break
#Driver Code
md5reversehashing('e10adc3949ba59abbe56e057f20f883e') # 123456
#md5reversehashing('365d38c60c4e98ca5ca6dbc02d396e53') # This one coming from the challenges is not working