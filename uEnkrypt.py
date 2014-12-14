'''
Project ala Pegeant:
    Encryption and Decryption.
'''

from Tkinter import *

class XOR:
    '''
    For operation concerning XOR method.
    Attribute : A sequence of character.
    '''
    def __init__(self, original='Default', rawkey='00000000', auto=False, filename='untitled'):
        self.root = Tk()
        if auto:
            self.filename = StringVar()
            self.filename.set(filename)
            self.load()
        self.root.resizable(width=FALSE, height=FALSE)
        self.root.geometry('{}x{}'.format(300, 400))
        self.root.title('XOR Cipher')
        Label(self.root, text='').grid(row=3)
        Label(self.root, text='   XOR cipher uses its namesake logic gate     ').grid(row=1)
        Label(self.root, text='           to switch binary from 0 to 1 and vice versa.           ').grid(row=2)
        Label(self.root, text='Enter sequence of characters you wish to decrypt below.').grid(row=4)
        self.original = StringVar(self.root)
        self.original.set(original)
        Entry(self.root, textvariable=self.original).grid(row=5,columnspan=100, sticky=W+E+N+S)
        self.stat = StringVar(self.root)
        self.stat.set("Binary") # initial value
        option = OptionMenu(self.root, self.stat, "Binary", "Number", "ASCII Character").grid(row=7)
        Label(self.root, text='Select key type from below.').grid(row=6)
        Label(self.root, text='Insert a key according to the type you choose.').grid(row=8)
        self.rawkey = StringVar(self.root)
        self.rawkey.set(rawkey)
        Entry(self.root, textvariable=self.rawkey).grid(row=9,column=0)
        Button(self.root, text="      Begin Encryption/Decryption      ", command=self.encryption).grid(row=10)
        Label(self.root, text='').grid(row=100)
        Label(self.root, text='Filename').grid(row=101)
        self.filename = StringVar(self.root)
        self.filename.set('untitled')
        Entry(self.root, textvariable=self.filename).grid(row=105)
        Button(self.root, text="      Save      ", command=self.save).grid(row=106)
        Button(self.root, text="      Load      ", command=self.load).grid(row=107)
        Label(self.root, text='').grid(row=108)
        Button(self.root, text="      Back      ", command=self.quitting).grid(row=200)

        self.root.mainloop()
    def __str__(self):
        return self.original
    def get_key(self):#Maximum MUST be 00111111
        print self.rawkey.get()
        if self.stat.get() == 'Number':
            self.key = bin(int(self.rawkey.get()))[-6:]
        elif self.stat.get() == 'ASCII Character':
            self.key = bin(ord(self.rawkey.get()))[-6:]
        else:
            self.key = self.rawkey.get()[-6:]
        self.key = '0'*(8-len(self.key.replace('b', '')))+self.key.replace('b', '')
    def encryption(self):
        '''
        It's both the encryption and decryption actually.
        '''
        self.get_key()
        self.encrypted = ''
        for longgong in self.original.get():
            temp = ''
            longgong = '0'*(8-len(bin(ord(longgong.replace('b', '')))))+bin(ord(longgong)).replace('b', '')#OLD-> '%8s' % bin(ord(longgong)).replace('b', '')
            for tower, rook in zip(longgong.replace(' ', '0'), self.key):
                if tower == rook:
                    temp += '0'
                else:
                    temp += '1'
            print longgong.replace(' ', '0'), self.key, temp
            self.encrypted += chr(int(temp, 2))
        print self.encrypted
        PopupResult('XOR Cipher', self.encrypted)
    def decryption(self):
        '''
        A layout for other methods.
        '''
        pass
    def quitting(self):
        self.root.destroy()
        mane = Mainmenu()

    def save(self):
        try:
            text = open('%s.txt' % self.filename.get(), 'w')
            text.write('bindingofclarke')
            text.write('jaaaaiaaayaaaason!jaaaasonjasonjaeeeaason')
            text.write(self.key)
            text.write('8151321542334longgong5789546512367')
            text.write(self.encrypted)
            Popup('XOR Save', 'Save completed.')
        except:
            Popup('XOR Save', 'Save Failed.')

    def load(self):
        try:
            text = open('%s.txt' % self.filename.get(), 'r')
            cur = text.read().split('jaaaaiaaayaaaason!jaaaasonjasonjaeeeaason',1)[1]
            rawkey, original = cur.split('8151321542334longgong5789546512367', 1)
            self.root.destroy()
            current = XOR(original, rawkey)
        except:
            Popup('XOR Load', 'Load Failed.')

###############################################################END OF XOR############################################################################

