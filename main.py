##UI For Application

import tkinter as tk


def print_func():
    print("THIS WAS SUCCESS")


#Array for button count and names
button_array = [
    ["Scan", print_func],
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

button_dict = {
    "Scan": print_func,
    "button2": "button2_func",
    "button3": "button3_func",
    "button4": "button4_func",
    "button5": "button5_func",
    "button6": "button6_func",
    "button7": "button7_func",
    "button8": "button8_func",
    "button9": "button9_func",
    "button10": "button10_func",
    "button11": "button11_func",
    "button12": "button12_func",
    "button13": "button13_func",
    "button14": "button14_func"
}

#Creating window
window = tk.Tk()
window.title("Application Title")
window.geometry("1280x720")


#Widgets
def create_buttons(button_array):
    for count, i in enumerate(button_array):
        #button = tk.Button(window, text=i[0], command=lambda i=i: i[1]) ##This "i=i" captures the i value at this point in the loop and stores it to use the function name, this is cool
        button = tk.Button(window, text=i[0], command=i[1]) 
        button.grid(row=count, column=0, padx=20, pady=10)
        
        
def create_dropdown(button_array, button_dict):
    default = tk.StringVar() ##this is the default value for the dropdown menu
    default.set(button_array[0][0]) ##this sets the default value to the first item in the array
    
    dropdownlist = []
    for i in button_array:
        dropdownlist.append(i[0])
    
    for count, i in enumerate(button_array):
        menu = tk.OptionMenu(window, default, *dropdownlist)
        # menu = tk.OptionMenu(window, default, *button_array[0]) ##this only shows the first entry in the array, not all first entries
        menu.config(width=50)
        menu.grid(row=0, column=2, padx=20, pady=10)
        
    go_button = tk.Button(window, text=("Go"), command=lambda: print(default.get()))
    # go_button = tk.Button(window, text=("Go"), command=lambda: button_dict[default.get()])
    go_button.grid(row=0, column=3, padx=20, pady=10)

    
create_buttons(button_array)
create_dropdown(button_array, button_dict)
# create_dictdropdown(button_dict)
window.mainloop()