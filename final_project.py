
"""
Zach Taylor
Jacob Ollerhead
CS 1210
Snake
"""

#need to use current_row and current_label stored in squares[] to save position of snake


import tkinter as tk
import time

snake_speed = 0.1
snake_spawn = (1, 10)
snake_pos = []
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
            
    starting_square = [5, 2]            
    update_label(lst, window, starting_square)
    
    return window

def update_label(lst, window, next_square):
    for values in squares.values():
        if values[1] == next_square[0] and values[2] == next_square[1]:
            label = values[0]
            lst = values[0], values[1], values[2]
    window.bind('<Key>', lambda event: update_direction(event, lst, window))
            
            
    label.config(text='', width=6, height=3, fg='green', bg='green')
    window.after(300, delete_square, label, lst, window, next_square)


    return label

def delete_square(label, lst, window, next_square):
    label.config(text=f'', width=6, height=3, fg='black', bg='black')
    
def update_direction(event, lst, window):
    direction = [0, 0]
    print(lst)
    
    if event.char == 'd':
            #key_pressed = 'd'
            direction = lst[1], lst[2] + 1
            print(direction)
            window.after(300, iteration, direction, lst, window)
    if event.char == 'a':
        direction = lst[1], lst[2] - 1
    if event.char == 'w':
        direction = lst[1] - 1, lst[2]
    if event.char == 's':
        direction = lst[1] + 1, lst[2]
    
    update_label(lst, window, direction)
    # need to add milisecond wait for this function


def iteration(direction, lst, window):
        direction = direction[0], direction[1] + 1
        print(direction)
        update_label(lst, window, direction)
        window.after(300, iteration, direction, lst, window)

    
    # if key_pressed == 'a':
    #     direction = lst[1], lst[2] - 1
    #     print(direction)
    #     return direction
    # if key_pressed == 'w':
    #     direction = lst[1] - 1, lst[2]
    #     print(direction)
    #     return direction
    # if key_pressed == 's':
    #     direction = lst[1] + 1, lst[2]
    #     print(direction)
    #     return direction
   

if __name__ == '__main__':
    window = main()
    window.mainloop()