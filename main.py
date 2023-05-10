import random
from tkinter import *
from view import *
def main():
    file = 'words'
    window = Tk()
    window.title('Hangman')
    window.geometry('700x600')
    window.resizable(False, False)
    game = HangMan(window)
    window.mainloop()


if __name__ == '__main__':
    main()