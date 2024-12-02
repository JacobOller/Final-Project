

"""
Zach Taylor
Jacob Ollerhead
CS 1210
Snake
"""

#need to use current_row and current_label stored in squares[] to save position of snake


import tkinter as tk
import time


direction = []
squares = {}


def main():
    window = main_grid()
    return window


def main_grid():
    window = tk.Tk()
    x = 0
    timer = 1000 # for updating the label, first label updates 1 second after window initially opens.

    for current_row in range(11): # Maybe the current row
        for current_label in range(20): # Maybe the current column
            x += 1
            frame = tk.Frame(
                master=window,
                relief=tk.SUNKEN,
                borderwidth=1
            ) # 53
            frame.grid(row=current_row, column=current_label)
            label = tk.Label(master=frame, text=f'{current_row}\n{current_label}',
                              width=6, height=3, fg ='white',bg ='black') # creates each black label
            # The reason we are using labels instead of labels is because we will be able to create
            # a function and bind each label to the function so when you press on an arrow key
            # A label will update with the color of the snake. 
            label.pack()
            lst = [label, current_row, current_label]
            squares[f"key{x}"] = lst
            
            
    global direction        
    direction = [5, 2]            
    update_label(lst, window)
    
    return window

def update_label(lst, window):
    window.bind('<Key>', lambda event: update_direction(event, lst, window))
    
    for values in squares.values():
        if values[1] == direction[0] and values[2] == direction[1]:
            #print(direction)
            label = values[0]
            lst = values[0], values[1], values[2]
            label.config(text='', width=6, height=3, fg='green', bg='green')
            window.after(300, update_label, lst, window)  
            
            


    return label

def delete_square(label, lst, window, next_square):
    label.config(text=f'', width=6, height=3, fg='black', bg='black')
    
def update_direction(event, lst, window):
    global direction

    if event.char == 'd':
        direction = lst[1], lst[2] + 1
    if event.char == 'a':
        direction = lst[1], lst[2] - 1
    if event.char == 'w':
        direction = lst[1] - 1, lst[2]
    if event.char == 's':
        direction = lst[1] + 1, lst[2]


if __name__ == '__main__':
    window = main()
    window.mainloop()

