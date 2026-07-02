from tkinter import*
from PIL import ImageTk,Image
from tkinter import messagebox
from main import Face_Recognition

class  Login:
    def __init__(self,root):
        self.root=root
        self.root.title("Login System")
        self.root.geometry("1400x700+100+50")
        self.root.resizable(False,False)
        # Bg Image 
        self.bg=PhotoImage(file=r"C:\Users\dell\Desktop\LOGIN TKINTER/pic2.png")
        self.bg_image=Label(self.root,image=self.bg).place(x=0,y=0,relwidth=1,relheight=1)
        
        ##Login Frame 
        Frame_login=Frame(self.root,bg="white")
        Frame_login.place(x=800,y=150,height=420,width=500)
        
        
        
        title=Label(Frame_login,text="Login Here",font=("Impact",35,"bold"),fg="#d77337",bg="white").place(x=90,y=30)
        desc=Label(Frame_login,text="Accounatant Employee Login Area",font=("Goudy old style",15,"bold"),fg="#d25d17",bg="white").place(x=90,y=100)
        
        
        lbl_user=Label(Frame_login,text="Username",font=("Goudy old style",15,"bold"),fg="gray",bg="white").place(x=90,y=140)
        self.txt_user=Entry(Frame_login,font=("times new roman",15),bg="lightgray")
        self.txt_user.place(x=90,y=170,width=350,height=35)
        
        
        lbl_pass=Label(Frame_login,text="Password",font=("Goudy old style",15,"bold"),fg="gray",bg="white").place(x=90,y=210)
        self.txt_pass=Entry(Frame_login,show="*",font=("times new roman",15),bg="lightgray")
        self.txt_pass.place(x=90,y=240,width=350,height=35)
        
        forgot=Button(Frame_login,text="Forgot Password",bg="white",fg="#d77337",bd=0,font=("times new roman",12)).place(x=90,y=280)
        
        Register=Button(Frame_login,text="New User Registeration ",bg="white",fg="#d77337",bd=0,font=("times new roman",12)).place(x=90,y=310)
        
        
        
        Login=Button(self.root,command=self.login_fun,text="Login",fg="white",bg="#d77337",font=("times new roman",20)).place(x=970,y=500,width=180,height=40)
                ##### edit your name 
          
        Coder_nAME=Label(Frame_login,text="Code By Naved Khan",fg="Black",bg="white",font=("consolas",12,"bold")).pack()
        
        
        
        
        
        
        ### Id and password
        
    def login_fun(self):
        if self.txt_pass.get()==""or self.txt_user.get()=="":
            messagebox.showerror("Error","All Feilds are required",parent=self.root)
        elif self.txt_pass.get()!="12345"or self.txt_user.get()!="Naved":
            messagebox.showerror("Error","Invalid username/Password",parent=self.root)
        else:
            messagebox.showinfo("Welcome",f"Welcome:{self.txt_user.get()}\nYour Password:{self.txt_pass.get()}",parent=self.root)
            
                      
        
root=Tk()
obj=Login(root)
root.mainloop()        
        
