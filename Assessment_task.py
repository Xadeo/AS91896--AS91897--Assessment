#This program is going to store information such as customer full name Receipt number, 
#the item that is hired, how many of the item the customer has hired and prints it out within the GUI.

#This program will also have the ability to be able to delete a certain row of the printed information after the customer have return
#the hired item.

from tkinter import *
from tkinter import font
from tkinter.font import Font

#Defining font styles
def titlefonts():
    Font(
        family= "Times",
        size= 42,
        weight= "bold",
        slant= "roman"
        )

def normalfonts():
    Font(
        family= "Helvetica",
        size= 20
    )

#Creating my entry points for the user and buttons for the command
def setup_layout():
    Label(main_window, text="WELCOME", font= titlefonts).grid(row= 0, column= 1)
    Label(main_window, text="Please Enter the Following Details", font= normalfonts).grid(row= 1, column= 1)

    #Entry points
    Label(main_window, text="Customer Full Name", font= normalfonts).grid(row= 2, column= 0)
    entry_customer_name = Entry(main_window)
    entry_customer_name.grid(row= 2, column= 1)

    Label(main_window, text="Receipt Number", font= normalfonts).grid(row= 3, column= 0)
    entry_receipt_number = Entry(main_window)
    entry_receipt_number.grid(row= 3, column= 1)

    Label(main_window, text="Item Hired", font= normalfonts).grid(row= 4, column= 0)
    entry_item_hired = Entry(main_window)
    entry_item_hired.grid(row = 4, column= 1)

    Label(main_window, text="Number Hired", font= normalfonts).grid(row= 5, column= 0)
    entry_number_hired = Entry(main_window)
    entry_number_hired.grid(row = 5, column= 1)
    Button(main_window, text="Append Details", font= normalfonts).grid(row= 6, column= 1, sticky= W)
    Button(main_window, text="Print Details", font= normalfonts).grid(row= 6, column= 1, sticky= E)

    Label(main_window, text="Row Number", font= normalfonts).grid(row= 2, column= 2)
    delete_row = Entry(main_window)
    delete_row.grid(row= 2, column= 3)
    Button(main_window, text="Delete", font= normalfonts).grid(row= 3, column= 3, sticky= E)
    Button(main_window, text= "Quit", font= normalfonts).grid(row= 0, column= 3, sticky= E)
    

#This will start the program and also have the main start of everything such as a list for customer details and total entries
def main():
    global main_window
    global customer_details, total_entries, main_window
    customer_details = []
    total_entries = 0
    main_window = Tk()
    setup_layout()
    main_window.mainloop()
main()