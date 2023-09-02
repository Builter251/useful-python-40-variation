from datetime import timedelta
import tkinter as tk
from tkcalendar import DateEntry
import sys

window = tk.Tk()
window.title("Plus D-day")

def plus(event):
    selected_basis_date = basis_date.get_date()
    plus_days = spin_days.get()
    result_date = selected_basis_date + timedelta(days=int(plus_days))
    label_result.config(text=f"{selected_basis_date}로 부터 {plus_days}일 후의 날짜는 {result_date} 입니다")

label_basis = tk.Label(window, text="기준일")
basis_date = DateEntry(window, foreground="black", showweeknumbers = False)
label_spin = tk.Label(window, text="기준일로부터 + ")
spin_days = tk.Spinbox(window, from_=1, to=sys.maxsize)
label_result = tk.Label(window, text=f"{basis_date.get_date()}로 부터 {spin_days.get()}일 후의 날짜는 ")

basis_date.bind("<<DateEntrySelected>>", plus)
spin_days.bind("<Button-1>", plus)

label_basis.pack()
basis_date.pack()
label_spin.pack()
spin_days.pack()
label_result.pack()

window.mainloop()