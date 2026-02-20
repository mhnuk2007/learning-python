""" Event-Driven Example - Button Click (Tkinter GUI) """

import tkinter as tk

def on_button_click():
    print("Button clicked!")

root = tk.Tk()
root.title("Event-Driven GUI Example")

button = tk.Button(root, text="Click Me", command=on_button_click)
button.pack(pady=20)

root.mainloop()