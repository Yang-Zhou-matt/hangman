from tkinter import *  # Import tkinter

import random

list5 = ['ankle', 'apple', 'birds', 'aunts', 'blood',
        'bones', 'forty', 'glitz', 'gnome', 'goats',
        'fairy', 'gator', 'glass', 'kneel', 'laces',
        'patio', 'party', 'taffy', 'zones', 'wages'
        ]# a list of five letter words

list10 = ['jackrabbit', 'maximizers', 'abnormally', 'abolishers',
        'adrenaline', 'california', 'basketball', 'friendship',
        'renovation', 'skateboard', 'understand', 'leadership',
        'restaurant', 'generation', 'girlfriend', 'vegetables',
        'protection', 'trampoline', 'rainforest', 'instrument'
        ]# a list of 10 letter words

list15 = ['maneuverability', 'insubordination', 'excommunication',
        'acclimatization', 'rationalisation', 'mischievousness',
        'kindheartedness', 'procrastinating', 'confidentiality',
        'instrumentation', 'inaccessibility', 'marginalization'
        ]# a list of 15 lettter words


class Hangman:  # create the class
    def __init__(self):
        window = Tk()  # Create a window
        window.title("Hangman Game")  # Set a title
        self.word = list(list10[random.randint(0, 20)])  # chose a random word from list
        self.blanks = list("*" * len(self.word))  # show the number of word's letter
        self.guessed = []  # create a list store guessed letters
        self.missed = 0  # create a variable to record missed time

        menubar = Menu(window)  # create a menu bar
        window.config(menu=menubar)  # Display the menu bar

        # create a pulldown menu, and add it to the menu bar
        operationMenu = Menu(menubar, tearoff=0)
        menubar.add_cascade(label="difficulty", menu=operationMenu)
        operationMenu.add_command(label="5 letter words",
                                  command=self.list5)
        operationMenu.add_command(label="10 letter words",
                                  command=self.list10)
        operationMenu.add_command(label="15 letter words",
                                  command=self.list15)

        canvas = Canvas(window, bg="white", width=1, height=1)  # create a canvas to bind with key
        canvas.pack()
        canvas.bind("<Key>", self.processKeyEvent)  # bind the key pressed with the GUI programe
        canvas.focus_set()

        frame1 = Frame(window)  # create a frame and some labels to show information
        frame1.pack()
        self.lbl = Label(frame1, text="(Guess) Press a key letter in word"+ str(self.blanks) + ">")
        self.lbl.pack()
        self.lb2 = Label(frame1, text="")
        self.lb2.pack()
        self.lb3 = Label(frame1, text="")
        self.lb3.pack()
        self.lb4 = Label(frame1, text="")
        self.lb4.pack()

        frame2 = Frame(window)  # create a frame and add a bottom for "play again" and a label to show "Time Left"
        frame2.pack()
        btPlayAgain = Button(frame2, text="play again",
                              command=self.playagain)
        self.label2 = Label(frame2, text="Times Left: 7")
        btPlayAgain.grid(row=1, column=3)
        self.label2.grid(row=2, column=1)

        # Place canvas in window
        self.canvas = Canvas(window, width=400, height=300, bg="white")
        self.canvas.pack()
        # show a picture of hangman
        self.canvas.create_text(100, 150, text="""
                                                        ||=======
                                                        ||//           
                                                        ||             
                                                        ||            
                                                        ||
                                                        ||
                                                        ||
                                                        ||
                                                        ||
                                                        ||
                                                        ----------------""", font="Helvetica 10", tags="string")

        window.mainloop()  # Create an event loop

    def processKeyEvent(self, event):  # create a function, the input is event(the key pressed).
        if self.blanks != self.word:  # check if word have been guessed
            letter = event.char  #
            if letter in self.guessed: # check if the word have been guessed.
                self.lb2["text"] = letter, "is already guessed"
            elif letter in self.word:  # check if the letter in word
                for i in range(0, len(self.word)):
                    if letter == self.word[i]:  # find where the letter is in the word.
                        self.blanks.pop(i)  # remove the * in the place
                        self.blanks.insert(i, letter)  # insert the letter in
                        if self.blanks == self.word:  # if the word is guessed
                            self.lb2["text"] = "The word is program.You missed", self.missed, "time"
                            self.lb3["text"] = "Do you want to guess another word or change difficulty?"
            elif letter not in self.word:  # if the letter is not in word
                self.lb2["text"] = letter, "is not in the word"
                self.missed += 1  # missed time add one
                self.drawHangman()  # show next picture
        self.guessed.append(letter)  # add the letter to the guessed list
        self.lbl["text"] = "(Guess) Press a key letter in word" + str(self.blanks) + ">"  # show letter guessed
        self.lb4["text"] = "guessed words:" + str(self.guessed)  # show guessed letters
        self.label2["text"] = "Time Left:" + str(7 - self.missed)  # show time left

    def playagain(self):  # play again
        self.word = list(list10[random.randint(0, 20)])  # choose a new word
        self.blanks = list("*" * len(self.word))  # reset the blank
        self.guessed = []  # reset guessed list
        self.missed = 0  # reset missed time
        # reset these labels
        self.lbl["text"] = "(Guess) Press a key letter in word" + str(self.blanks) + ">"
        self.lb2["text"] = ""
        self.lb3["text"] = ""
        self.canvas.delete("string")  # delete canvas picture

    def list5(self):  # change list where the word came from and reset everything for play again
        self.word = list(list5[random.randint(0, 20)])
        self.blanks = list("*" * len(self.word))
        self.guessed = []
        self.missed = 0
        self.lbl["text"] = "(Guess) Press a key letter in word" + str(self.blanks) + ">"
        self.lb2["text"] = ""
        self.lb3["text"] = ""
        self.canvas.delete("string")

    def list10(self):  # change list where the word came from and reset everything for play again
        self.word = list(list10[random.randint(0, 20)])
        self.blanks = list("*" * len(self.word))
        self.guessed = []
        self.missed = 0
        self.lbl["text"] = "(Guess) Press a key letter in word" + str(self.blanks) + ">"
        self.lb2["text"] = ""
        self.lb3["text"] = ""
        self.canvas.delete("string")

    def list15(self):  # change list where the word came from and reset everything for play again
        self.word = list(list15[random.randint(0, 20)])
        self.blanks = list("*" * len(self.word))
        self.guessed = []
        self.missed = 0
        self.lbl["text"] = "(Guess) Press a key letter in word" + str(self.blanks) + ">"
        self.lb2["text"] = ""
        self.lb3["text"] = ""
        self.canvas.delete("string")

    def drawHangman(self):  # show hangman pictures when guessed wrong letters
        if self.missed == 1:
            self.canvas.delete("string")
            self.canvas.create_text(100, 150, text="""
                                                    ||=======
                                                    ||//           |
                                                    ||             |
                                                    ||            0
                                                    ||
                                                    ||
                                                    ||
                                                    ||
                                                    ||
                                                    ||
                                                    ----------------""", font="Helvetica 10", tags="string")
        elif self.missed == 2:
            self.canvas.delete("string")
            self.canvas.create_text(100, 150, text="""
                                                    ||=======
                                                    ||//           |
                                                    ||             |
                                                    ||            O
                                                    ||             |
                                                    ||
                                                    ||
                                                    ||
                                                    ||
                                                    ||
                                                    ----------------""", font="Helvetica 10", tags="string")
        elif self.missed == 3:
            self.canvas.delete("string")
            self.canvas.create_text(100, 150, text="""
                                                    ||=======
                                                    ||//           |
                                                    ||             |
                                                    ||            O
                                                    ||            /|
                                                    ||           |
                                                    ||
                                                    ||
                                                    ||
                                                    ||
                                                    ----------------""", font="Helvetica 10", tags="string")
        elif self.missed == 4:
            self.canvas.delete("string")
            self.canvas.create_text(100, 150, text=r"""
                                                    ||=======
                                                    ||//           |
                                                    ||             |
                                                    ||            O
                                                    ||            /|\
                                                    ||           |   |
                                                    ||
                                                    ||
                                                    ||
                                                    ||
                                                    ----------------""", font="Helvetica 10", tags="string")
        elif self.missed == 5:
            self.canvas.delete("string")
            self.canvas.create_text(100, 150, text=r"""
                                                    ||=======
                                                    ||//           |
                                                    ||             |
                                                    ||            O
                                                    ||            /|\
                                                    ||           | | |
                                                    ||
                                                    ||
                                                    ||
                                                    ||
                                                    ----------------""", font="Helvetica 10", tags="string")

        elif self.missed == 6:
            self.canvas.delete("string")
            self.canvas.create_text(100, 150, text=r"""
                                                    ||=======
                                                    ||//           |
                                                    ||             |
                                                    ||            O
                                                    ||            /|\
                                                    ||           | | |
                                                    ||            /
                                                    ||           |
                                                    ||
                                                    ||
                                                    ----------------""", font="Helvetica 10", tags="string")
        elif self.missed == 7:
            self.canvas.delete("string")
            self.canvas.create_text(100, 150, text=r"""
                                                        ||=======
                                                        ||//           |
                                                        ||             |
                                                        ||            O
                                                        ||            /|\
                                                        ||           | | |
                                                        ||            / \
                                                        ||           |   |
                                                        || you have dead,
                                                        || but you can keep
                                                        || guessing or play 
                                                        || again.   
                                                        ----------------""", font="Helvetica 10", tags="string")


Hangman()  # Create GUI

