from tkinter import *
import tkinter.messagebox as msg
from tools.tools_and_validators import *

def save_button():
    try:
        username_validator(username.get())
        password_validator(password.get())
        nickname_validator(nickname.get())
        save_user(username.get(), password.get(), nickname.get(), lock_state.get())
        msg.showinfo("Save","Login Successful")
    except Exception as e:
        msg.showerror("Error", f"{e}")

window = Tk()
window.title("Login")
window.geometry("280x300")
#username
username = StringVar()
Label(window, text="username :" ,fg= "blue",font="20").place(x=20, y=20)
Entry(window, textvariable=username).place(x=140, y=27)
#password
password = StringVar()
Label(window, text="password :", fg= "blue",font="20").place(x=20, y=60)
Entry(window, show= "*", textvariable=password).place(x=140, y=67)
#nickname
nickname = StringVar()
Label(window, text="nickname :", fg= "blue",font="20").place(x=20, y=100)
Entry(window, textvariable=nickname).place(x=140, y=107)
#lock state
lock_state= BooleanVar()
Checkbutton(window, text="Lock", fg= "red",variable= lock_state ,font="20").place(x=20, y=137)
# save button
Button(window, text="Save",bg="light blue", font="20", command=save_button).place(x=20, y=177)
window.mainloop()