import hashlib

def hash_file(filename):

   # make a hash object
   h = hashlib.sha1()

   # open file for reading in binary mode
   with open(filename,'rb') as file:

       # loop till the end of the file
       chunk = 0
       while chunk != b'':
           # read only 1024 bytes at a time
           chunk = file.read(4096)
           h.update(chunk)

   # return the hex representation of digest
   return h.hexdigest()

message = hash_file("README.md")
print(message)