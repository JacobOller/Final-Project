"""
Zach Taylor
Jacob Ollerhead
CS 1210
Snake
"""

#need to use current_row and current_column stored in squares[] to save position of snake


import tkinter as tk
import time
import random

direction = []
squares = {}
current_key = None
position = [5, 2]
length = 5
apples = 5

def starting_window():
    starting_window = tk.Tk()
    starting_window.title("Starting Screen")
    tk.Label(master=starting_window, 
                          text="Welcome to Snake! Choose your difficulty below.").pack()
    tk.Button(master=starting_window,
                            text="Easy Mode",
                            command=lambda: mode('easy')).pack()
    tk.Button(master=starting_window,
                            text="Medium Mode",
                            command=lambda: mode('medium')).pack()
    tk.Button(master=starting_window,
                            text="Hard Mode",
                            command=lambda: mode('hard')).pack()
    return starting_window


def mode(difficulty):
    starting_window.destroy() # Destroys the starting window, initializing the main window.
    global timer
    if difficulty == 'easy':
        timer = 400 # number of miliseconds between each snake movement
    if difficulty == 'medium':
        timer = 300 # number of miliseconds between each snake movement
    if difficulty == 'hard':
        timer = 200 # number of miliseconds between each snake movement

def main():
    global window
    window = tk.Tk()
    x = 0
    timer = 1000 # for updating the label, first label updates 1 second after window initially opens.

    for current_row in range(11): # Maybe the current row
        for current_column in range(20): # Maybe the current column
            x += 1
            frame = tk.Frame(
                master=window,
                relief=tk.SUNKEN,
                borderwidth=1
            )
            frame.grid(row=current_row, column=current_column)
            label = tk.Label(master=frame, text=d'',
                              width=6, height=3, fg ='white',bg ='black') # creates each black label
            label.pack()
            lst = [label, current_row, current_column]
            squares[f"key{x}"] = lst
    window.after(300, check_for_new_key)
    update_label(lst)
   
    for apple in range(apples): #spawn in apples randomly 
        while True:
            apple_label = squares[f'key{random.randint(1, 220)}'][0]     
            if apple_label.cget("bg") != 'green' and apple_label.cget("bg") != 'red':
                break
        apple_label.config(text='', width=6, height=3, fg='red', bg='red')
    
    return window


def update_label(position):
    global window
    global timer
    global length

    window.bind('<Key>', on_key_press)
    for values in squares.values():
        if values[1] == position[0] and values[2] == position[1]: # if the current x coordinate in the loop == the current direction
            # and if the current y coordinate in the loop == the current direction
            # This is for finding the correct label to update after updating the direction.
            label = values[0] # Once the above if statement finds the correct coordinates, it sets value of label = the correct label.
            x_coordinate = values[1]
            y_coordinate = values[2]
            lst = label, x_coordinate, y_coordinate # once above if statement finds correct coordinates, it sets value of lst = label, x, y
            
            if label.cget("bg") == 'green': #snake dies because it hits itself
                print('death')
            elif label.cget("bg") == 'red': #add length when snake gets an apple
                length += 1
                while True:
                    apple_label = squares[f'key{random.randint(1, 220)}'][0]     
                    if apple_label.cget("bg") != 'green' and apple_label.cget("bg") != 'red':
                        break
                apple_label.config(text='', width=6, height=3, fg='red', bg='red')
                label.config(text='', width=6, height=3, fg='green', bg='green')
                window.after(timer * length, delete_label, label) # we can use the after and a timer to delay the deletion of a square making the snake longer
            elif label.cget("bg") == 'black':
                label.config(text='', width=6, height=3, fg='green', bg='green')
                window.after(timer * length, delete_label, label) # we can use the after and a timer to delay the deletion of a square making the snake longer


def on_key_press(event):
    global current_key
    current_key = event.keysym
    # bind function returns none, so we made current_key a global variable instead of returning it

def check_for_new_key():
    #global current_key
    global position

    if current_key == 'a':
        position = position[0], position[1] - 1
        update_label(position)

    elif current_key == 'd':
        position = position[0], position[1] + 1
        update_label(position)

    elif current_key == 'w':
        position = position[0] - 1, position[1]
        update_label(position)

    elif current_key == 's':
        position = position[0] + 1, position[1]
        update_label(position)

    window.after(timer, check_for_new_key) # Runs itself over and over constantly based on the difficulty that the user chose.


def delete_label(label):
    label.config(text='', width=6, height=3, fg='black', bg='black')


if __name__ == '__main__':
    starting_window = starting_window()
    starting_window.mainloop()
    window = main()
    window.mainloop()
