import turtle
import random
import time

# -------- GLOBAL VARIABLES --------

# Sets up the main window
wn = turtle.Screen()
wn.title("Hangman")
wn.setup(height=800, width=1000)
wn.bgpic("img\\chalkboard.gif")
wn.tracer(0)

# To display text on screen
pen = turtle.Turtle()
pen.hideturtle()
pen.color("white")
pen.penup()
pen.goto(x=-60, y=-60)

# Keeps track of remaining guesses
num_of_guesses = 6

# Keeps track of correctly guessed letters
letter_count = 0

# Opens a file with a list of words
words_list = list(open("words", mode="r"))


# -------- CLASSES --------
class Gallows:
    def __init__(self):
        self.gallows = turtle.Turtle()

        # Adds the Gallows graphics
        wn.addshape("img\\Gallows1.gif")
        wn.addshape("img\\Gallows2.gif")
        wn.addshape("img\\Gallows3.gif")
        wn.addshape("img\\Gallows4.gif")
        wn.addshape("img\\Gallows5.gif")
        wn.addshape("img\\Gallows6.gif")
        wn.addshape("img\\Gallows7.gif")

    def display_gallows(self, remaining_guesses):
        """
        Displays right gallows image depending on the remaining guesses.
        """

        self.gallows.penup()
        self.gallows.goto(x=-250, y=150)

        if remaining_guesses == 6:
            self.gallows.shape("img\\Gallows1.gif")
        elif remaining_guesses == 5:
            self.gallows.shape("img\\Gallows2.gif")
        elif remaining_guesses == 4:
            self.gallows.shape("img\\Gallows3.gif")
        elif remaining_guesses == 3:
            self.gallows.shape("img\\Gallows4.gif")
        elif remaining_guesses == 2:
            self.gallows.shape("img\\Gallows5.gif")
        elif remaining_guesses == 1:
            self.gallows.shape("img\\Gallows6.gif")
        elif remaining_guesses == 0:
            self.gallows.shape("img\\Gallows7.gif")