class CipherDisk:
    '''
    For operation concerning Cipher Disk method.
    Attribute: A sequence of character, number of turns
    '''
    def __init__(self, original='Default', turn='1', disk='ABCDEFGHIJKLMNOPQRSTUVWXYZ', auto=False, filename=''):
        self.root = Tk()
        if auto:
            self.filename = StringVar()
            self.filename.set(filename)
            self.load()
        self.root.resizable(width=FALSE, height=FALSE)
        self.root.geometry('{}x{}'.format(310, 480))
        self.root.title('Cipher Disk')
        Label(self.root, text='').grid(row=3)
        Label(self.root, text='   While not as cool as the German Enigma     ').grid(row=1)
        Label(self.root, text='There are people who are oblivious to this method.').grid(row=2)
        Label(self.root, text='Enter sequence of characters you wish to decrypt below.').grid(row=4)
        Label(self.root, text='Any character not in the disk will not be altered.').grid(row=5)
        self.original = StringVar(self.root)
        self.original.set(original)
        Entry(self.root, textvariable=self.original).grid(row=6,columnspan=100, sticky=W+E+N+S)
        Label(self.root, text='Specify a number of turn in integer. (Shift)').grid(row=7)
        self.turn = StringVar(self.root)
        self.turn.set(turn)
        Entry(self.root, textvariable=self.turn).grid(row=10,columnspan=1)
        Label(self.root, text='Alter the Cipher Disk below.').grid(row=14)
        self.disk = StringVar(self.root)
        self.disk.set(disk)
        Entry(self.root, textvariable=self.disk).grid(row=15,columnspan=2, sticky=W+E+N+S)
        Label(self.root, text='').grid(row=16)
        Button(self.root, text="      Begin Encryption      ", command=self.encryption).grid(row=20)
        Button(self.root, text="      Begin Decryption      ", command=self.decryption).grid(row=21)
        Label(self.root, text='').grid(row=100)
        Label(self.root, text='Filename').grid(row=101)
        self.filename = StringVar(self.root)
        self.filename.set('untitled')
        Entry(self.root, textvariable=self.filename).grid(row=105)
        Button(self.root, text="      Save      ", command=self.save).grid(row=106)
        Button(self.root, text="      Load      ", command=self.load).grid(row=107)
        Label(self.root, text='').grid(row=199)
        Button(self.root, text="      Back      ", command=self.quitting).grid(row=200)
        self.root.mainloop()
        
    def encryption(self):
        self.encrypted = ''
        for longgong in self.original.get():
            if longgong in self.disk.get():
                self.encrypted += self.disk.get()[(self.disk.get().index(longgong)+int(self.turn.get()))%len(self.disk.get())]
            elif longgong.upper() in self.disk.get():
                self.encrypted += self.disk.get()[(self.disk.get().index(longgong.upper())+int(self.turn.get()))%len(self.disk.get())].lower()
            else:
                self.encrypted += longgong
        print self.encrypted
        PopupResult('Cipher Disk', self.encrypted)
        
    def decryption(self):
        self.decrypted = ''
        for longgong in self.original.get():
            if longgong in self.disk.get():
                self.decrypted += self.disk.get()[(self.disk.get().index(longgong)-int(self.turn.get()))%len(self.disk.get())]
            elif longgong.upper() in self.disk.get():
                self.decrypted += self.disk.get()[(self.disk.get().index(longgong.upper())-int(self.turn.get()))%len(self.disk.get())].lower()
            else:
                self.decrypted += longgong
        print self.decrypted
        PopupResult('Cipher Disk', self.decrypted)
        
    def quitting(self):
        self.root.destroy()
        mane = Mainmenu()

    def save(self):
        try:
            text = open('%s.txt' % self.filename.get(), 'w')
            text.write('Cesareborgia')
            text.write('jaaaaiaaayaaaason!jaaaasonjasonjaeeeaason')
            text.write(self.disk.get())
            text.write('shauunshaunnasdsafyaaaashaunnnnnwaaksdjdisal')
            text.write(self.turn.get())
            text.write('8151321542334longgong5789546512367')
            text.write(self.encrypted)
            Popup('CipherDisk Save', 'Save Completed.')
        except:
            Popup('CipherDisk Save', 'Save Failed.')

    def load(self):
        try:
            text = open('%s.txt' % self.filename.get(), 'r')
            cur = text.read().split('jaaaaiaaayaaaason!jaaaasonjasonjaeeeaason',1)[1]
            disk, cur = cur.split('shauunshaunnasdsafyaaaashaunnnnnwaaksdjdisal', 1)
            turn, original = cur.split('8151321542334longgong5789546512367', 1)
            self.root.destroy()
            current = CipherDisk(original, turn, disk)
        except:
            Popup('CipherDisk Load', 'Load Failed.')
        
def load(filename='untitled'):
    text = open('%s.txt' % filename, 'r')
    return tuple(text.read().split('jaaaaiaaayaaaason!jaaaasonjasonjaeeeaason'))

class AutoDetect:
    def __init__(self, filename):
        try:
            me = load(filename)
            if me[0] == 'bindingofclarke':
                Popup('Auto-Detect Report', '      This file uses XOR method.      ', 'Taking you there.')
                current = XOR('', '', True, filename)
            elif me[0] == 'Cesareborgia':
                Popup('Auto-Detect Report', '       This file uses Cipher Disk method.        ', 'Taking you there.')
                current = CipherDisk('', '', '', True, filename)
            else:
                Popup('Achtung!', 'The program cannot recognize this files.', 'Which makes it near 100% that it can not be decrypted.')
                mane = Mainmenu()
        except(IOError):
            Popup('Achtung!', 'Attention : No such files specified.')
            mane = Mainmenu()


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

class PopupResult():
    def __init__(self, title='Insert Title', bunny='A result'):
        self.root = Tk()
        self.root.resizable(width=FALSE, height=FALSE)
        self.root.geometry('{}x{}'.format(400, 150))
        self.root.title(title)
        Label(self.root, text='                                                                                                                             ').grid(row=0)
        Label(self.root, text='The result is in.').grid(row=1)
        Label(self.root, text='').grid(row=2)
        Label(self.root, text='').grid(row=5)
        message = StringVar(self.root)
        message.set(bunny)
        Entry(self.root, textvariable=message).grid(row=4,columnspan=5,rowspan=250, sticky=W+E+N+S)
        Button(self.root, command=self.root.destroy, text='Comprendo').grid(row=500)
        

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
        self.filename = StringVar(self.root)
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
        self.root.destroy()
        current = XOR()
    
    def disk(self):
        self.root.destroy()
        current = CipherDisk()
    
    def detect(self):
        self.root.destroy()
        current = AutoDetect(self.filename.get())

mane = Mainmenu()
