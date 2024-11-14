import tkinter as tk

window = tk.Tk()

for current_row in range(11):
    for current_column in range(16):
        frame = tk.Frame(
            master=window,
            relief=tk.SUNKEN,
            borderwidth=1
        )
        frame.grid(row=current_row, column=current_column)
        label = tk.Label(master=frame, text=f'row {current_row}\ncolumn {current_column}')
        label.pack()


if __name__ == '__main__':
    window.mainloop()