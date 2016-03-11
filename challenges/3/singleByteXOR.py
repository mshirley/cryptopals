#!/usr/bin/env python
""" This is for cryptopals challenge #3 Single Byte XOR Cipher

    Details:
    Single-byte XOR cipher
    The hex encoded string:

    1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736
    ... has been XOR'd against a single character. Find the key, decrypt
    the message.

    You can do this by hand. But don't: write code to do it for you.

    How? Devise some method for "scoring" a piece of English plaintext.
    Character frequency is a good metric. Evaluate each output and choose
    the one with the best score.

    Achievement Unlocked
    You now have our permission to make "ETAOIN SHRDLU" jokes on Twitter.
"""
import binascii
from string import ascii_lowercase
import json

# let's use these characters for our keys
#chars = ['1','2','3','4','5','6','7','8','9','0','a','b','c','d','e','f','g',
#         'h','i','j','k','l','n','m','n','o','p','q','r','s','t','u','v','w',
#         'x','y','z', 'A','B','C','D','E','F','G','H','I','J','K','L','N','M',
#         'N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

# i'm sorry, but fuck pep8 in regard to spaces between list elements!
#
# chars variable above is just as easy to read and takes up less space
charsPEP8 = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'a', 'b', 'c',
             'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'n', 'm', 'n', 'o',
             'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 
             'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'N', 'M', 'N', 
             'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
hexString = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393" \
            "b3736"
byteArray = bytearray(binascii.a2b_hex(hexString))
endArray = []

for c in charsPEP8:
    resultArray = []
    for b in byteArray:
        intResult = b ^ ord(c)
        resultArray.append(intResult)
    endArray.append({c:binascii.b2a_hex(bytearray(resultArray))})

scores = []
for a in endArray:
    indexChar = a.keys()[0]
    score = 0
    alphas = filter(lambda x: x.isalpha(), charsPEP8)
    testString = binascii.a2b_hex(a[indexChar])
    for c in testString:
        if c in alphas:
            score += 1
    scores.append({indexChar: {'score': score, 'string': testString}})
        
winner = {}
for s in scores:
    tmpChar = s.keys()[0]
    tmpString = s[tmpChar]['string']
    print(tmpString)
    tmpScore = s[tmpChar]['score']
    if not winner.has_key('score'):
        winner['score'] = 0
    if tmpScore > winner['score']:
        winner['score'] = tmpScore
        winner['char'] = tmpChar 
        winner['string'] = tmpString
# i can't figure out a way to cleanly print out winner['string']
print(json.dumps(winner, indent=4))
print(winner)

