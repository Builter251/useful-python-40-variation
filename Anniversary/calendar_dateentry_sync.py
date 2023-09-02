from tkinter import *
from tkcalendar import Calendar, DateEntry

def updateDate(event):
    selectedDate = cal.get_date()
    dateLabel.config(text=f"Selected Date is {selectedDate.strftime('%Y-%m-%d')}")
    date_entry.set_date(selectedDate)

def updateDateEntry(event):
    selectedDate = date_entry.get_date()
    dateLabel.config(text=f"Selected Date is {selectedDate.strftime('%Y-%m-%d')}")
    cal.selection_set(selectedDate)

window = Tk()
window.title("Date Synchronization")
window.geometry("350x450")

cal = Calendar(window, selectmode="day")
cal.pack(padx=10, pady=10)
cal.bind("<<CalendarSelected>>", updateDate)

date_entry = DateEntry(window)
date_entry.pack(padx=10, pady=5)
date_entry.bind("<<DateEntrySelected>>", updateDateEntry)

dateLabel = Label(window, text="Selected Date is ")
dateLabel.pack()

window.mainloop()