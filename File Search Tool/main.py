from tkinter import *
from index import *

def main_func():
    search_path = path_entry.get()
    search_keyword = keyword_entry.get()
    result_files = search_file(search_path, search_keyword)
    for file in result_files:
        output_list.insert(END, file)


root = Tk()
root.geometry("300x400")
root.title("FIle Search Tool")

top_frame = Frame(root)
top_frame.pack(fill='x')

top_frame.columnconfigure(0, weight=1)

header = Label(top_frame, text="File Search Tool", font=('Ariel', 15), bg="Black", fg='White')
header.grid(row=0, column=0, columnspan=2, padx=5, pady=5)

main_frame = Frame(root)
main_frame.pack(fill='x')

path_label = Label(main_frame, text='Directory Path: ')
path_label.grid(row=0, column=0, padx=5, pady=5)

path_entry = Entry(main_frame)
path_entry.grid(row=0, column=1, padx=5, pady=5)

keyword_label = Label(main_frame, text='File keyword: ')
keyword_label.grid(row=1, column=0, padx=5, pady=5)

keyword_entry = Entry(main_frame)
keyword_entry.grid(row=1, column=1, padx=5, pady=5)

btn = Button(main_frame, text='Search', command=main_func)
btn.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

bottom_frame = Frame(root)
bottom_frame.pack(fill='both', expand=True)

scrollbar = Scrollbar(bottom_frame)
scrollbar.pack(side=RIGHT, fill=Y)

output_list = Listbox(bottom_frame, width=30, height=10, yscrollcommand=scrollbar.set)
output_list.pack(side=LEFT, padx=5, pady=5)

scrollbar.config(command=output_list.yview())


root.mainloop()