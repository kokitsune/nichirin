'''
Project ala Pegeant:
    Encryption and Decryption.
'''

from Tkinter import *
from os import *

class XOR(object):
    '''
    For operation concerning XOR method.
    Attribute : A sequence of character.
    '''
    def __init__(self, original='Default', key='00000000'):
        self.original = original
        self.key = key[-6:]
        self.key = '0'*(8-len(self.key))+self.key.replace('b', '')
    def __str__(self):
        return self.original
    def get_key(self, stat='bin', key='00000000'):#Maximum MUST be 00111111
        if stat == 'num':
            self.key = bin(key)
        else:
            self.key = key
        self.key = key[-6:]
        self.key = '0'*(8-len(self.key))+self.key.replace('b', '')
        return self.key
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
    def save(self, filename='untitled'):
        text = open('%s.txt' % filename, 'w')
        text.write(self.key)
        text.write('834longgong567')
        text.write(self.encrypted)
    def load(self, filename='untitled'):
        text = open('%s.txt' % filename, 'r')
        self.key, self.encrypted = tuple(text.read().split('834longgong567'))
        

class CipherDisk(object):
    '''
    For operation concerning Cipher Disk method.
    Attribute: A sequence of character, number of turns
    '''
    def __init__(self, original='Default', turn=1, disk=None):
        self.original = original
        self.turn = turn
        if disk == None:
            self.disk = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    def disk_tuning(self, position, char):
        if position >= len(self.disk):
            self.disk.append(char.upper())
        elif char == 'delete':
            self.disk.pop(position)
        else:
            self.disk[position] = char.upper()
        return self.disk
    def encryption(self):
        self.encrypted = ''
        for longgong in self.original:
            if longgong in self.disk:
                self.encrypted += self.disk[(self.disk.index(longgong)+self.turn)%len(self.disk)]
            elif longgong.upper() in self.disk:
                self.encrypted += self.disk[(self.disk.index(longgong.upper())+self.turn)%len(self.disk)].lower()
            else:
                self.encrypted += longgong
        return self.encrypted
    def decryption(self):
        self.decrypted = ''
        for longgong in self.original:
            if longgong in self.disk:
                self.decrypted += self.disk[abs(self.disk.index(longgong)-self.turn)%len(self.disk)]
            elif longgong.upper() in self.disk:
                self.decrypted += self.disk[abs(self.disk.index(longgong.upper())-self.turn)%len(self.disk)].lower()
            else:
                self.decrypted += longgong
        return self.decrypted
    def save(self, filename='untitled', pathname=''):
        text = open('%s.txt' % filename, 'w')
        text.write(self.key)
        text.write('834longgong567')
        text.write(self.encrypted)
    def load(self, filename='untitled'):
        text = open('%s.txt' % filename, 'r')
        self.key, self.encrypted = tuple(text.read().split('834longgong567'))
    
class GUI:
    def __init__(self):
        self.root = Tk()
        self.root.geometry('{}x{}'.format(250, 250))
        self.root.title('uDEncrypt')
        Label(self.root, text='Welcome to uEncrypt 2000').grid(row=0)
        Label(self.root, text='Please select any type of encryption to begin').grid(row=400)
        Button(self.root, text="      XOR Encryption/Decryption      ", command=self.test).grid(row=500)
        Button(self.root, text="      CipherDisk Encryption/Decryption      ", command=self.test).grid(row=600)
        Button(self.root, command=self.root.quit, text='Exit').grid(row=700)
        ##Spaces are disgraces//
        Label(self.root, text='').grid(row=401)
        Label(self.root, text='').grid(row=501)
        Label(self.root, text='').grid(row=601)
        Label(self.root, text='').grid(row=602)
        Label(self.root, text='').grid(row=402)
        Label(self.root, text='').grid(row=0)
        ##End of disgraces//
        self.root.mainloop()
        

    def test(self):
        print 'gong'

gui = GUI()
