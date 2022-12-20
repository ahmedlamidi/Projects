import tkinter
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import time
from PIL import Image, ImageTk

answer = None


def amazon_parsing():

    def new_tab(URL):
        driver.execute_script("window.open('" + URL + "');")

    srvice = Service(executable_path="/Users/ahmee/OneDrive/Desktop/chromedriver_win32/chromedriver.exe")
    driver = webdriver.Chrome(service=srvice)
    url = "https://www.amazon.com/"
    driver.get(url)
    search_bar = driver.find_element(By.ID, value="twotabsearchtextbox")
    search_bar.send_keys(answer)
    search_button = driver.find_element(By.ID, value="nav-search-submit-button")
    search_button.click()
    keeps = []
    for elements in driver.find_elements(By.TAG_NAME, value="a"):
        if answer.lower() in (elements.text).lower():
            keeps = [elements.text]
        elif "$" in elements.text and len(keeps) == 3:
            keeps.append(elements.text)
            print(keeps[0] + "\n" + keeps[3].split("\n")[0])
        else:
            keeps.append(elements.text)


def user_input():

    def response():
        global answer
        answer = (name.get())
        name.set("")
        root.destroy()

    def clear():
        name.set("")

    root = tkinter.Tk()
    frame_input = tkinter.Frame()
    image_icon = ImageTk.PhotoImage(Image.open("/Users/ahmee/OneDrive/Documents/Shoppingbag.png").resize((40, 40)))
    frame_label = tkinter.Frame(height=150, width=200)
    frame_button = tkinter.Frame(height=30, width=130)
    name = tkinter.StringVar()
    question = tkinter.Label(text="Input Search Item", foreground="black", background="grey",
                             width=15, height=5, master=frame_label)
    question.place(x=38, y=35)
    logo = tkinter.Label(image=image_icon, master=frame_label)
    logo.place(x=160, y=20)
    start_function = tkinter.Button(text="Submit", height=1, width=6, command=response, master=frame_button
                                    , background="green", foreground="black")
    start_function.place(x=75, y=0)
    clear_button = tkinter.Button(text="Clear", height=1, width=5, command=clear, master=frame_button,
                                  background="red", foreground="black")
    clear_button.place(x=0, y=0)
    user_entry = tkinter.Entry(width=20, textvariable=name, master=frame_input)
    user_entry.pack()

    frame_label.pack()
    frame_input.pack()
    frame_button.pack()
    root.mainloop()


def main():
    user_input()
    while True:
        if answer is not None:
            amazon_parsing()
            break


main()
