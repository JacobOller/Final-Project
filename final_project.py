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


squares = {}
coordinates_lst = []
position = [5, 2]
length = 5
apples = 1
timer = 300
number_of_rows = 13
number_of_columns = 17
current_key = None
former_key = None
difficulty = 'medium'
dimensions = '13x17'


def center_window(window, width, height):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    screen_x = (screen_width // 2) - (width // 2)
    screen_y = (screen_height // 2) - (height // 2)
    window.geometry(f'{width}x{height}+{screen_x}+{screen_y}')
    return

'''Includes button to play and button to change settings'''
def initial_screen():
    global difficulty_label
    global dimensions_label
    global apples_label

    starting_window = tk.Tk()
    center_window(starting_window, 600, 500)

    starting_window.title("Starting Window")
    starting_window.config(bg='#1fa6a8')

    tk.Label(master=starting_window, # Title
             text='SNAKE',
             font=('Castellar', 50, 'bold'),
             width=10,
             padx=10,
             pady=10,
             bg='blue').pack(pady=(0,10))
    tk.Label(master=starting_window, # Current Settings
             text='Current Settings:',
             font=('Unispace', 22),
             padx=10,
             pady=10,
             bg='#1fa6a8').pack()
    difficulty_label = tk.Label(master=starting_window,
             text=f'Difficulty: {difficulty}',
             font=('Unispace', 14),
             bg='#1fa6a8')
    difficulty_label.pack()
    dimensions_label = tk.Label(master=starting_window,
            text=f'Grid Size: {dimensions}',
            font=('Unispace', 14),
            bg='#1fa6a8')
    dimensions_label.pack()
    apples_label = tk.Label(master=starting_window,
            text=f'Apples: {apples}',
            font=('Unispace', 14),
            bg='#1fa6a8')
    apples_label.pack()
    tk.Button(master=starting_window,
              text='Change Settings',
              font=('Unispace', 17),
              command=settings).pack(pady=(50,0))
    tk.Button(master=starting_window,
              text='Play',
              font=('Unispace', 30),
              bg='blue',
              command=initial_play).pack(pady=(15,0))
    return starting_window


'''Includes many buttons that are used to change individual settings;
 includes multiple smaller functions'''
def settings():
    settings_window = tk.Tk()

    tk.Button(master=settings_window,
                            text="Easy Mode",
                            command=lambda: mode('easy', difficulty_label),
                            #command=(mode,'easy'),
                            bg='green').pack()
    tk.Button(master=settings_window,
                            text="Medium Mode",
                            command=lambda: mode('medium', difficulty_label),
                            #command=(mode,'medium'),
                            bg='yellow').pack()
    tk.Button(master=settings_window,
                            text="Hard Mode",
                            command=lambda: mode('hard', difficulty_label),
                            #command=(mode,'hard'),
                            bg='red').pack()
    tk.Button(master=settings_window,
              text='10x10 Grid',
              command=lambda: grid_sizer('10x10', dimensions_label)).pack()
    tk.Button(master=settings_window,
              text='10x12 Grid',
              command=lambda: grid_sizer('10x12', dimensions_label)).pack()
    tk.Button(master=settings_window,
              text='12x12 Grid',
              command=lambda: grid_sizer('12x12', dimensions_label)).pack()
    tk.Button(master=settings_window,
              text='10x14 Grid',
              command=lambda: grid_sizer('10x14', dimensions_label)).pack()
    tk.Button(master=settings_window,
              text='13x16 Grid',
              command=lambda: grid_sizer('13x16', dimensions_label)).pack()
    tk.Button(master=settings_window,
              text='12x18 Grid',
              command=lambda: grid_sizer('12x18', dimensions_label)).pack()
    tk.Button(master=settings_window,
              text='1 Apple',
              command=lambda: apple_amount('1 apple', apples_label)).pack()
    tk.Button(master=settings_window,
              text='2 Apples',
              command=lambda: apple_amount('2 apple', apples_label)).pack()
    tk.Button(master=settings_window,
              text='3 Apples',
              command=lambda: apple_amount('3 apple', apples_label)).pack()
    tk.Button(master=settings_window,
              text='4 Apples',
              command=lambda: apple_amount('4 apple', apples_label)).pack()
    tk.Button(master=settings_window,
              text='5 Apples',
              command=lambda: apple_amount('5 apple', apples_label)).pack()
    tk.Button(master=settings_window,
              text='Exit Settings',
              command=lambda: exit_settings(settings_window)).pack()

    return settings_window


'''Part of Settings'''
def mode(selected_diff, label):
    global timer
    global difficulty
    if difficulty == None:
        return 'medium'
    if selected_diff == 'easy':
        timer = 400 # number of miliseconds between each snake movement
    if selected_diff == 'medium':
        timer = 300 # number of miliseconds between each snake movement
    if selected_diff == 'hard':
        timer = 200 # number of miliseconds between each snake movement
    difficulty = selected_diff
    difficulty_label_update(label)


def difficulty_label_update(label):
    label.config(text=f'Difficulty: {difficulty}')


'''Part of Settings'''
def grid_sizer(selected_size, label):
    list_of_characters_in_size = []
    global dimensions

    for i in selected_size:
        list_of_characters_in_size.append(i)
    number_of_rows = list_of_characters_in_size[0] + list_of_characters_in_size[1] # Takes the first 2 numbers (ex. 10 in 10x12)
    number_of_rows = int(number_of_rows)
    number_of_columns = list_of_characters_in_size[3] + list_of_characters_in_size[4] # Takes the last 2 numbers ( ex. 12 in 10x12 )
    number_of_columns = int(number_of_columns)

    dimensions = f'{number_of_rows}x{number_of_columns}'
    dimensions_label_update(label)


def dimensions_label_update(label):
    label.config(text=f'Grid Size: {dimensions}')


'''Part of Settings'''
def apple_amount(amount, label):
    global apples
    for i in range(6):
        if amount == f'{i} apple':
            apples = i
    apples_label_update(label)


def apples_label_update(label):
    label.config(text=f'Apples: {apples}')


'''Function that exits the settings'''
def exit_settings(settings_window):
    settings_window.destroy()

'''Function that exits the starting window; this exit initializes the logic for the game itself.'''
def initial_play():
    starting_window.destroy()

'''Main Function; First Creates Labels in a grid style (grid is based off of user input from settings), then every 300ms checks for a new keyboard
input with the check_for_new_key function; Calls update_label function to update each label acording
to the last key that has been pressed - This is tracked within the update_label function aswell as the 
check_for_new_key function; creates apples function (number of apples is based off of user input from settings).'''
def main():
    global window
    global x
    x = 0

    window = tk.Tk()
    center_window(window, number_of_columns*50,number_of_rows*53)
    temp_window()

    for current_row in range(number_of_rows): # Maybe the current row
        for current_column in range(number_of_columns): # Maybe the current column
            x += 1
            frame = tk.Frame(
                master=window,
                relief=tk.SUNKEN,
                borderwidth=1
            )
            frame.grid(row=current_row, column=current_column)
            label = tk.Label(master=frame, text='',
                            width=6, height=3, fg ='white',bg ='#47e322') # creates each light green label
            label.pack()

            lst = [label, current_row, current_column]
            squares[f"key{x}"] = lst
    window.after(300, check_for_new_key)
    update_label(lst)
   
    for apple in range(apples): #spawns in apples randomly based off of user input
        while True:
            apple_label = squares[f'key{random.randint(1, number_of_rows * number_of_columns)}'][0]     
            if apple_label.cget("bg") != 'blue' and apple_label.cget("bg") != 'red':
                break
        apple_label.config(text='', width=6, height=3, fg='red', bg='red')
    
    return window


'''Called within main; physically updates label based off of keyboard input by calling on_key_press function;
checks if snake runs into itself - if it does then initiates death screen; creates the apples and checks if
 snake gets an apple - if it does then adds 1 to the length of the snake through creating a new
 blue label; calls delete_label function to maintain
 the correct length of the snake constantly; '''
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
            
            if label.cget("bg") == 'blue': #snake dies because it hits itself
                print('death')
                window.destroy()
            elif label.cget("bg") == 'red': #add length when snake gets an apple
                length += 1
                while True:
                    apple_label = squares[f'key{random.randint(1, number_of_rows * number_of_columns)}'][0]     
                    if apple_label.cget("bg") != 'blue' and apple_label.cget("bg") != 'red':
                        break
                apple_label.config(text='', width=6, height=3, fg='red', bg='red')
                label.config(text='', width=6, height=3, fg='blue', bg='blue')
                window.after(timer * length, delete_label, label) # we can use the after and a timer to delay the deletion of a square making the snake longer
            elif label.cget("bg") == '#47e322':
                label.config(text='', width=6, height=3, fg='blue', bg='blue')
                window.after(timer * length, delete_label, label) # we can use the after and a timer to delay the deletion of a square making the snake longer


'''Function that is called from update_label everytime a new key is pressed and sets current_key = the key'''
def on_key_press(event):
    global current_key
    current_key = event.keysym
    # bind function returns none, so we made current_key a global variable instead of returning it


'''Function that is called from main, is constantly checking for a new keyboard input update; when it recieves a new
key, checks whether the new key is the opposite key of the former key (a is opposite of d, s is opposite of w) in
order to ensure that the snake moves correctly; calls update_label to update the future labels to move in the correct direction
until a new key is pressed, then the direction will change based off of that key.
'''
def check_for_new_key():
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


'''Function that ensures that the length of the snake is correct by constantly changing the color of labels
from the color of the snake to the background based off of the snake's movement'''
def delete_label(label):
    #label.config(text='', width=6, height=3, fg='black', bg='black')
    # if label.cget("bg") == '#47e322':
    label.config(text='', width=6, height=3, fg='#47e322', bg='#47e322')
    # else:
    #     label.config(text='', width=6, height=3, fg='#1e8106', bg='#1e8106')


def temp_window():
    temp_win = tk.Tk()
    temp_win.config(bg='#d058f0')
    center_window(temp_win, 100, 50)
    temp_win.focus()
    temp_win.attributes('-topmost', True)
    tk.Label(master=temp_win,
            text='Press a key to start\n(WASD)',
            bg='#d058f0',
            font=('Unispace', 6),).pack(expand=True)
    destroy_temp(temp_win)
    

def destroy_temp(temp_win):
    if current_key == 'w' or current_key == 'a' or current_key == 's' or current_key == 'd':
        temp_win.destroy()
        return
    temp_win.after(100, destroy_temp, temp_win)


'''Function that creates the death window; is initiated from update_label'''
def death_window():
    death_window = tk.Tk()
    death_window.config(bg='#d058f0')
    center_window(death_window, 100, 50)
    tk.Label(master=death_window,
            text=f'You died!\nScore of {length - 5}',
            bg='#d058f0',
            font=('Unispace', 8),).pack(expand=True)
    return death_window


if __name__ == '__main__':
    starting_window = initial_screen()
    starting_window.mainloop()

    window = main()
    window.mainloop()

    death_window = death_window()
    death_window.mainloop()