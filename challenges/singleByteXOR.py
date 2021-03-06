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
import itertools

options = {}

# let's use these characters for our keys
#chars = ['1','2','3','4','5','6','7','8','9','0','a','b','c','d','e','f','g',
#         'h','i','j','k','l','n','m','n','o','p','q','r','s','t','u','v','w',
#         'x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','N','M',
#         'N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

# i'm sorry, but fuck pep8 in regard to spaces between list elements!
#
# chars variable above is just as easy to read and takes up less space
#
options['charsPEP8'] = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'a',
                        'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
                        'n', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
                        'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G',
                        'H', 'I', 'J', 'K', 'L', 'N', 'M', 'N', 'O', 'P', 'Q',
                        'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
#options['charsPEP8'] = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'N', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
#                        '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'a',
#                        'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
#                        'n', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
#                        'w', 'x', 'y', 'z', 
                        
#options['charsPEP8'] = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'n', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

options['hexString'] = "1b37373331363f78151b7f2b783431333d78397828372d363c7" \
                       "8373e783a393b3736"

def somethingNew(options):
    byteArray = bytearray(binascii.a2b_hex(options['hexString']))
    

def newExecXOR2(options):
    result = {}
    byteArray = bytearray(binascii.a2b_hex(options['hexString']))
    for i in range(0,len(byteArray)):
        for c in options['charsPEP8']:
            if c not in result:
                result[c] = []
            positionInt = byteArray[i] ^ ord(c)
            result[c].append(chr(positionInt))

    result_array = []
    another_array = []
    for l in options['charsPEP8']:
        for i in range(0,len(byteArray)):
            result_array.append(result[l][i])
        another_array.append(''.join(result_array))
        result_array = []

        #print ''.join(first_array)
        #if len(first_array) > 1:
        #    final_array.append(''.join(first_array))
        #print final_array
        # let's iterate over each deciphered string and see if it's alpha
    #    lookup_tuple = i  
    #    print lookup_tuple
    #    print type(lookup_tuple)
    #    for e in lookup_tuple:
    #        print "e is " + e
    #        print result[e]
    #        my_array.append(result[e])
    #        print my_array
    #        print "end of first loop"
    #    my_array = []
    #
    return another_array

def newExecXOR(options):
    #result = {}
    byteArray = bytearray(binascii.a2b_hex(options['hexString']))
    #for i in range(0,len(byteArray)):
    #    print i
    #    for c in options['charsPEP8']:
    #        if c not in result:
    #            result[c] = []
    #        positionInt = byteArray[i] ^ ord(c)
    #        result[c].append(chr(positionInt))
    #print "finished, len: {length}".format(length=len(result))
    completed = False
    #my_array = []
    final_array = []
    high_score = 0
    score = 0
    alphas = filter(lambda x: x.isalpha(), options['charsPEP8'])
    for key in itertools.product(options['charsPEP8'],
                               repeat=len(byteArray)):
        key = list(reversed(list(key)))
        first_array = []
        stopit = False
        for index, letter in enumerate(key):
            if stopit == False:
                my_char = chr(ord(letter) ^ byteArray[index])
        #        if my_char.isalpha() is False:
        #            print "stop it"
        #            stopit = True
        #        else:
                first_array.append(my_char)
        for c in first_array:
            if c in alphas:
                score += 1

        if score > high_score:
            print "new high_score: {score}, string: {string}".format(score=score, string=''.join(first_array))
            high_score = score
            score = 0

        score = 0

        #print ''.join(first_array)
        #if len(first_array) > 1:
        #    final_array.append(''.join(first_array))
        #print final_array
        # let's iterate over each deciphered string and see if it's alpha
    #    lookup_tuple = i  
    #    print lookup_tuple
    #    print type(lookup_tuple)
    #    for e in lookup_tuple:
    #        print "e is " + e
    #        print result[e]
    #        my_array.append(result[e])
    #        print my_array
    #        print "end of first loop"
    #    my_array = []
    #
    return final_array
            
 
def execXOR(options):
    endArray = []
    # create a byte array from the hexstring
    byteArray = bytearray(binascii.a2b_hex(options['hexString']))
    
    print("input hexString: {hs}".format(hs=options['hexString']))
    print("executing XOR against input ciphertext byte array and"
          " alpha char key")
    for c in options['charsPEP8']:
        resultArray = []
        # iterate over the byte array, XOR, and store the result
        for b in byteArray:
            intResult = b ^ ord(c)
            resultArray.append(intResult)
        # convert bytearray to hex chars and store
        endArray.append({c: binascii.b2a_hex(bytearray(resultArray))})
    return endArray


def detectAlpha(options, endArray):
    print("executing alpha char detection against deciphered char")
    scores = []
    # iterate over all XOR'd strings and calculate a score
    for a in endArray:
        indexChar = a.keys()[0]
        score = 0
        testString = binascii.a2b_hex(a[indexChar])
        # create a new list of alpha chars from list of alphanums
        alphas = filter(lambda x: x.isalpha(), options['charsPEP8'])
        # let's iterate over each deciphered string and see if it's alpha
        for c in testString:
            if c in alphas:
                score += 1
        # create list of scored key chars
        scores.append({'char': indexChar, 'score': score, 'string': testString})
    for s in scores:
        print s
    return scores


def createScores(options):
    endArray = execXOR(options)
    scores = detectAlpha(options, endArray)
    # get iterable of scores
    testScore = [x['score'] for x in scores]
    # get the maximum value of all scores
    maxScore = max(testScore)
    winners = []
    # check for scores that are equal and consider them the same
    for s in scores:
        if s['score'] == maxScore:
            winners.append(s)
    return winners 

def main():
    print("executing singleByteXOR")
    scores = createScores(options)
    print("results:")
    for s in scores:
        print(s)

if __name__ == "__main__":
    main()
