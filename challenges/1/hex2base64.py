#!/usr/bin/env python
""" This is for cryptopals challenge #1 Convert hex to base64

    Details:

    Convert hex to base64
    The string:

    49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d

    Should produce:

    SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t

    So go ahead and make that happen. You'll need to use this code for the rest of the exercises.

    Cryptopals Rule
    Always operate on raw bytes, never on encoded strings. Only use hex and base64 for pretty-printing.
"""

import binascii

hexString = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706" \
            "f69736f6e6f7573206d757368726f6f6d"
solution = "SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t"

result = binascii.b2a_base64(binascii.a2b_hex(hexString)).strip()

if result == solution:
    print "yup"

# for fun
print(binascii.a2b_hex(hexString))
