'''
Project ala Pegeant:
    Encryption and Decryption.
'''
from Tkinter import *

class App(object):
    """
    Simple Interface. It might change later.
    """
    def __init__(self, master):
        frame = Frame(master)
        frame.pack()
        
        self.label = Label(root, text='uEnkrypt')
        self.label.pack()

        self.label = Label(root, text='Choose your mode')
        self.label.pack()
        
        self.button = Button(root, text='XOR Mode')
        self.button.pack()

        self.button = Button(root, text='Cypher Mode')
        self.button.pack()

        self.button = Button(root, command=frame.quit, text='Exit')
        self.button.pack()
        
root = Tk()

app = App(root)

root.mainloop()
root.destroy()
    
class XOR(object):
    '''
    For operation concerning XOR method.
    Attribute : A sequence of character.
    '''
    def __init__(self, original='Default', key='00000000'):
        self.original = original
        self.key = '0'*(8-len(key))+key.replace('b', '')
    def __str__(self):
        return self.original
    def get_key(self, stat='bin', key='00000000'):#Maximum MUST be 01111111
        if stat == 'character':
            self.key = bin(ord(key))
        elif stat == 'num':
            self.key = bin(key)
        self.key = key
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
        text.write('834567')
        text.write(self.encrypted)
    def load(self, filename='untitled'):
        text = open('%s.txt' % filename, 'r')
        self.key, self.encrypted = tuple(text.read().split('834567'))
        

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
        pass



































