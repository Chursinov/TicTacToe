from tkinter import *
from PIL import ImageTk
from PIL import Image as Img
from random import randint


class Window:
    def __init__(self):
        self.A = []
        self.root = Tk()
        self.root.title('Black Jack [21]')
        self.root.geometry('330x330')
        self.root.resizable(False, False)
        self.root.attributes('-topmost', True)
        self.status = Label(self.root)
        self.blank = ImageTk.PhotoImage(Img.open('blank.png'))  # Определяем текстуру фона окна
        self.X = ImageTk.PhotoImage(Img.open('X.png'))  # Определяем текстуру фона окна
        self.O = ImageTk.PhotoImage(Img.open('O.png'))  # Определяем текстуру фона окна
        self.kv0 = Button(self.root, image=self.blank, bg='#000000', border='0', relief=FLAT, command=lambda: self.tap(0))
        self.kv1 = Button(self.root, image=self.blank, bg='#000000', border='0', relief=FLAT, command=lambda: self.tap(1))
        self.kv2 = Button(self.root, image=self.blank, bg='#000000', border='0', relief=FLAT, command=lambda: self.tap(2))
        self.kv3 = Button(self.root, image=self.blank, bg='#000000', border='0', relief=FLAT, command=lambda: self.tap(3))
        self.kv4 = Button(self.root, image=self.blank, bg='#000000', border='0', relief=FLAT, command=lambda: self.tap(4))
        self.kv5 = Button(self.root, image=self.blank, bg='#000000', border='0', relief=FLAT, command=lambda: self.tap(5))
        self.kv6 = Button(self.root, image=self.blank, bg='#000000', border='0', relief=FLAT, command=lambda: self.tap(6))
        self.kv7 = Button(self.root, image=self.blank, bg='#000000', border='0', relief=FLAT, command=lambda: self.tap(7))
        self.kv8 = Button(self.root, image=self.blank, bg='#000000', border='0', relief=FLAT, command=lambda: self.tap(8))
        self.end_button = Button(self.root, text='Повторить', border='0', relief=FLAT, command=self.start)
        self.start()
        self.root.mainloop()

    def start(self):
        self.A = [0, 1, 2, 3, 4, 5, 6, 7, 8]
        self.status.place_forget()
        self.end_button.place_forget()
        self.kv0.place(x=0, y=0, width=110, height=110)
        self.kv0.config(image=self.blank)
        self.kv1.place(x=110, y=0, width=110, height=110)
        self.kv1.config(image=self.blank)
        self.kv2.place(x=220, y=0, width=110, height=110)
        self.kv2.config(image=self.blank)
        self.kv3.place(x=0, y=110, width=110, height=110)
        self.kv3.config(image=self.blank)
        self.kv4.place(x=110, y=110, width=110, height=110)
        self.kv4.config(image=self.blank)
        self.kv5.place(x=220, y=110, width=110, height=110)
        self.kv5.config(image=self.blank)
        self.kv6.place(x=0, y=220, width=110, height=110)
        self.kv6.config(image=self.blank)
        self.kv7.place(x=110, y=220, width=110, height=110)
        self.kv7.config(image=self.blank)
        self.kv8.place(x=220, y=220, width=110, height=110)
        self.kv8.config(image=self.blank)

    def tap(self, number):
        if self.A[number] != 'O' and self.A[number] != 'X':
            self.A[number] = 'X'
            exec(f'self.kv{number}.config(image=self.X)')
            self.check()
            self.ai()
        else:
            pass

    def ai(self):
        try:
            choose = randint(0, 8)
            if self.A[choose] != 'O' and self.A[choose] != 'X':
                self.A[choose] = 'O'
                exec(f'self.kv{choose}.config(image=self.O)')
                self.check()
            else:
                self.ai()
        except RecursionError:
            self.end('draw')

    def check(self):
        if self.A[0] == self.A[4] == self.A[8]:
            if self.A[0] == 'X':
                self.end('player')
            else:
                self.end('ai')
        elif self.A[2] == self.A[4] == self.A[6]:
            if self.A[2] == 'X':
                self.end('player')
            else:
                self.end('ai')
        elif self.A[0] == self.A[1] == self.A[2]:
            if self.A[0] == 'X':
                self.end('player')
            else:
                self.end('ai')
        elif self.A[3] == self.A[4] == self.A[5]:
            if self.A[3] == 'X':
                self.end('player')
            else:
                self.end('ai')
        elif self.A[6] == self.A[7] == self.A[8]:
            if self.A[6] == 'X':
                self.end('player')
            else:
                self.end('ai')
        elif self.A[0] == self.A[3] == self.A[6]:
            if self.A[0] == 'X':
                self.end('player')
            else:
                self.end('ai')
        elif self.A[1] == self.A[4] == self.A[7]:
            if self.A[1] == 'X':
                self.end('player')
            else:
                self.end('ai')
        elif self.A[2] == self.A[5] == self.A[8]:
            if self.A[2] == 'X':
                self.end('player')
            else:
                self.end('ai')
        else:
            pass

    def end(self, who):
        if who == 'player':
            self.status['text'] = 'Вы выиграли!'
        elif who == 'ai':
            self.status['text'] = 'Вы Проиграли!'
        else:
            self.status['text'] = 'Ничья'
        self.kv0.place_forget()
        self.kv1.place_forget()
        self.kv2.place_forget()
        self.kv3.place_forget()
        self.kv4.place_forget()
        self.kv5.place_forget()
        self.kv6.place_forget()
        self.kv7.place_forget()
        self.kv8.place_forget()
        self.status.place(x=0, y=0, width=330, height=330)
        self.end_button.place(x=0, y=220, width=330)


_ = Window()
