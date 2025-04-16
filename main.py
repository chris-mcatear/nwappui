##UI For Application

import tkinter as tk

#Creating window
window = tk.Tk()
window.title("Application Title")
window.geometry("1280x720")

#Widgets
scanbutton = tk.Button(window, text="Scan")#
scanbutton.grid(row=0, column=0)

window.mainloop()