class Keyboard:
    def __init__(self):
        self.letters = ["QWERTYUIOP", "ASDFGHJKL", "ZXCVBNM"]
        self.mouse = turtle.Turtle()
        self.pen = turtle.Turtle()

        # Keeps track of whether a letter has already been clicked.
        self.q_enabled = True
        self.w_enabled = True
        self.e_enabled = True
        self.r_enabled = True
        self.t_enabled = True
        self.y_enabled = True
        self.u_enabled = True
        self.i_enabled = True
        self.o_enabled = True
        self.p_enabled = True
        self.a_enabled = True
        self.s_enabled = True
        self.d_enabled = True
        self.f_enabled = True
        self.g_enabled = True
        self.h_enabled = True
        self.j_enabled = True
        self.k_enabled = True
        self.l_enabled = True
        self.z_enabled = True
        self.x_enabled = True
        self.c_enabled = True
        self.v_enabled = True
        self.b_enabled = True
        self.n_enabled = True
        self.m_enabled = True

    def display_buttons(self):
        """
        Displays the buttons in the style of a QWERTY keyboard.
        """

        y_cor = 250
        self.pen.hideturtle()
        self.pen.pensize(2)

        # Iterates over each row with letters
        for row in self.letters:
            y_cor -= 54
            x_cor = -60

            # For each letter in each row, draws a square, fills its colour and writes the letter.
            for i in row:
                self.pen.penup()
                self.pen.goto(x=x_cor, y=y_cor)
                self.pen.pendown()
                self.pen.fillcolor("grey")
                self.pen.begin_fill()
                self.pen.forward(50)
                self.pen.right(90)
                self.pen.forward(50)
                self.pen.right(90)
                self.pen.forward(50)
                self.pen.right(90)
                self.pen.forward(50)
                self.pen.right(90)
                self.pen.end_fill()

                self.pen.penup()
                self.pen.goto(x=self.pen.xcor() + 25, y=self.pen.ycor() - 45)
                self.pen.write(i, align="center", font=("Arial", 25, "bold"))

                x_cor += 54

    def mouse_clicks(self):
        """
        Allows for clicks on the letters with the mouse.
        """

        self.mouse.hideturtle()
        self.mouse.penup()
        wn.listen()
        wn.onscreenclick(self.mouse.goto)
        self.mouse.goto(0, 0)

        # Sets up the pen for scoring out letters which have already been clicked
        self.pen.hideturtle()
        self.pen.pensize(4)
        self.pen.color("red")
        self.pen.penup()
        self.pen.left(45)

    def assign_letter(self):
        """
        Tracks the position of the mouse on click and assigns a letter based on the letter clicked.
        """

        # Top row keys
        if self.q_enabled and self.mouse.xcor() in range(-60, -10) and self.mouse.ycor() in range(146, 196):
            x_cor = -60
            y_cor = 146
            self.mouse.goto(0, 0)
            self.cross_out_letter(x_cor, y_cor)
            # Disables the button after it has been clicked
            self.q_enabled = False
            return "q"
        elif self.w_enabled and self.mouse.xcor() in range(-6, 44) and self.mouse.ycor() in range(146, 196):
            x_cor = -6
            y_cor = 146
            self.mouse.goto(0, 0)
            self.cross_out_letter(x_cor, y_cor)
            # Disables the button after it has been clicked
            self.w_enabled = False
            return "w"
        elif self.e_enabled and self.mouse.xcor() in range(48, 98) and self.mouse.ycor() in range(146, 196):
            x_cor = 48
            y_cor = 146
            self.mouse.goto(0, 0)
            self.cross_out_letter(x_cor, y_cor)
            # Disables the button after it has been clicked
            self.e_enabled = False
            return "e"
        elif self.r_enabled and self.mouse.xcor() in range(102, 152) and self.mouse.ycor() in range(146, 196):
            x_cor = 102
            y_cor = 146
            self.mouse.goto(0, 0)
            self.cross_out_letter(x_cor, y_cor)
            # Disables the button after it has been clicked
            self.r_enabled = False
            return "r"
        elif self.t_enabled and self.mouse.xcor() in range(156, 206) and self.mouse.ycor() in range(146, 196):
            x_cor = 156
            y_cor = 146
            self.mouse.goto(0, 0)
            self.cross_out_letter(x_cor, y_cor)
            # Disables the button after it has been clicked
            self.t_enabled = False
            return "t"
        elif self.y_enabled and self.mouse.xcor() in range(210, 260) and self.mouse.ycor() in range(146, 196):
            x_cor = 210
            y_cor = 146
            self.mouse.goto(0, 0)
            self.cross_out_letter(x_cor, y_cor)
            # Disables the button after it has been clicked
            self.y_enabled = False
            return "y"
        elif self.u_enabled and self.mouse.xcor() in range(264, 314) and self.mouse.ycor() in range(146, 196):
            x_cor = 264
            y_cor = 146
            self.mouse.goto(0, 0)
            self.cross_out_letter(x_cor, y_cor)
            # Disables the button after it has been clicked
            self.u_enabled = False
            return "u"
        elif self.i_enabled and self.mouse.xcor() in range(318, 368) and self.mouse.ycor() in range(146, 196):
            x_cor = 318
            y_cor = 146
            self.mouse.goto(0, 0)
            self.cross_out_letter(x_cor, y_cor)
            # Disables the button after it has been clicked
            self.i_enabled = False
            return "i"
        elif self.o_enabled and self.mouse.xcor() in range(372, 422) and self.mouse.ycor() in range(146, 196):
            x_cor = 372
            y_cor = 146
            self.mouse.goto(0, 0)
            self.cross_out_letter(x_cor, y_cor)
            # Disables the button after it has been clicked
            self.o_enabled = False
            return "o"
        elif self.p_enabled and self.mouse.xcor() in range(426, 476) and self.mouse.ycor() in range(146, 196):
            x_cor = 426
            y_cor = 146
            self.mouse.goto(0, 0)
            self.cross_out_letter(x_cor, y_cor)
            # Disables the button after it has been clicked
            self.p_enabled = False
            return "p"

        # Middle Row
        elif self.a_enabled and self.mouse.xcor() in range(-60, -10) and self.mouse.ycor() in range(94, 142):
            x_cor = -60
            y_cor = 94
            self.mouse.goto(0, 0)
            self.cross_out_letter(x_cor, y_cor)
            # Disables the button after it has been clicked
            self.a_enabled = False
            return "a"
        elif self.s_enabled and self.mouse.xcor() in range(-6, 44) and self.mouse.ycor() in range(94, 142):
            x_cor = -6
            y_cor = 94
            self.mouse.goto(0, 0)
            self.cross_out_letter(x_cor, y_cor)
            # Disables the button after it has been clicked
            self.s_enabled = False
            return "s"
        elif self.d_enabled and self.mouse.xcor() in range(48, 98) and self.mouse.ycor() in range(94, 142):
            x_cor = 48
            y_cor = 94
            self.mouse.goto(0, 0)
            self.cross_out_letter(x_cor, y_cor)
            # Disables the button after it has been clicked
            self.d_enabled = False
            return "d"
        elif self.f_enabled and self.mouse.xcor() in range(102, 152) and self.mouse.ycor() in range(94, 142):
            x_cor = 102
            y_cor = 94
            self.mouse.goto(0, 0)
            self.cross_out_letter(x_cor, y_cor)
            # Disables the button after it has been clicked
            self.f_enabled = False
            return "f"
        elif self.g_enabled and self.mouse.xcor() in range(156, 206) and self.mouse.ycor() in range(94, 142):
            x_cor = 156
            y_cor = 94
            self.mouse.goto(0, 0)
            self.cross_out_letter(x_cor, y_cor)
            # Disables the button after it has been clicked
            self.g_enabled = False
            return "g"
        elif self.h_enabled and self.mouse.xcor() in range(210, 260) and self.mouse.ycor() in range(94, 142):
            x_cor = 210
            y_cor = 94
            self.mouse.goto(0, 0)
            self.cross_out_letter(x_cor, y_cor)
            # Disables the button after it has been clicked
            self.h_enabled = False
            return "h"
        elif self.j_enabled and self.mouse.xcor() in range(264, 314) and self.mouse.ycor() in range(94, 142):
            x_cor = 264
            y_cor = 94
            self.mouse.goto(0, 0)
            self.cross_out_letter(x_cor, y_cor)
            # Disables the button after it has been clicked
            self.j_enabled = False
            return "j"
        elif self.k_enabled and self.mouse.xcor() in range(318, 368) and self.mouse.ycor() in range(94, 142):
            x_cor = 318
            y_cor = 94
            self.mouse.goto(0, 0)
            self.cross_out_letter(x_cor, y_cor)
            # Disables the button after it has been clicked
            self.k_enabled = False
            return "k"
        elif self.l_enabled and self.mouse.xcor() in range(372, 422) and self.mouse.ycor() in range(94, 142):
            x_cor = 372
            y_cor = 94
            self.mouse.goto(0, 0)
            self.cross_out_letter(x_cor, y_cor)
            # Disables the button after it has been clicked
            self.l_enabled = False
            return "l"

        # Bottom Row
        elif self.z_enabled and self.mouse.xcor() in range(-60, -10) and self.mouse.ycor() in range(42, 90):
            x_cor = -60
            y_cor = 42
            self.mouse.goto(0, 0)
            self.cross_out_letter(x_cor, y_cor)
            # Disables the button after it has been clicked
            self.z_enabled = False
            return "z"
        elif self.x_enabled and self.mouse.xcor() in range(-6, 44) and self.mouse.ycor() in range(42, 90):
            x_cor = -6
            y_cor = 42
            self.mouse.goto(0, 0)
            self.cross_out_letter(x_cor, y_cor)
            # Disables the button after it has been clicked
            self.x_enabled = False
            return "x"
        elif self.c_enabled and self.mouse.xcor() in range(48, 98) and self.mouse.ycor() in range(42, 90):
            x_cor = 48
            y_cor = 42
            self.mouse.goto(0, 0)
            self.cross_out_letter(x_cor, y_cor)
            # Disables the button after it has been clicked
            self.c_enabled = False
            return "c"
        elif self.v_enabled and self.mouse.xcor() in range(102, 152) and self.mouse.ycor() in range(42, 90):
            x_cor = 102
            y_cor = 42
            self.mouse.goto(0, 0)
            self.cross_out_letter(x_cor, y_cor)
            # Disables the button after it has been clicked
            self.v_enabled = False
            return "v"
        elif self.b_enabled and self.mouse.xcor() in range(156, 206) and self.mouse.ycor() in range(42, 90):
            x_cor = 156
            y_cor = 42
            self.mouse.goto(0, 0)
            self.cross_out_letter(x_cor, y_cor)
            # Disables the button after it has been clicked
            self.b_enabled = False
            return "b"
        elif self.n_enabled and self.mouse.xcor() in range(210, 260) and self.mouse.ycor() in range(42, 90):
            x_cor = 210
            y_cor = 42
            self.mouse.goto(0, 0)
            self.cross_out_letter(x_cor, y_cor)
            # Disables the button after it has been clicked
            self.n_enabled = False
            return "n"
        elif self.m_enabled and self.mouse.xcor() in range(264, 314) and self.mouse.ycor() in range(42, 90):
            x_cor = 264
            y_cor = 42
            self.mouse.goto(0, 0)
            self.cross_out_letter(x_cor, y_cor)
            # Disables the button after it has been clicked
            self.m_enabled = False
            return "m"
        else:
            self.mouse.goto(0, 0)
            return ""

    def cross_out_letter(self, x_cor, y_cor):
        """
        Crosses out the letters which have already been clicked.
        """

        self.pen.hideturtle()
        self.pen.goto(x=x_cor, y=y_cor)
        self.pen.pendown()
        self.pen.forward(70)
        self.pen.penup()

    def reset_keyboard(self):
        """
        Resets the keyboard.
        """

        self.q_enabled = True
        self.w_enabled = True
        self.e_enabled = True
        self.r_enabled = True
        self.t_enabled = True
        self.y_enabled = True
        self.u_enabled = True
        self.i_enabled = True
        self.o_enabled = True
        self.p_enabled = True
        self.a_enabled = True
        self.s_enabled = True
        self.d_enabled = True
        self.f_enabled = True
        self.g_enabled = True
        self.h_enabled = True
        self.j_enabled = True
        self.k_enabled = True
        self.l_enabled = True
        self.z_enabled = True
        self.x_enabled = True
        self.c_enabled = True
        self.v_enabled = True
        self.b_enabled = True
        self.n_enabled = True
        self.m_enabled = True

        self.pen.reset()


