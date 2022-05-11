from tkinter import *
import math

window = Tk()
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = NONE
# ---------------------------- TIMER RESET ------------------------------- #

def timer_reset():
    window.after_cancel(timer)
    Timer.config(text="Timer")
    canvas.itemconfig(timer_text, text="00:00")
    Check.config(text="")
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global reps
    reps += 1
    works_secs = WORK_MIN * 60
    short_break_secs = SHORT_BREAK_MIN * 60
    long_break_secs = LONG_BREAK_MIN * 60

    if reps % 8 == 0 :
        count_down(long_break_secs)
        Timer.config(text="Break",font=(FONT_NAME, 36),fg=RED)
    elif reps % 2 == 0:
        count_down(short_break_secs)
        Timer.config(text="Break", font=(FONT_NAME, 36), fg=PINK)
    else:
        count_down(works_secs)
        Timer.config(text="Work", font=(FONT_NAME, 36), fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def count_down(count):
    count_minutes = math.floor(count / 60)
    count_seconds = count % 60
    if count_seconds < 10:
        count_seconds = f"0{count_seconds}"
    canvas.itemconfig(timer_text,text=f"{count_minutes}:{count_seconds}")
    if count > 0:
        global timer
        timer = window.after(1000,count_down,count-1)
    else:
        start_timer()
        marks = ""
        works_sessions = math.floor(reps/2)
        for n in range(works_sessions):
            marks += checkmark
        Check.config(text=marks)




# ---------------------------- UI SETUP ------------------------------- #

window.title("Pomodoro")
window.config(padx=100, pady=50,bg=YELLOW)
checkmark = "✓"


my_img = PhotoImage(file="tomato.png")
canvas = Canvas(width=200,height=224,bg=YELLOW,highlightthickness=0)
canvas.create_image(100,112,image = my_img)
timer_text = canvas.create_text(100,130,text=f"00:00",font=(FONT_NAME,36),fill="white")
canvas.grid(row=1,column=1)
# canvas.create_text(100,1,text="TIMER",font=(FONT_NAME,36),fill=GREEN)
Timer = Label(text = "Timer",fg=GREEN,font=(FONT_NAME, 36),bg=YELLOW)
Timer.grid(row=0,column=1)
Check = Label(fg=GREEN,font=(FONT_NAME, 12),bg=YELLOW)
Check.grid(column=1,row=3)

start_btn = Button(text="Start",padx=10,pady=10,highlightthickness=0,command=start_timer)
start_btn.grid(row=2,column=0)

reset_btn = Button(text="Reset",padx=10,pady=10,highlightthickness=0,command=timer_reset)
reset_btn.grid(row=2,column=2)



canvas.mainloop()
window.mainloop()