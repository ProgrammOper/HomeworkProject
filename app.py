from tkinter import *
from main import *
root = Tk()

def btn_click():
    value = float(inp.get())
    result.config(text=str(function(value).pop()))
root['bg']='#ffdead'
root.title('Название программы')
#root.wm_attributes('-alpha',0.7)
root.geometry('300x250')
root.resizable(width=False, height=False)
canvas = Canvas(root, height=300,width=250)
canvas.pack()
frame = Frame(root,background='#ffdead')
frame.place(relheight=1,relwidth=1)

title1 = Label(frame,text='Введите значение',font=40)
title1.pack()
inp=Entry(frame,bg='white')
inp.pack()
btn = Button(frame,text='Запустить', bg='blue', command=btn_click)
btn.pack()
title2 = Label(frame,text='Oтвет:',font=40)
title2.pack()
result = Label(frame,text='',font=40)
result.pack()
root.mainloop()