class Word:
    def __init__(self):
        # Picks a random word from the list of words
        self.word = random.choice(words_list).strip()

        # Stores the correctly guessed letters
        self.correct_letters = ["-"] * len(self.word)

        self.pen = turtle.Turtle()

    def display_word(self):
        """
        Displays an nth amount of dashes depending on the length of the word.
        """

        self.pen.hideturtle()
        self.pen.color("white")
        self.pen.pensize(6)
        self.pen.penup()
        self.pen.goto(x=-480, y=-250)
        self.pen.pendown()

        # For each letter in the word, draws a dash
        for i in self.word:
            self.pen.forward(60)
            self.pen.penup()
            self.pen.forward(40)
            self.pen.pendown()

    def length_of_word(self):
        """
        Returns the length of the random word.
        """

        return len(self.word)

    def check_for_letter(self, letter):
        """
        Checks whether the passed letter is in the word. If yes draws the letter, if not updates the gallows.
        """

        global num_of_guesses
        global letter_count

        self.pen.hideturtle()
        self.pen.color("white")
        self.pen.penup()
        x_cor = -450
        y_cor = -255
        x_offset = 100

        # If the letters is in the word, writes the letter in the correct position
        if letter in self.word:
            for i in range(len(self.word)):
                if self.word[i] == letter:
                    # Stores the correct letter
                    self.correct_letters[i] = self.word[i]

                    # Moves the turtle over the correct dash with which the letter in the word is associated with
                    # and writes the letter
                    self.pen.goto(x=x_cor + (x_offset * i), y=y_cor)
                    self.pen.write(letter.upper(), align="center", font=("Arial", 60, "bold"))

                    # Increments the count of correctly guessed letters by 1
                    letter_count += 1
        # If the letters is not in the word, decrements the number of available guesses by 1
        else:
            num_of_guesses -= 1

    def fill_in_missing_letters(self):
        """
        If the game is lost, fills in the remaining letters to reveal what the random word was.
        """

        self.pen.hideturtle()
        self.pen.color("red")
        self.pen.penup()

        x_cor = -450
        y_cor = -255
        x_offset = 100

        for i in range(len(self.correct_letters)):
            if self.correct_letters[i] != self.word[i]:
                self.pen.goto(x=x_cor + (x_offset * i), y=y_cor)
                self.pen.write(self.word[i].upper(), align="center", font=("Arial", 60, "bold"))

    def reset_word(self):
        """
        Resets the word.
        """

        self.pen.clear()


