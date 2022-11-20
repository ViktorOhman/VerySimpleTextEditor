import tkinter as tk
from tkinter import *
import pyautogui
import os

window = Tk()
window.geometry('950x650+550+275')
window.title("Window...")
window.resizable(False,False)

text_box = tk.Text()
text_box.pack(side='top',fill='both',expand=True)

def insert_lastFile(RegistryExist,lastFileText):
    if RegistryExist:
        text_box.insert('1.0', lastFileText)

def writeToFile(content):
    fileName = pyautogui.prompt(text='What shuold the name off the file be?', title='FileName')
    with open('Text/'+fileName+'.txt', 'w') as textFile:
        textFile.write(content)
    with open("Text\lastFileRegistry.key", 'w') as registry:
        registry.write('Text/'+fileName+'.txt')

def retrieve_input():
    input = text_box.get("1.0",END)
    return input

def onClose():
    wantToQuit = pyautogui.confirm(text='Are you sure you want to quit \n You may unsaved changes',title='Confirm',buttons=['YES','NO'])
    if wantToQuit == 'YES':
        exit()

def restore():
    for file in os.listdir('Text'):
        if file == "lastFileRegistry.key":
            with open('Text\lastFileRegistry.key', 'r') as Registry:
                    R_lastFile = Registry.read()
                    wantToRestore = pyautogui.confirm(text='Do You want to open your latest document?',title='?', buttons=['YES','NO'])
                    if wantToRestore == 'YES':
                        with open(R_lastFile, 'r') as lastFile:
                            lastFileContense = lastFile.read()
                        insert_lastFile(True, lastFileContense)

def saveText(saveWindow,save):
    if saveWindow:
        save = pyautogui.confirm(text='', title='Save', buttons=['SAVE'])
        if save == 'SAVE':
            content = retrieve_input()
            writeToFile(content)
            saveText(True,'')
    if save == 'SAVE':
        content = retrieve_input()
        writeToFile(content)


window.withdraw()
restore()
window.deiconify()
window.lift()
window.protocol('WM_DELETE_WINDOW', onClose)
saveText(True,'')

window.mainloop()
