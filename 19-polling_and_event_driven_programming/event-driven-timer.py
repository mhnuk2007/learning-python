""" Event-Driven Example - Timer Events """

import tkinter as tk

def tick():
    print("Tick")
    root.after(1000, tick)  # schedule next tick after 1 second

root = tk.Tk()
root.title("Timer Event Example")

tick()  # start the timer
root.mainloop()