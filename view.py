from tkinter import *
import random

class HangMan:
    """
    Class representing details for HangMan ui functionality
    """
    def __init__(self, window) -> None:
        """
        Constructor to create initial state of HangMan object
        :param window: window made in main, named HangMan with dimensions 700x600
        """
        self.get_word() #gets word in list form
        self.lives = ['head','body','left_arm','right_arm','left_leg','right_leg']
        self.guess = ['  _  ' for i in self.word] #creates list of 'blanks' to hold correctly guessed letters
        self.window = window
        self.frame = Frame(self.window)

        #creating canvas for hangman to be drawn onto
        self.canvas = Canvas(window, width=700, height=500, bg='white') #
        self.canvas.create_rectangle(350, 0, 700, 100, fill='white', outline='')
        self.canvas.pack()
        self.canvas.create_line(80, 30, 320, 30, width=12)  # top line
        self.canvas.create_line(80, 24, 80, 400, width=12)  # vertical line
        self.canvas.create_line(50, 400, 150, 400, width=12)  # base line

        #word dashes/blank spaces
        self.canvas.create_text(425,425, width=500, text=''.join(self.guess), font='Ariel 40 bold')

        #entry
        self.submit_button = Button(self.frame, width=5, text='Submit', font=('Ariel 20 bold'), command=self.clicked)
        self.label = Label(self.frame, text='INPUT YOUR GUESS:',font=('Ariel 30 bold'))
        self.entry = Entry(self.frame,width=10, font=('Ariel 50'))
        self.entry.focus_set()
        self.frame.pack(anchor='w', pady=5)
        self.submit_button.pack(ipady=10, side='right')
        self.label.pack(padx=5, side='left')
        self.entry.pack(ipady=45, side='left')

    def get_word(self) -> None:
        '''
        Function to get list of the word for game from file
        '''
        word_bank = []
        file = 'words'
        with open(file, 'r') as file:
            for line in file:
                word_bank.append(file.readline())
                word_bank = [i.strip() for i in word_bank]
        self.word = word_bank[random.randint(0, len(word_bank) - 1)] #picks random word from file/wordbank
        self.word = [i for i in self.word] #converts word str to list
        #print(self.word) #can uncomment to make testing easier, will print the correct word once chosen


    def clicked(self) -> None:
        '''
        Function for when the self.submit_button is clicked to check if letter is in word and track the 'lives' left for player
        '''
        letter = self.entry.get().lower()
        user = self.lives[0] #so it will go in order of self.lives list in drawing hangman
        self.canvas.create_rectangle(350, 0, 700, 100, fill='white', outline='') #covers try exception text
        self.entry.delete(0, END) #blanks entry
        self.entry.focus_set()
        try: #if user entry is multiple letters or not a str raises ValueError()
            if len(letter) != 1:
                raise ValueError()

            #guess is wrong
            elif letter not in self.word:
                if user == 'head':
                    self.create_head()
                elif user == 'body':
                    self.create_body()
                elif user == 'left_arm':
                    self.create_arm_L()
                elif user == 'right_arm':
                    self.create_arm_R()
                elif user == 'left_leg':
                    self.create_leg_L()
                elif user == 'right_leg':
                    self.create_leg_R()
                self.lives.pop(0)
                if len(self.lives) == 0:
                    self.game_over()

            #guess is correct
            else:
                for i in range(len(self.word)):
                    if self.word[i] != self.guess[i]:
                        if self.word[i] == letter:
                            self.guess[i] = letter
                #displays guess and blank spaces left
                self.canvas.create_rectangle(200,550,700,400,fill='white',outline='')
                self.canvas.create_text(425, 425, width=500, text='   '.join(self.guess),font='Ariel 40 bold')

                #if they've won
                if self.guess == self.word:
                    self.winner()

        #displays error of "Must be one letter only!!" if int or len >1
        except ValueError:
            self.canvas.create_text(510,30,text='Must be one letter only!!',fill='red',font='Ariel 25 italic bold')

    def create_head(self) -> None:
        '''
        Function to create head of hangman
        '''
        self.canvas.create_line(300, 30, 300, 60, width=2.5) #rope
        self.canvas.create_oval(250, 60, 350, 160, width=4)

    def create_body(self) -> None:
        '''
        Function to create body of hangman
        '''
        self.canvas.create_line(300,160,300,300, width=4)

    def create_leg_R(self) -> None:
        '''
        Function to create right leg of hangman
        '''
        self.canvas.create_line(300,300,360,380, width=4)

    def create_leg_L(self) -> None:
        '''
        Function to create left leg of hangman
        '''
        self.canvas.create_line(300,300,240,380, width=4)

    def create_arm_R(self) -> None:
        '''
        Function to create right arm of hangman
        '''
        self.canvas.create_line(300,200,350,250, width=4)

    def create_arm_L(self) -> None:
        '''
        Function to create left arm of hangman
        '''
        self.canvas.create_line(300,200,250,250, width=4)

    def game_over(self) -> None:
        '''
        Function for game over screen after whole hangman has been created and asks if player wants to try again
        '''
        self.erase_window()
        self.frame = Frame(self.window)
        self.canvas = Canvas(self.window, width=700, height=500, bg='white')
        self.canvas.pack()
        self.frame.pack()
        self.canvas.create_rectangle(0,0,700,700, fill='red')
        self.canvas.create_text(350,250,text='GAME OVER',font='Impact 100 bold',)
        self.canvas.create_text(350,350,text=f"The word was... {''.join(self.word)}!",font='Impact 25 bold',)
        self.try_again = Button(self.frame, width=100, text="Try Again?", fg="red", font='Ariel 30 bold',command=lambda: self.restart())
        self.try_again.pack(side='bottom', anchor='s')

    def winner(self) -> None:
        '''
        Function for winner screen after they got all the correct letters and asks if player wants to try again
        '''
        self.erase_window()
        self.frame = Frame(self.window)
        self.canvas = Canvas(self.window, width=700, height=500, bg='white')
        self.canvas.pack()
        self.frame.pack()
        self.canvas.create_rectangle(0,0,700,700, fill='light green')
        self.canvas.create_text(350,250,text='WINNER!!',font='Impact 100 bold',)
        self.canvas.create_text(350,350,text=f"The word was... {''.join(self.word)}!",font='Impact 25 bold',)
        self.frame = Frame(self.window)
        self.try_again = Button(self.frame, width=100, text="Try Again?", fg="green", font='Ariel 30 bold', command=lambda:self.restart())
        self.try_again.pack(side='bottom',anchor='s')
        self.frame.pack()

    def restart(self) -> None:
        """
        Function to restart game
        """
        self.erase_window()
        HangMan(self.window)

    def erase_window(self) -> None:
        '''
        Function for clearing window
        '''
        self.frame.pack_forget()
        self.canvas.pack_forget()



