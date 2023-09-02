import tkinter as tk
from tkcalendar import DateEntry

def update_date():
    selected_date = cal.get_date()
    date_label.config(text=f"Selected Date: {selected_date}")

def on_date_select(event):
    update_date()

root = tk.Tk()
root.title("Date Selection")

cal = DateEntry(root, year=2023, month=8, day=7)
cal.pack(padx=10, pady=10)

update_button = tk.Button(root, text="Update Date", command=update_date)
update_button.pack(pady=5)

date_label = tk.Label(root, text="")
date_label.pack()

cal.bind("<<DateEntrySelected>>", on_date_select)

root.mainloop()
