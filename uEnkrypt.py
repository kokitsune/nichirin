'''
Project ala Pegeant:
    Encryption and Decryption.
'''
from Tkinter import *

class XOR(object):
    '''
    For operation concerning XOR method.
    Attribute : A sequence of character.
    '''
    def __init__(self, original):
        self.original = original
        self.encrypted = ''
    def __str__(self):
        return self.original
    def get_key(self, stat, key):
        if stat == 'character':
            key = bin(ord(key))
        elif stat == 'num':
            key = bin(key)
        return key.replace('b', '')
    def encryption(self):
        for longgong in self.original:
            temp = ''
            for tower, rook in zip(bin(ord(longgong)).replace('b', ''), self.key):
                if tower == rook:
                    temp += '0'
                else:
                    temp += '1'
            print temp
            self.encrypted += chr(int(temp, 2))
        return self.encrypted
# Eh...Mac if you do see this. Please make the resulting binaries
#length from 7 to 8 please.