# -------- MAIN GAME --------
gallows = Gallows()
keyboard = Keyboard()

while True:
    # Displays the gallows
    gallows.display_gallows(num_of_guesses)

    # Assigns a random word
    word = Word()

    # Displays the correct amount of dashes based on the length of the random word
    word.display_word()

    # Builds and displays the keyboard
    keyboard.display_buttons()

    # Allows for keyboard clicks with the mouse
    keyboard.mouse_clicks()

    len_word = word.length_of_word()

    while True:
        wn.update()

        # Assigns the letter based on the letter clicked
        letter = keyboard.assign_letter()

        # Checks whether the letters is in the word
        word.check_for_letter(letter)

        # Updates the gallows based on whether the letter was or was not in the word
        gallows.display_gallows(num_of_guesses)

        # If the number of guesses is 0 or the number of correctly guessed letters equals to the length of the word,
        # breaks out of the loop
        if num_of_guesses == 0:
            pen.write("You Lose!", font=("Arial", 45, "bold"))
            # Fills in the missing letters
            word.fill_in_missing_letters()
            break
        elif letter_count == len_word:
            pen.write("You Win!", font=("Arial", 45, "bold"))
            break
        else:
            continue

    # Updates the window one final time
    while True:
        wn.update()
        break

    # Pauses the game for 2 seconds
    time.sleep(2)

    # Resets the game
    num_of_guesses = 6
    letter_count = 0
    pen.clear()
    word.reset_word()
    keyboard.reset_keyboard()
