#!/usr/bin/env python
""" This is for cryptopals challenge #3 Single Byte XOR Cipher

    Details:
    Detect single-character XOR
    One of the 60-character strings in this file has been encrypted by single-character XOR.
    
    Find it.
    
    (Your code from #3 should help.)
"""
from singleByteXOR import execXOR, detectAlpha, createScores, options

fileName = 's1c4.txt'

# execute singleByteXOR on rows in file
tmpWinners = []
print("executing detectSingleByteXOR")
with open(fileName) as row:
    for r in row:
        print r.strip()
        options['hexString'] = r.strip()
        print("executing singleByteXOR")
        tmpWinners.append(createScores(options))

# flatten the winners list
winners = []
for w in tmpWinners:
    for sw in w:
        winners.append(sw)    

newWinners = sorted(winners, key=lambda k: k['score'], reverse=True) 
for nw in newWinners[1:10]:
    print nw

tmpWords = open('/usr/share/dict/words').readlines()
words = []
for tw in tmpWords:
    if len(tw) > 4:
        words.append(tw.strip())

for word in words:
    for w in winners:
        if word in w['string']:
            print("found word in string: {word} - {string}".format(word=word,string=w['string']))
            print w
