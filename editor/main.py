import tkinter as tk

screen = tk.Tk()
screen.geometry('500x500')
screen.title('Python form')
heading = tk.Label(text='Python form', bg='grey', fg='black', height='3', width='500')
heading.pack()

text = tk.StringVar()
text_thing = tk.Entry(textvariable=text, width='500')

def save_info():
    print(text)


register = tk.Button(screen, text='register', width='25', height='2', command=save_info, bg='grey')
register.place(x=15, y=280)

screen.mainloop()







