from random import randint
from tkinter import *


class TestGame(Frame):
    board = [["|" for x in range(3)] for i in range(7)]]
    bo = False
    car = 1
    counter = 0
    lst = []  #list of obstacle coordinates

    def __init__(self, master=None):
        super().__init__(master)

    def spawn_obst(self):
        check = False
        if self.counter % 3 == 0 or self.counter == 0:#every three passes of the cycle starting from 0 inslusively
            for j in range(randint(1, 2)):                                                      #executes this loop
                rnd = randint(0, 2)
                if len(self.lst) >= 2 and rnd == self.lst[len(self.lst)-1]:
                    while rnd == self.lst[len(self.lst)-1]:
                        rnd = randint(0, 2)
                self.lst.append(0) #put the first obstacle in position(0,rnd) of the board
                self.lst.append(rnd)
        for ind in range(0, len(self.lst), 2):
            if self.lst[ind] != 0: #if the index of the obstacle is not equals to the first line then replace
                if self.board[self.lst[ind]-1][self.lst[ind+1]] != "O":   #last obstacle value to the value of free
                    self.board[self.lst[ind]-1][self.lst[ind+1]] = "|"    #traffic if car is not in this position
            if self.lst[ind] == len(self.board):    #if obstacle reached the end of the board then do the same as
                if self.board[self.lst[ind] - 1][self.lst[ind + 1]] != "O": #on the 25-26 lines
                    self.board[self.lst[ind] - 1][self.lst[ind + 1]] = "|"
                check = True    #and set the true value of check variable || look down ---
                continue
            self.board[self.lst[ind]][self.lst[ind+1]] = "x"  #put obstacle on the board due to coordinates in lst list
            if len(self.board)-1 == self.lst[ind] and self.car == self.lst[ind+1]: #if obstacle and the car
                self.bo = True    # in the same position
            self.lst[ind] += 1      #moves the obstacle towards
        else:
            if check: #if check is true then remove the first 2 values from lst list, because coordinates of these obstacles
                self.lst = self.lst[2:]  #are unnecessary e. g. because they reached the end and obstacle is redundant
        self.counter += 1
        TestGame.clear_screen(self)
        TestGame.build_board(self)

    def car_spawn(self):
        self.board[len(self.board)-1][self.car] = "O"

    def car_control_left(self):
        if self.car != 0:
            self.board[len(self.board) - 1][self.car] = "|"
            self.car -= 1
            if self.board[len(self.board) - 1][self.car] != "x":
                self.board[len(self.board) - 1][self.car] = "O"
            else:
                self.bo = True
            TestGame.clear_screen(self)
            TestGame.build_board(self)

    def car_control_right(self):
        if self.car != 2:
            self.board[len(self.board) - 1][self.car] = "|"
            self.car += 1
            if self.board[len(self.board) - 1][self.car] != "x":
                self.board[len(self.board) - 1][self.car] = "O"
            else:
                self.bo = True      #True when the game is finished
            TestGame.clear_screen(self)
            TestGame.build_board(self)

    def build_board(self):      #shows the board
        for each in gm.board:
            txt.insert(END, "    ".join(each) + "\n")
        txt.tag_add("justify", "1.0", END)
        txt.pack(side="left")

    def game_over(self):        #finishes the game
        txt.destroy()
        lbl.pack()
        btn1.destroy()
        btn2.destroy()
        root.after(10000, root.destroy)

    def clear_screen(self):
        txt.delete("1.0", END)

    def loopSpawnObst(self, n, t):  #loop to delay obstacles appearance
        if self.bo != True:
            TestGame.spawn_obst(self)
            if n >= 550:
                t = 0
            elif n >= 500:
                t = 3
            elif n >= 350:
                t = 5
            root.after(750-n, TestGame.loopSpawnObst, self, n+t, t)
        else:
            TestGame.game_over(self)

    def run(self):
        btnm.destroy()
        fr.pack(side="bottom")
        btn1.pack(anchor=W, side="left")
        btn2.pack(anchor=E, side="left")
        TestGame.car_spawn(self)
        TestGame.build_board(self)
        TestGame.loopSpawnObst(self, 0, 10)


root = Tk()
root.title("Minigame")
root.geometry("400x320+500+200")
gm = TestGame(root)
txt = Text(root, font=("Courier",19))
fr = Frame(root)
lbl = Label(root, text="Game over", justify="center", font=("Courier",19))
txt.tag_configure("justify", justify="center")
btnm = Button(root, text="Start", command=gm.run, width=20, height=5)
btn1 = Button(fr, text="<", command=gm.car_control_left, width=28, height=5)
btn2 = Button(fr, text=">", command=gm.car_control_right, width=28, height=5)
btnm.pack(side="top")
root.resizable(False,True)
root.mainloop()
