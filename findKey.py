# Virginia Williams
# 10/15/2021
# Program to determine the key used in a aes-128-cbc encrypted file given plain text, cipher text,
# IV, and the fact that the key is a less than 16 character English word.
# Sources used:
# https://github.com/li-xin-yi/seedlab/blob/master/Secret-Key-Encryption/README.MD
# - I used this source mostly as a template for the for loop to search through each word
# - The rest of the program, and some parts within the loop, I came up with as they were different
#
# TO RUN:
# python3 findKey.py
# I had trouble with Crypto not existing and had to run in a python env so I could install
# pycryptodome on the flip servers.  I don't know if this will affect how the grader will have
# to runs it or not.
# Also words.txt must be in same directory

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from sys import argv


# Set known values as strings"
ivString = "00000000000000000000000000000000"
plain = "This is a top secret."
cipher = "8d20e5056a8d24d0462ce74e4904c1b513e10d1df4a2ef2ad4540fae1ca0aaf9"

# Convert the known values from strings to bytearrays
plaintext = bytearray(plain, encoding='utf-8')
ciphertext = bytearray.fromhex(cipher)
iv = bytearray.fromhex(ivString)

# Open word list
with open('./words.txt') as f_in:
    words = f_in.readlines()

# Loop words until we find a match
for w in words:
    w = w.rstrip('\n')
    if len(w) <= 16:
        key = w + ' '*(16-len(w))
        newcipher = AES.new(key=bytearray(key,encoding='utf-8'), mode=AES.MODE_CBC, iv=iv)
        temp = newcipher.encrypt(pad(plaintext, 16))
        if temp == ciphertext:
            print("Key: ", key)
            exit(0)

print("uh oh")

