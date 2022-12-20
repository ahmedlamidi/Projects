import tkinter
from PIL import Image, ImageTk
import time

total = []
current = "X"
check = [["1", "1", "1"], ["1", "1", "1"], ["1", "1", "1"]]


class Board:
    def __init__(self):
        self.possible = [str(i) for i in range(0, 9)]

    def show(self):

        def checks():
            for X in range(0, 3):
                if check[0][X] == check[1][X] == check[2][X] and check[0][X] != "1":
                    print(check[0][X] + " WINS")
                    current.destroy()
                elif check[X][0] == check[X][1] == check[X][2] and check[X][0] != "1":
                    print(check[X][0] + " WINS")
                    current.destroy()
            if check[0][0] == check[1][1] == check[2][2] and check[2][2] != "1":
                print(check[0][0] + " WINS")
                current.destroy()
            elif check[0][2] == check[1][1] == check[2][0] and check[2][0] != "1":
                print(check[0][2] + " WINS")
                current.destroy()
            if len(self.possible) == 0:
                print("DRAW")
                current.destroy()

        def make(example):
            global total
            global current
            if example in self.possible:
                self.possible.remove(example)
                if current == "X":
                    check[int(example) // 3][int(example) % 3] = "X"
                    total[0].configure(image=big_x)
                    total = []
                    current = "O"
                    checks()
                else:
                    total[0].configure(image=big_o)
                    check[int(example) // 3][int(example) % 3] = "O"
                    total = []
                    current = "X"
                    checks()
            else:
                total = []

        current = tkinter.Tk()

        vertical_black = ImageTk.PhotoImage(Image.open("/Users/ahmee/OneDrive/Documents/download.png").resize((5, 270)))
        horizontal = tkinter.Frame(height=270, width=270)
        first_vertical = tkinter.Label(master=horizontal, image=vertical_black)
        first_vertical.place(x=90, y=0)
        second_vertical = tkinter.Label(master=horizontal, image=vertical_black)
        second_vertical.place(x=180, y=0)

        horizontal_black = ImageTk.PhotoImage(Image.open("/Users/ahmee/OneDrive/Documents/download.png").resize((80, 5)))
        first_horizontal = tkinter.Label(master=horizontal, image=horizontal_black)
        first_horizontal.place(x=5, y=90)
        second_horizontal = tkinter.Label(master=horizontal, image=horizontal_black)
        second_horizontal.place(x=97.5, y=90)
        third_horizontal = tkinter.Label(master=horizontal, image=horizontal_black)
        third_horizontal.place(x=187.5, y=90)
        fourth_horizontal = tkinter.Label(master=horizontal, image=horizontal_black)
        fourth_horizontal.place(x=5, y=180)
        fifth_horizontal = tkinter.Label(master=horizontal, image=horizontal_black)
        fifth_horizontal.place(x=97.5, y=180)
        sixth_horizontal = tkinter.Label(master=horizontal, image=horizontal_black)
        sixth_horizontal.place(x=187.5, y=180)

        all_white = ImageTk.PhotoImage(Image.open("/Users/ahmee/OneDrive/Documents/white background.png").resize((80, 80)))
        big_x = ImageTk.PhotoImage(Image.open("/Users/ahmee/OneDrive/Documents/my_x.png").resize((80, 80)))
        big_o = ImageTk.PhotoImage(Image.open("/Users/ahmee/OneDrive/Documents/my_o.png").resize((80, 80)))

        button1 = tkinter.Button(master=horizontal, image=all_white
                                 , command=lambda: [total.append(button1), make("0")])
        button1.place(x=5, y=5)
        button2 = tkinter.Button(master=horizontal, image=all_white
                                 , command=lambda: [total.append(button2), make("1")])
        button2.place(x=97.5, y=5)
        button3 = tkinter.Button(master=horizontal, image=all_white
                                 , command=lambda: [total.append(button3), make("2")])
        button3.place(x=187.5, y=5)
        button4 = tkinter.Button(master=horizontal, image=all_white
                                 , command=lambda: [total.append(button4), make("3")])
        button4.place(x=5, y=97.5)
        button5 = tkinter.Button(master=horizontal, image=all_white
                                 , command=lambda: [total.append(button5), make("4")])
        button5.place(x=97.5, y=97.5)
        button6 = tkinter.Button(master=horizontal, image=all_white
                                 , command=lambda: [total.append(button6), make("5")])
        button6.place(x=187.5, y=97.5)
        button7 = tkinter.Button(master=horizontal, image=all_white
                                 , command=lambda: [total.append(button7), make("6")])
        button7.place(x=5, y=187.5)
        button8 = tkinter.Button(master=horizontal, image=all_white
                                 , command=lambda: [total.append(button8), make("7")])
        button8.place(x=97.5, y=187.5)
        button9 = tkinter.Button(master=horizontal, image=all_white
                                 , command=lambda: [total.append(button9), make("8")])
        button9.place(x=187.5, y=187.5)

        horizontal.pack()
        current.mainloop()


def main():
    example = Board()
    example.show()


main()

