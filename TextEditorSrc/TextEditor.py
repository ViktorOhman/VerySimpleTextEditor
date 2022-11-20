#Import libraries
import tkinter as tk
from tkinter import *
import pyautogui
import os
#Create a new window using tkinter
window = Tk()
window.geometry('950x650+550+275') #Give the window height, widht and position
window.title("Window...")
window.resizable(False,False) #Make it unresizable
#Make a user input area that scales with the screen
text_box = tk.Text()
text_box.pack(side='top',fill='both',expand=True)
#Make a function for inserting text from the last opend file to the editor
def insert_lastFile(lastFileText):
    text_box.insert('1.0', lastFileText)
#Make a function for writting a new file or updating a already existing one
def writeToFile(content):
    fileName = pyautogui.prompt(text='What is the name off the file', title='FileName') #Asking for the name of the file
    #Write the text into a file
    with open('Text/'+fileName+'.txt', 'w') as textFile:
        textFile.write(content)
    #Write to the Last Opend File Registry(Important for later)
    with open("Text\lastFileRegistry.key", 'w') as registry:
        registry.write('Text/'+fileName+'.txt')
#Make a function for geting input from the window
def retrieve_input():
    input = text_box.get("1.0",END)
    return input
#Make a function that asks the user if they really want to close the window
def onClose():
    wantToQuit = pyautogui.confirm(text='Are you sure you want to quit \n You may unsaved changes',title='Confirm',buttons=['YES','NO'])
    if wantToQuit == 'YES':
        exit()
#Make a function for opening the last opend file if a Last Opend File Registry exists
def restore():
    for file in os.listdir('Text'):
        if file == "lastFileRegistry.key":
            with open('Text\lastFileRegistry.key', 'r') as Registry: #Open the Last Opend File Registry
                    R_lastFile = Registry.read()
                    wantToRestore = pyautogui.confirm(text='Do You want to open your latest document?',title='?', buttons=['YES','NO'])
                    if wantToRestore == 'YES':
                        with open(R_lastFile, 'r') as lastFile:
                            lastFileContense = lastFile.read()
                        insert_lastFile(lastFileContense)
#Make a function that saves the text
def saveText(saveWindow,save):
    if saveWindow: #Check if we want to save using a window or not
        save = pyautogui.confirm(text='', title='Save', buttons=['SAVE']) #<-The save button
        if save == 'SAVE':
            content = retrieve_input()
            writeToFile(content)
            saveText(True,'')
    if save == 'SAVE':
        content = retrieve_input()
        writeToFile(content)


window.withdraw() #Hide the editor window
restore() #Ask if the user wants to open thier last opend file
window.deiconify() #Show the editor window again
window.lift() #Make the editor window come out on top
window.protocol('WM_DELETE_WINDOW', onClose) #Constantly check if the X Buton is pressed by lookingat windows protocols
saveText(True,'') #Show the save button

window.mainloop() #Tkinter's main loop
