import tkinter as tk

screen = tk.Tk()
screen.geometry('500x500')
screen.title('Python form')
heading = tk.Label(text='Python form', bg='grey', fg='black', height='3', width='500')
heading.pack()

firstname_text = tk.Label(text='Firstname *')
lastname_text = tk.Label(text='Lastname *')
age_text = tk.Label(text='age')
firstname_text.place(x=15, y=70)
lastname_text.place(x=10, y=140)
age_text.place(x=15, y=210)

firstname = tk.StringVar()
lastname = tk.StringVar()
age = tk.IntVar()

firstname_entry = tk.Entry(textvariable=firstname, width='30')
lastname_entry = tk.Entry(textvariable=lastname, width='30')
age_entry = tk.Entry(textvariable=age, width='30')
 
firstname_entry.place(x=15, y=100)
lastname_entry.place(x=15, y=180)
age_entry.place(x=15, y=240)

def save_info():
    firstname_info = firstname.get()
    lastname_info = lastname.get()
    age_info = age.get()

    print(firstname_info, lastname_info, age_info)

register = tk.Button(screen, text='register', width='25', height='2', command=save_info, bg='grey')
register.place(x=15, y=280)

screen.mainloop()







