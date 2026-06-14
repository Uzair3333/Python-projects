from tkinter import *
from tkinter import filedialog

def open_file():
    file_path = filedialog.askopenfilename()
    if file_path:
        with open(file_path, 'r') as file:
            text.delete('1.0', END)
            text.insert('1.0', file.read())

def save_file():
    file_path = filedialog.asksaveasfilename(defaultextension='.txt')
    if file_path:
        with open(file_path, 'w') as file:
            file.write(text.get('1.0', 'end-1c'))

root = Tk()
root.geometry("300x400")
root.title("THe Simple Text Editor")

text = Text(root)
text.pack(fill='both', expand=True)

menu_bar = Menu(root)
root.config(menu=menu_bar)

file_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="FIle", menu=file_menu)

file_menu.add_command(label="Open File", command=open_file)
file_menu.add_command(label="Save File", command=save_file)
file_menu.add_separator()

file_menu.add_command(label='Exit', command=root.quit)



root.mainloop()