from tkinter import  *

win = Tk()
win.title('XO')
win.geometry('500x505')
win.resizable(0,0)
win.config(bg="lightgray")
win.option_add("*Button*font","times 16 bold")
_t = "0"

def add_button(bt,r,c):
    bt.config(width=3,command=lambda:button_click(bt))
    bt.grid(row=r,column=c,padx=10,pady=10)

for r in range(0,3):
    for c in range(0,3):
        add_button(Button(),r,c)
mainloop()
