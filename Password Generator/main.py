from tkinter import *
from index import *

def choices():
    # 1. Get the length from the UI
    password_length = length.get()
    
    # 2. Run the logic from index.py
    result = generate_func(password_length, num, upp, sym)
    
    # 3. Update the UI Output
    output_entry.delete(0, END)
    output_entry.insert(0, result)

root = Tk()
root.geometry("350x450")
root.title("Password Generator V1.0")

# --- Top Frame ---
top_frame = Frame(root, bg='lightblue', pady=10)
top_frame.pack(fill='x')

title = Label(top_frame, text="Secure Pass Gen", font=("Times New Roman", 18, "bold"), bg='lightblue')
title.pack()

# --- Main Frame ---
main_frame = Frame(root, padx=20, pady=20)
main_frame.pack(fill='both', expand=True)

Label(main_frame, text="Password Length:").grid(row=0, column=0, sticky='w', pady=5)
length = Entry(main_frame)
length.grid(row=0, column=1, pady=5, padx=10)

# Checkbutton Variables
num = IntVar()
sym = IntVar()
upp = IntVar()

Checkbutton(main_frame, text="Include Numbers", variable=num).grid(row=1, column=0, columnspan=2, sticky='w')
Checkbutton(main_frame, text="Include Symbols", variable=sym).grid(row=2, column=0, columnspan=2, sticky='w')
Checkbutton(main_frame, text="Include Uppercase", variable=upp).grid(row=3, column=0, columnspan=2, sticky='w')

# Generate Button
gen_btn = Button(main_frame, text="Generate Password", bg="#4CAF50", fg="white", command=choices)
gen_btn.grid(row=4, column=0, columnspan=2, pady=20, sticky='swe')

# Output Field
Label(main_frame, text="Your Result:").grid(row=5, column=0, columnspan=2)
output_entry = Entry(main_frame, font=("Courier", 12), justify='center')
output_entry.grid(row=6, column=0, columnspan=2, sticky='we', pady=5)

root.mainloop()