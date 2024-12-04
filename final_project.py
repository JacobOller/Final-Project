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
apples = 3
former_key = None
number_of_rows = 13
number_of_columns = 17
coordinates_lst = []
list_of_characters_in_size = []
settings_accessed = None
timer = 300

''' Initial Screen: Includes button to play and button to change settings'''

def initial_screen():
    starting_window = tk.Tk()
    starting_window.geometry('500x500')
    starting_window.title("Starting Window")

    tk.Label(master=starting_window,
             text='Default Settings:').pack()
    tk.Label(master=starting_window,
             text='Difficulty: Medium\nGrid Size: 13x16\nApples: 3').pack()
    tk.Button(master=starting_window,
              text='Change Settings',
              command=settings).pack()
    tk.Button(master=starting_window,
              text='Play',
              command=initial_play).pack()
    return starting_window


''' Settings: Includes many buttons that are used to change individual settings;
 includes multiple smaller functions'''

def settings():
    global settings_accessed
    settings_accessed = True
    settings_window = tk.Tk()

    tk.Button(master=settings_window,
                            text="Easy Mode",
                            command=lambda: mode('easy'),
                            bg='green').pack()
    tk.Button(master=settings_window,
                            text="Medium Mode",
                            command=lambda: mode('medium'),
                            bg='yellow').pack()
    tk.Button(master=settings_window,
                            text="Hard Mode",
                            command=lambda: mode('hard'),
                            bg='red').pack()
    tk.Button(master=settings_window,
              text='10x10 Grid',
              command=lambda: grid_sizer('10x10')).pack()
    tk.Button(master=settings_window,
              text='10x12 Grid',
              command=lambda: grid_sizer('10x12')).pack()
    tk.Button(master=settings_window,
              text='12x12 Grid',
              command=lambda: grid_sizer('12x12')).pack()
    tk.Button(master=settings_window,
              text='10x14 Grid',
              command=lambda: grid_sizer('10x14')).pack()
    tk.Button(master=settings_window,
              text='13x16 Grid',
              command=lambda: grid_sizer('13x16')).pack()
    tk.Button(master=settings_window,
              text='12x18 Grid',
              command=lambda: grid_sizer('12x18')).pack()
    tk.Button(master=settings_window,
              text='1 Apple',
              command=lambda: apple_amount('1 apple')).pack()
    tk.Button(master=settings_window,
              text='2 Apples',
              command=lambda: apple_amount('2 apple')).pack()
    tk.Button(master=settings_window,
              text='3 Apples',
              command=lambda: apple_amount('3 apple')).pack()
    tk.Button(master=settings_window,
              text='4 Apples',
              command=lambda: apple_amount('4 apple')).pack()
    tk.Button(master=settings_window,
              text='5 Apples',
              command=lambda: apple_amount('5 apple')).pack()
    tk.Button(master=settings_window,
              text='Exit Settings',
              command=lambda: exit_settings(settings_window)).pack()

    return settings_window

def mode(difficulty):
    global timer
    if difficulty == 'easy':
        timer = 400 # number of miliseconds between each snake movement
    if difficulty == 'medium':
        timer = 300 # number of miliseconds between each snake movement
    if difficulty == 'hard':
        timer = 200 # number of miliseconds between each snake movement


def grid_sizer(selected_size):
    global number_of_rows
    global number_of_columns
    
    for i in selected_size:
        list_of_characters_in_size.append(i)
    number_of_rows = list_of_characters_in_size[0] + list_of_characters_in_size[1] # Takes the first 2 numbers (ex. 10 in 10x12)
    number_of_rows = int(number_of_rows)
    number_of_columns = list_of_characters_in_size[3] + list_of_characters_in_size[4] # Takes the last 2 numbers ( ex. 12 in 10x12 )
    number_of_columns = int(number_of_columns)


def apple_amount(amount):
    print('initiated')
    global apples
    for i in range(6):
        if amount == f'{i} apple':
            apples = i

'''Function that exits the settings'''
def exit_settings(settings_window):
    settings_window.destroy()

'''Function that exits the starting window; this exit initializes the logic for the game itself.'''
def initial_play():
    starting_window.destroy()

'''Main Function; First Creates Labels in a grid style (grid is based off of user input from settings), then every 300ms checks for a new keyboard
input with the check_for_new_key function; Calls update_label function to update each label acording
to the last key that has been pressed - This is tracked within the update_label function aswell as the 
check_for_new_key function; creates apples function (number of apples is based off of user input from settings), '''
def main():
    global window
    #starting_window.destroy()
    window = tk.Tk()
    x = 0

    for current_row in range(number_of_rows): # Maybe the current row
        for current_column in range(number_of_columns): # Maybe the current column
            x += 1
            frame = tk.Frame(
                master=window,
                relief=tk.SUNKEN,
                borderwidth=1
            )
            frame.grid(row=current_row, column=current_column)
            # if x % 2 == 0:
            #     label = tk.Label(master=frame, text='',
            #                     width=6, height=3, fg ='white',bg ='#47e322') # creates each light green label
            # else:
            #     label = tk.Label(master=frame, text='',
            #                     width=6, height=3, fg ='white',bg ='#1e8106') # creates each dark green label
            label = tk.Label(master=frame, text='',
                            width=6, height=3, fg ='white',bg ='black') # creates each black background label
            label.pack()
            lst = [label, current_row, current_column]
            squares[f"key{x}"] = lst
    window.after(300, check_for_new_key)
    update_label(lst)
   
    for apple in range(apples): #spawns in apples randomly based off of user input
        while True:
            apple_label = squares[f'key{random.randint(1, number_of_rows * number_of_columns)}'][0]     
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
                window.destroy()
            elif label.cget("bg") == 'red': #add length when snake gets an apple
                length += 1
                while True:
                    apple_label = squares[f'key{random.randint(1, number_of_rows * number_of_columns)}'][0]     
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
    global former_key

    if current_key == 'a':
        if former_key == 'd':
            position = position[0], position[1] + 1
            #check_coordinates(coordinates_lst)
            update_label(position)
        else:
            position = position[0], position[1] - 1
            former_key = 'a'
            update_label(position)

    elif current_key == 'd':
        if former_key == 'a':
            position = position[0], position[1] - 1
            update_label(position)
        else:
            position = position[0], position[1] + 1
            former_key = 'd'
            update_label(position)

    elif current_key == 'w':
        if former_key == 's':
            position = position[0] + 1, position[1]
            update_label(position)
        else:
            position = position[0] - 1, position[1]
            former_key = 'w'
            update_label(position)

    elif current_key == 's':
        if former_key == 'w':
            position = position[0] - 1, position[1]
            update_label(position)
        else:
            position = position[0] + 1, position[1]
            former_key = 's'
            update_label(position)

    window.after(timer, check_for_new_key) # Runs itself over and over constantly based on the difficulty that the user chose.


def delete_label(label):
    label.config(text='', width=6, height=3, fg='black', bg='black')


def death_window():
    death_window = tk.Tk()
    tk.Label(master=death_window,
             text=f'You died!\nScore of {length - 5}').pack()
    return death_window


if __name__ == '__main__':
    starting_window = initial_screen()
    starting_window.mainloop()

    window = main()
    window.mainloop()

    death_window = death_window()
    death_window.mainloop()