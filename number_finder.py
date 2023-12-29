import tkinter as tk
from tkinter import *
#from tkinter import messagebox #libary for messagebox
from tkinter import filedialog, Entry, StringVar
import re

def openFile():
    filepath = filedialog.askopenfilename(
        title="Open file, okey?",
        filetypes=(("text files", "*.txt"),
        ("all files", "*.*"))
    )
    with open(filepath, 'r') as file:
            global numbers
            global words
            numbers = []
            words = []
            for line in file:
                matches = re.findall(r'\d+', line)
                for match in matches:
                    number = int(match)
                    numbers.append(number)
                matches = re.findall(r'\b\w+\b', line)
                for match in matches:
                    word = match
                    words.append(word)

def openReset():
    label.config(text="This function is not ready yet.")


window = tk.Tk()
window.geometry("500x500") #Size of the programs window
menubar = Menu(window) #Menubar
window.config(menu=menubar)


def on_button1_click():
    openFile()
    #after opening the file new options appear on the window
    global button3
    global button4
    global button5
    button3 = tk.Button(window, text="Find the biggest number", command=on_button3_click)
    button3.pack()
    button4 = tk.Button(window, text="Find the smallest number", command=on_button4_click)
    button4.pack()
    button5 = tk.Button(window, text="Search the number or word you want", command=findNumber)
    button5.pack()
def on_button2_click():
    button3.pack_forget()
    button4.pack_forget()
    label.config(text="Open new file. ")

#Find the biggest number in your file
def on_button3_click():
    largest_number = max(numbers)
    label.config(text="The biggest number is: " +str(largest_number))
    button3.pack_forget()

#Find the smallest number on the file
def on_button4_click():
    smallest_number = min(numbers)
    label.config(text="The smallest number is: " + str(smallest_number))
    button4.pack_forget()

#Type your number or word and check if its in the file
def findNumber():
    button3.pack_forget()
    button4.pack_forget()
    button5.pack_forget()

    find_button.pack()
    entry.pack()

    search_value = entry_var.get()
    try:
        search_number = int(search_value)
        if search_number in numbers:
            inc = 0
            for i in numbers:
                if (i == search_number):
                    inc = inc + 1
            label.config(text="We found: " + str(search_number))
            label2.config(text="Your number/word was found this many times: " + str(inc))
            label.update_idletasks()
        else:
            label.config(text="Nothing found :( ")
            label2.config(text="")
            label.update_idletasks()
    except ValueError:
        if search_value in words:
            inc2 = 0
            for i in words:
                if (i == search_value):
                    inc2 = inc2 + 1
            label.config(text="We found: " + search_value)
            label2.config(text="Your number/word was found this many times: " + str(inc2))
            label.update_idletasks()
        else:
            label.config(text="Nothing found :( ")
            label2.config(text="")
            label.update_idletasks()


#Menubar
fileMenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="File", menu=fileMenu)
fileMenu.add_command(label="Open", command=on_button1_click)
fileMenu.add_command(label="Reset", command=on_button2_click)
fileMenu.add_separator()
fileMenu.add_command(label="Exit", command=quit)


# First button to open files
button1 = tk.Button(window, text="Open File", command=on_button1_click)
button1.pack()

# Test button, prints message
button2 = tk.Button(window, text="Reset", command=on_button2_click)
button2.pack()

#Welcome text
label = tk.Label(window, text="Welcome. Now open your file.")
label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
label2 = tk.Label(window, text="")
label2.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
label.pack()

#global entry_var
entry_var = StringVar()
entry = Entry(window, textvariable=entry_var)
find_button = Button(window, text="Search", command=findNumber)

window.title("Number Finder program by Mnrds 2023")
window.mainloop()
