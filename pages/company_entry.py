import csv
import tkinter as tk
from tkinter import messagebox
from ttkbootstrap import Style
from ttkbootstrap.widgets import Entry

def add_entry_to_csv(file_name, company_name, email):
    with open(file_name, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([company_name, email])

def submit_entry():
    company_name = company_name_entry.get()
    email = email_entry.get()
    if company_name and email:
        add_entry_to_csv('companies.csv', company_name, email)
        messagebox.showinfo("Success", "Entry added successfully!")
        company_name_entry.delete(0, tk.END)
        email_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Input Error", "Please fill in both fields")

# Create the CSV file with headers if it doesn't exist
try:
    with open('companies.csv', 'x', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Company name", "Email address"])
except FileExistsError:
    pass

# Create the main window
root = tk.Tk()
root.title("Company Information Entry")
root.geometry('400x350')
root.resizable(width=False, height=False)

# colors
grey = 'grey'
black = 'black'
white = 'white'
light_purple = '#008db4'
deep_purple = '#0044ab'

main_frame = tk.Frame(root, bg=grey, pady=40)
main_frame.pack(fill=tk.BOTH, expand=True)
main_frame.columnconfigure(0, weight=1)
main_frame.rowconfigure(0, weight=1)
main_frame.rowconfigure(1, weight=1)

# Create and place the labels and entries inside the main_frame
tk.Label(main_frame,
         background=grey,
         font=('Arial', 12, 'bold'),
         text="Company Name:",).grid(row=0, column=0, padx=10, pady=5)
company_name_entry = Entry(main_frame,
                           bootstyle="info",
                           width=30,
                           font=('Arial', 14, 'normal'))
company_name_entry.grid(row=1, column=0, padx=10, pady=5)

tk.Label(main_frame,
         background=grey,
         font=('Arial', 12, 'bold'),
         text="Email Address:").grid(row=2, column=0, padx=10, pady=5)
email_entry = Entry(main_frame,
                    bootstyle="info",
                    width=30,
                    font=('Arial', 14, 'normal'))
email_entry.grid(row=3, column=0, padx=10, pady=5)

# Create and place the submit button inside the main_frame
submit_button = tk.Button(
    main_frame,
    background=light_purple,
    foreground=white,
    activebackground=deep_purple,
    activeforeground=white,
    highlightthickness=2,
    highlightbackground=black,
    highlightcolor=black,
    width=13,
    height=2,
    border=0,
    cursor='hand2',
    text="Submit",
    font=('Arial', 16, 'bold'),
    command=submit_entry)
submit_button.grid(row=4, column=0, pady=10)

# Run the application
root.mainloop()
