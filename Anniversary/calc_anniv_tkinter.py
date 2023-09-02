import tkinter as tk
from tkcalendar import Calendar
from datetime import datetime

today = datetime.now().date()

window = tk.Tk()
window.title("일생 계산기")

label_guide = tk.Label(window, text="당신의 생일을 선택해주세요")
cal = Calendar(window, selectmode="day", foreground="black", showweeknumbers = False)
label_today = tk.Label(window, text=f"오늘은 {today} 입니다.")
label_selected = tk.Label(window, text=f"당신의 생일은 ")
label_diff = tk.Label(window, text="당신이 태어난지 ")

def update_date(event):
    date_selected = cal.selection_get()
    
    if date_selected < today:
        date_diff = today - date_selected
        label_selected.config(text=f"당신의 생일은 {date_selected} 입니다")
        label_diff.config(text=f"당신이 태어난 지 {date_diff.days}일이 지났습니다.")
    if date_selected >= today:
        label_selected.config(text=f"당신의 생일은 아직 오지 않았습니다")
        label_diff.config(text=f"앞으로의 날들도 응원합니다!")

cal.bind("<<CalendarSelected>>", update_date)

label_guide.pack()
cal.pack()
label_today.pack()
label_selected.pack()
label_diff.pack()

window.mainloop()