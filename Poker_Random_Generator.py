import random

from tkinter import*

root = Tk()
root.geometry("250x100")
root.configure(bg="black")
root.title("Poker_Random_Generator")
root.grid()


def std_poker():
    value =random.randint(1,100)
    print(value)
    if (value<=35):
        number.config(text=value,foreground="red")
    elif (value >=75):
        number.config(text=value,foreground="black")
    else:
        number.config(text=value,foreground="blue")


button_1= Button( text="Generate[1-100]",bg="white",command=std_poker)
button_1.pack()
button_1.place(height=35,width=155,x=50,y=10)


number=Label(text="",foreground="blue")
number.pack()
number.place(height=20,width=60,x=100,y=70)

root.mainloop()
