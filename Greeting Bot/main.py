from tkinter import *
from index import *

def greet():
    first_name= first_entry.get()
    last_name = last_entry.get()
    outupt = great_user(first_name, last_name)
    greeting_label.configure(text=outupt)

root = Tk()
root.geometry("400x350")
root.title("Greeting Bot")

top_frame = Frame(root)
top_frame.pack(fill='x')

top_frame.columnconfigure(0, weight=1)

header = Label(top_frame, text="Greeting Bot", font=('Ariel', 19), bg='blue', fg='white')
header.grid(row=0, column=0, columnspan=2)

main_frame = Frame(root)
main_frame.pack(fill='x')


first_label = Label(main_frame, text="First Name: ")
first_label.grid(row=0, column=0, padx=5, pady=5)



first_entry = Entry(main_frame)
first_entry.grid(row=0, column=1, padx=5, pady=5)

last_label = Label(main_frame, text="Last Name: ")
last_label.grid(row=1, column=0, padx=5, pady=5)

last_entry = Entry(main_frame)
last_entry.grid(row=1, column=1, padx=5, pady=5)


greeting_frame = Frame(root)
greeting_frame.pack(fill='x')

greeting_frame.columnconfigure(0, weight=1)

submit_btn = Button(greeting_frame, text='Submit', command=greet)
submit_btn.grid(row=0, column=0, columnspan=2, padx=5, pady=5)

greeting_label = Label(greeting_frame, text="Enter your name Above.", font=("Times New Roman", 16), bg="Black", fg="White")
greeting_label.grid(row=1, column=0, columnspan=2, padx=5, pady=5)

root.mainloop()