##UI For Application

import tkinter as tk

#Array for button count and names
button_array = [
    ["Scan", "scan_func"],
    ["button2", "button2_func"],
    ["button3", "button3_func"],
    ["button4", "button4_func"],
    ["button5", "button5_func"],
    ["button6", "button6_func"],
    ["button7", "button7_func"],
    ["button8", "button8_func"],
    ["button9", "button9_func"],
    ["button10", "button10_func"],
    ["button11", "button11_func"],
    ["button12", "button12_func"],
    ["button13", "button13_func"],
    ["button14", "button14_func"]
    ]


#Creating window
window = tk.Tk()
window.title("Application Title")
window.geometry("1280x720")


#Widgets
def create_buttons(button_array):
    for count, i in enumerate(button_array):
        scanbutton = tk.Button(window, text=i[0], command=lambda i=i, count=count: create_textlabels(count, i)) ##This "i=i" captures the i value at this point in the loop and stores it to use the function name, this is cool
        scanbutton.grid(row=count, column=0, padx=20, pady=10)
        
        
def create_textlabels(count, button_array):
    ##count is the int
    ##button_array is a list here when passing "i" into the func
    label = tk.Label(window, text=button_array[0])
    label.grid(row=count, column=1, padx=20, pady=10)
      
    
create_buttons(button_array)
window.mainloop()