#!/usr/bin/env python
""" This is for cryptopals challenge #2 Fixed XOR

    Details:

    Fixed XOR
    Write a function that takes two equal-length buffers and produces their
    XOR combination.

    If your function works properly, then when you feed it the string:

    1c0111001f010100061a024b53535009181c
    ... after hex decoding, and when XOR'd against:

    686974207468652062756c6c277320657965
    ... should produce:

    746865206b696420646f6e277420706c6179
"""
import binascii

hexString1 = "1c0111001f010100061a024b53535009181c"
hexString2 = "686974207468652062756c6c277320657965"
solution = "746865206b696420646f6e277420706c6179"

intResult = int(hexString1, 16) ^ int(hexString2, 16)
hexResult = "{:x}".format(intResult)

if hexResult == solution:
    print("yup")

# for fun
print(binascii.a2b_hex(hexString1))
print(binascii.a2b_hex(hexString2))
print(binascii.a2b_hex(hexResult))
