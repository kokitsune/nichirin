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
    def __str__(self):
        return self.original
    def get_key(self, stat, key):
        if stat == 'character':
            key = bin(ord(key))
        elif stat == 'num':
            key = bin(key)
        return '%8s'.replace(' ', '0') % key.replace('b', '')
    def encryption(self):
        '''
        It's both the encryption and decryption actually.
        '''
        self.encrypted = ''
        for longgong in self.original:
            temp = ''
            longgong = '%8s' % bin(ord(longgong)).replace('b', '')
            for tower, rook in zip(longgong.replace(' ', '0'), self.key):
                if tower == rook:
                    temp += '0'
                else:
                    temp += '1'
            print longgong.replace(' ', '0'), self.key
            self.encrypted += chr(int(temp, 2))
        return self.encrypted
    def decryption(self):
        '''
        A layout for other methods.
        '''
        pass


