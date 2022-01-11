from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import ImageTk
from controllers.AuthController import AuthController


class AuthView:

    def load(self):
        self.window = Tk()
        self.window.title("Face Mask Detection")
        self.window.geometry("1199x600+100+50")
        bg=ImageTk.PhotoImage(file="login.jpg")
        label1=Label(self.window,image=bg)
        label1.place(x=0,y=0,relwidth=1,relheight=1)

        tab_control = ttk.Notebook(self.window)

        login_frame = Frame(tab_control,  padx=120, pady=120)
        register_frame = Frame(tab_control,  padx=120, pady=120)
        login_frame.place(x=100,y=100,height=380,width=600)
        register_frame.place(x=150,y=150,height=380,width=600)
      
        tab_control.add(login_frame, text='Login')
        tab_control.add(register_frame, text='Register')

        self.login(login_frame)
        self.register(register_frame)

        tab_control.grid()

        self.window.mainloop() 

    def login(self, login_frame):
        
        heading = Label(login_frame, text = "Login Form", bg = "black", fg="white", font=('Arial',20))
        heading.place(x=70, y=-50)
       
        #create user_name lable and entry
        username_lable = Label(login_frame,text='username',font=('Arial', 15))
        username_lable.grid(row=0, column=0,padx=5, pady=5,ipady=5)

        username_entry = Entry(login_frame, width=20)
        username_entry.grid(row=0, column=1,padx=5, pady=5,ipady=5)

        #create password lable and extry
        password_lable = Label(login_frame, text='password',font=('Arial', 15))
        password_lable.grid(row=1, column=0,padx=5, pady=5,ipady=5)

        password_entry = Entry(login_frame, show='*', width=20)
        password_entry.grid(row=1, column=1,padx=5, pady=5,ipady=5)


        #create button for login
        login_button = Button(login_frame, text='Login',font=('Arial', 15),  command= lambda: self.login_control(username_entry.get(), password_entry.get()), padx=5, pady=5)
        login_button.grid(row=2, column=1, pady=15)

    def register(self, register_frame):

        window = register_frame
        heading = Label(register_frame, text = "Registration Form", bg = "black", fg="white", font=('Arial',20))
        heading.place(x=70, y=-50)

        name_lable = Label(window,text='name      ',font=('Arial', 15))
        name_lable.grid(row=0, column=0,padx=5, pady=5,ipady=5)

        name_entry = Entry(window, width=20)
        name_entry.grid(row=0, column=1,padx=5, pady=5,ipady=5)

        username_lable = Label(window,text='username',font=('Arial', 15))
        username_lable.grid(row=1, column=0,padx=5, pady=5,ipady=5)

        username_entry = Entry(window, width=20)
        username_entry.grid(row=1, column=1,padx=5, pady=5,ipady=5)

        password_lable = Label(window, text='password',font=('Arial', 15))
        password_lable.grid(row=2, column=0,padx=5, pady=5,ipady=5)

        password_entry = Entry(window, show='*', width=20)
        password_entry.grid(row=2, column=1,padx=5, pady=5,ipady=5)

        email_lable = Label(window,text='email      ',font=('Arial', 15))
        email_lable.grid(row=3, column=0,padx=5, pady=5,ipady=5)

        email_entry = Entry(window, width=20)
        email_entry.grid(row=3, column=1,padx=5, pady=5,ipady=5)

        phone_lable = Label(window,text='phone     ',font=('Arial', 15))
        phone_lable.grid(row=4, column=0,padx=5, pady=5,ipady=5)

        phone_entry = Entry(window, width=20)
        phone_entry.grid(row=4, column=1,padx=5, pady=5,ipady=5)

        login_button = Button(window, text='Register',  command= lambda: self.register_control(name_entry.get(), phone_entry.get(), email_entry.get(), username_entry.get(), password_entry.get()), padx=5, pady=5)
        login_button.grid(row=5, column=1, pady=5,padx=5,ipady=5)

    def login_control(self, username, password):
        ac = AuthController()
        message = ac.login(username, password)

        if(message == 1):
            self.window.destroy()
            self.transfer_control()
        else:
            messagebox.showinfo('Information', message)


    def register_control(self, name, phone, email, username, password):
        ac = AuthController()
        message = ac.register(name, phone, email, username, password)
        messagebox.showinfo('Information', message)



if __name__ == '__main__':
    av = AuthView()




