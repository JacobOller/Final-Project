"""
Zach Taylor
Jacob Ollerhead
CS 1210
Snake
"""
import tkinter as tk
import time

snake_speed = 0.1
direction = (1, -1)
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
    every_20 = 10

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
            label.pack()
            squares[f"key{x}"] = label

    for current_label in squares.keys(): # Iterates through each label from the squares dictionary
        if every_20 % 20 == 0:
            window.after(timer, update_label, squares[current_label])  # updates label from the function (update_label)
            timer += 300  # .3 second timer between each update (Can easily be adjusted faster/slower)
        every_20 += 1

    return window


def update_label(label):
    label.config(text=f'{label}', width=6, height=3, fg ='black',bg ='red') # This is the actual updating of each label
    return label

def movement():
    


if __name__ == '__main__':
    snake_pos = snake_spawn
    window = main()
    window.mainloop()
    print(type(squares))