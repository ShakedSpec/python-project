
from lib2to3.pgen2 import driver
from tkinter import Entry
from tkinter.tix import TEXT
from turtle import clear
import PySimpleGUI as sg
import Person
import Customer

from BankSystem import BankSystem
#sg.Window(title="my bank", layout=[[]], margins=(100, 50)).read()
daniel=Person.Person("daniel","ben ahron",3333,30,"050","no")
shaked=Customer.Customer("shaked","spector",308132281,30,"050","yes",4000,777)
bank=BankSystem()
bank.addCustomer(shaked)


layout = [ 
 
 [sg.Text("ID")],[sg.InputText('',key='-ID-')],
 [sg.Text("Account Number")],[sg.InputText(),sg.Button("Get Customer")],
 

 [sg.Text("Name: ", key='-NAME-')],
 [sg.Text("Balance", key='-BALANCE-')],
 [sg.Button("REFRESH")],
 [sg.Button("EXIT")]
 ]

# Create the window
window = sg.Window("Bank Appliction", layout)

# Create an event loop
while True:
    event, values = window.read()
    # End program if user closes window or
    # presses the EXIT button
    if event == "EXIT" or event == sg.WIN_CLOSED:
        break
    if event == "Get Customer":
       
        #open_window()
        customer_account_number=int(values[0])  

        customer=bank.get_customer_by_account_number(customer_account_number)
        
        window['-NAME-'].update('Name: '+ customer.firstName)
        window['-BALANCE-'].update('Balance: '+ str(customer.balance))
        
    if event=="REFRESH":
        window['-NAME-'].update('')
        window['-BALANCE-'].update('')
        window['-ID-'].update('')
        
    



    print(event) 

        
    
    
window.close()





