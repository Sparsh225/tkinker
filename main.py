from tkinter import *

window=Tk()
window.title("MILE TO KM")
window.minsize(width="200",height="100")

def button_clicked():
    text=float(entry.get())
    b=round(text*1.687)
    label3.config(text=f"{b}")
entry=Entry(width=10)
entry.grid(row=0,column=1)

label1=Label(text="Miles")
label1.grid(row=0,column=2)

label2=Label(text="is equal to")
label2.grid(row=1,column=0)

label3=Label(text="0")
label3.grid(row=1,column=1)

label4=Label(text="Km")
label4.grid(row=1,column=2)

button=Button(text="Calculate" ,command=button_clicked)
button.grid(row=2,column=1)

window.mainloop()