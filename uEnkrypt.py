'''
Project ala Pegeant:
    Encryption and Decryption.
'''

from Tkinter import *
import os

class XOR:
    '''
    For operation concerning XOR method.
    Attribute : A sequence of character.
    '''
    def __init__(self, original='Default', key='00000000'):
        self.root = Tk()
        self.root.resizable(width=FALSE, height=FALSE)
        self.root.geometry('{}x{}'.format(300, 320))
        self.root.title('XOR Cipher')
        Label(self.root, text='   XOR cipher uses its namesake logic gate     ').grid(row=1)
        Label(self.root, text='           to switch binary from 0 to 1 and vice versa.           ').grid(row=2)
        self.original = StringVar()
        Entry(self.root, textvariable=self.original).grid(row=4,padx=20,pady=20,columnspan=100, rowspan=100, sticky=W+E+N+S)
        Button(self.root, text="      Back      ", command=self.quitting).grid(row=200)

        #Non UI zone
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
    def quitting(self):
        global opening
        opening = False
        self.root.destroy()
        

class CipherDisk:
    '''
    For operation concerning Cipher Disk method.
    Attribute: A sequence of character, number of turns
    '''
    def __init__(self, original='Default', turn=1, disk=None):
        self.root = Tk()
        self.root.resizable(width=FALSE, height=FALSE)
        self.root.geometry('{}x{}'.format(300, 320))
        self.root.title('CipherDisk Encryption/Decryption')

        #None UI zone
        self.original = original
        self.turn = turn
        if disk == None:
            self.disk = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    def disk_tuning(self, position, char, mode=''):
        if char in self.disk and not mode == 'delete':
            Popup('Achtung!', 'Attention : This Character is already in the disk', 'Please refrain from confusing the cryptographer.')
        elif position >= len(self.disk):
            self.disk.append(char.upper())
        elif char == 'delete':
            self.disk.pop(position)
        elif mode == 'delete':
            self.disk.pop(self.disk.index(char))
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
    def quitting(self):
        global opening
        opening = False
        self.root.destroy()

def save(self,filename='untitled'):
    text = open('%s.txt' % filename, 'w')
    text.write(self.key)
    text.write('8151321542334longgong5789546512367')
    text.write(self.encrypted)

def load(filename='untitled'):
    text = open('%s.txt' % filename, 'r')
    return tuple(text.read().split('8151321542334longgong5789546512367'))

class AutoDetect:
    def __init__(self, filename):
        try:
            me = load(filename)
            if len(me[0]) == 8:
                for i in range(len(me[0])):
                    if not me[0][i] in '01':
                        stat = None
                    elif i == 7:
                        stat = 'bin'
            else:
                stat = None
        except(IOError):
            Popup('Achtung!', 'Attention : No such files specified.')


class Popup():
    def __init__(self, title='Insert something amusing here.', message='This message is intentionally left blank, I guess...', message2='', message3=''):
        self.root = Tk()
        self.root.title(title)
        self.root.resizable(width=FALSE, height=FALSE)
        Label(self.root, text='%s%s%s' % (' '*(50-len(message)), message, ' '*(50-len(message)))).grid(row=1)
        Label(self.root, text='%s%s%s' % (' '*(50-len(message2)), message2, ' '*(50-len(message2)))).grid(row=2)
        Label(self.root, text='%s%s%s' % (' '*(50-len(message3)), message3, ' '*(50-len(message3)))).grid(row=3)
        self.root.geometry('{}x{}'.format(400, 150))
        ##Spaces are disgraces//
        Label(self.root, text='').grid(row=4)
        Label(self.root, text='').grid(row=0)
        ##End of disgraces//
        Button(self.root, command=self.root.destroy, text='Comprendo').grid(row=800)
        

class Mainmenu:
    def __init__(self):
        self.root = Tk()
        self.root.resizable(width=FALSE, height=FALSE)
        self.root.geometry('{}x{}'.format(300, 320))
        self.root.title('uDEncrypt')
        Label(self.root, text='Welcome to uEncrypt 2000').grid(row=1)
        Label(self.root, text='Please select any type of encryption to begin').grid(row=400)
        Button(self.root, text="      XOR Encryption/Decryption      ", command=self.xor).grid(row=500)
        Button(self.root, text="      CipherDisk Encryption/Decryption      ", command=self.disk).grid(row=600)
        Label(self.root, text='Or insert a saved encrypted filename for ease of access.').grid(row=698)
        Button(self.root, text="      Auto Detect      ", command=self.detect).grid(row=700)
        self.filename = StringVar()
        self.filename.set("untitled")
        Entry(self.root, textvariable=self.filename).grid(row=699, column=0)
        Button(self.root, command=self.root.quit, text='        Terminate        ').grid(row=800)
        ##Spaces are disgraces//
        Label(self.root, text='').grid(row=1)
        Label(self.root, text='').grid(row=401)
        Label(self.root, text='').grid(row=501)
        Label(self.root, text='').grid(row=701)
        Label(self.root, text='').grid(row=602)
        Label(self.root, text='').grid(row=402)
        Label(self.root, text='').grid(row=0)
        ##End of disgraces//
        self.root.mainloop()
        
    def xor(self):
        if check_op():
            denied()
        else:
            global opening
            opening = True
            current = XOR()
    
    def disk(self):
        if check_op():
            denied()
        else:
            global opening
            opening = True
            current = CipherDisk()
    
    def detect(self):
        if check_op():
            denied()
        else:
            current = AutoDetect(self.filename.get())
    
def check_op():
    global opening
    if opening:
        return True

def denied():
    Popup('Achtung!', 'You may not open multiple encryption window.', 'Close any remaining window other than mainmenu before continuing.')
    
opening = False
mane = Mainmenu()
