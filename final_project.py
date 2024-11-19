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


def movement():
    time.sleep(snake_speed)
    movement()


def main_grid():
    window = tk.Tk()
    x = 0
    timer = 1000 # for updating the label, first label updates 1 second after window initially opens.

    for current_row in range(11): # Maybe the current row
        for current_label in range(21): # Maybe the current column
            x += 1
            frame = tk.Frame(
                master=window,
                relief=tk.SUNKEN,
                borderwidth=1
            )
            frame.grid(row=current_row, column=current_label)
            label = tk.Label(master=frame, text=f'{current_row}\n{current_label}',
                              width=6, height=3, fg ='white',bg ='black') # creates each black label
            label.pack()
            squares[f"key{x}"] = label

    for current_label in squares.keys(): # Iterates through each label from the squares dictionary
        window.after(timer, update_label, squares[current_label])  # updates label from the function (update_label)
        timer += 1000  # 1 second timer between each update (will probably need to make this faster, maybe .5 sec?)
    return window


def update_label(label):
    label.config(text=f'{label}', width=6, height=3, fg ='black',bg ='red') # This is the actual updating of each label
    return label


if __name__ == '__main__':
    snake_pos = snake_spawn
    window = main()
    window.mainloop()
    print(squares)