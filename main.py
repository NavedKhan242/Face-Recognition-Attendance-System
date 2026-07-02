from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from student import Student
import os
from train import Train
from face_recognition import Face_Recognition
from attendance import Attendance
from Developer import developer
from help import Help
import tkinter
from time import strftime
from datetime import datetime

class Face_Recognition_System:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")
        
          ###First Image
        
        img=Image.open(r"c:\Users\dell\Desktop\Face Recognition system\college_images\A\WhatsApp Image 2025-10-23 at 3.07.37 AM (3).jpeg")
        img=img.resize((500,130),Image.Resampling.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)
        
        
        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=500,height=130)
        
        
        ###Second Image
        
        img1=Image.open(r"c:\Users\dell\Desktop\Face Recognition system\college_images\A\gettyimages-1490940349-1024x1024.jpg")
        img1=img1.resize((500,130),Image.Resampling.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        
        
        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=500,y=0,width=500,height=130)
        
        
        ###Thired Image
        
        img2=Image.open(r"c:\Users\dell\Desktop\Face Recognition system\college_images\A\WhatsApp Image 2025-10-23 at 3.07.38 AM.jpeg")
        img2=img2.resize((500,130),Image.Resampling.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        
        
        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=1000,y=0,width=550,height=130)
        
        
        
        
        #BG IMAGE 
        
        
        img3=Image.open(r"c:\Users\dell\Desktop\Face Recognition system\A\dark-blue-digital-technology-with-line-big-data-background-abstract-cyber-lines-shiny-circuit-concept-vector.jpg")
        img3=img3.resize((1530,710),Image.Resampling.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)
        
        
        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=130,width=1530,height=710)
        
        
        title_lbl=Label(bg_img,text="FACE RECOGNITION ATTENDANCE SYSTEM SOFTWARE",font=("times new roman",35,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1530,height=45)
        
        ########3Time 
        def time():
            string=strftime('%H:%M:%S %p')
            lbl.config(text=string)
            lbl.after(1000,time)
        
        
        lbl=Label(title_lbl,font=("times new roman",14,'bold'),background='White',foreground='blue')
        lbl.place(x=0,y=0,width=110,height=50)
        time()
          ########### student button
        
        img4=Image.open(r"c:\Users\dell\Desktop\Face Recognition system\A\istockphoto-1166057711-612x612.jpg")
        img4=img4.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimg4=ImageTk.PhotoImage(img4)
        
        b1=Button(bg_img,image=self.photoimg4,command=self.SStudent_details,cursor="hand2")
        b1.place(x=200,y=100,width=220,height=220)
        
        
        
        
        b1_1=Button(bg_img,text="student Detail ",cursor="hand2",command=self.SStudent_details,font=("times new roman",15,"bold"),fg="white",bg="darkblue")
        b1_1.place(x=200,y=300,width=220,height=40)

        
        
        ########### Detect face 
        
        
        
        img5=Image.open(r"c:\Users\dell\Desktop\Face Recognition system\college_images\face_detector1.jpg")
        img5=img5.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimg5=ImageTk.PhotoImage(img5)
        
        b1=Button(bg_img,image=self.photoimg5,cursor="hand2",command=self.Face_data)
        b1.place(x=500,y=100,width=220,height=220)
        
        
        
        
        b1_1=Button(bg_img,text="Face Detection  ",cursor="hand2",command=self.Face_data,font=("times new roman",15,"bold"),fg="white",bg="darkblue")
        b1_1.place(x=500,y=300,width=220,height=40)
        
        
        ##############Attendance face buttton 
        img6=Image.open(r"c:\Users\dell\Desktop\Face Recognition system\college_images\smart-attendance.jpg")
        img6=img6.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimg6=ImageTk.PhotoImage(img6)
        
        b1=Button(bg_img,image=self.photoimg6,command=self.attendance,cursor="hand2")
        b1.place(x=800,y=100,width=220,height=220)
        
           
        b1_1=Button(bg_img,text=" Attendance ",cursor="hand2",command=self.attendance,font=("times new roman",15,"bold"),fg="white",bg="darkblue")
        b1_1.place(x=800,y=300,width=220,height=40)
        
        
        ########help face 
        
        
        
        
        img7=Image.open(r"c:\Users\dell\Desktop\Face Recognition system\college_images\help desk.jpg")
        img7=img7.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimg7=ImageTk.PhotoImage(img7)
        
        b1=Button(bg_img,image=self.photoimg7,command=self.help_desk,cursor="hand2")
        b1.place(x=1100,y=100,width=220,height=220)
        
        
        
        
        b1_1=Button(bg_img,text="  Help Desk  ",cursor="hand2",font=("times new roman",15,"bold"),command=self.help_desk,fg="white",bg="darkblue")
        b1_1.place(x=1100,y=300,width=220,height=40)
        
        
        
        
        ##### train data 
        
        
        
        img8=Image.open(r"c:\Users\dell\Desktop\Face Recognition system\college_images\Train.jpg")
        img8=img8.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimg8=ImageTk.PhotoImage(img8)
        
        b1=Button(bg_img,image=self.photoimg8,command=self.train_data,cursor="hand2")
        b1.place(x=200,y=380,width=220,height=220)
        
        
        
        
        b1_1=Button(bg_img,text="Train Data  ",cursor="hand2",command=self.train_data,font=("times new roman",15,"bold"),fg="white",bg="darkblue")
        b1_1.place(x=200,y=580,width=220,height=40)
        
        
        ########### photo face button 
        
        
        
        
        img9=Image.open(r"c:\Users\dell\Desktop\Face Recognition system\A\1000_F_1647230350_wzFpZnJLOs1g5qO58dgEGk7fiw38Tm8V.jpg")
        img9=img9.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimg9=ImageTk.PhotoImage(img9)
        
        b1=Button(bg_img,image=self.photoimg9,cursor="hand2",command=self.open_images)
        b1.place(x=500,y=380,width=220,height=220)
        
        
        
        
        b1_1=Button(bg_img,text="Photos ",cursor="hand2",command=self.open_images,font=("times new roman",15,"bold"),fg="white",bg="darkblue")
        b1_1.place(x=500,y=580,width=220,height=40)
        
        
        
        ##########Developers
        
        
        
        img10=Image.open(r"c:\Users\dell\Desktop\Face Recognition system\college_images\dev.jpg")
        img10=img10.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimg10=ImageTk.PhotoImage(img10)
        
        b1=Button(bg_img,image=self.photoimg10,command=self.devloper_data,cursor="hand2")
        b1.place(x=800,y=380,width=220,height=220)
        
        
        
        
        b1_1=Button(bg_img,text="Developer",cursor="hand2",command=self.devloper_data,font=("times new roman",15,"bold"),fg="white",bg="darkblue")
        b1_1.place(x=800,y=580,width=220,height=40)
        
        
        
        #######Exit
        
        
        
        img11=Image.open(r"c:\Users\dell\Desktop\Face Recognition system\college_images\exit.jpg")
        img11=img11.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimg11=ImageTk.PhotoImage(img11)
        
        b1=Button(bg_img,image=self.photoimg11,cursor="hand2",command=self.exit_data)
        b1.place(x=1100,y=380,width=220,height=220)
        
        
        
        
        b1_1=Button(bg_img,text="Exit ",cursor="hand2",font=("times new roman",15,"bold"),fg="white",bg="darkblue",command=self.exit_data)
        b1_1.place(x=1100,y=580,width=220,height=40) 

    def open_images(self):
      os.startfile(r"c:\Users\dell\Desktop\Face Recognition system\data")   
      
      
    def exit_data(self):
        self.exit_data=tkinter.messagebox.askyesno("Face Recognition","Are you sure to exit ",parent=self.root)
        if self.exit_data>0:
            self.root.destroy()
        else:
            return
       
       ##############Function Button
       
    def SStudent_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)
        
        
        
    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)
        
        
    def Face_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_Recognition(self.new_window)
            
        
    def attendance(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendance(self.new_window)
        
    def devloper_data(self):
        self.new_window=Toplevel(self.root)
        self.app=developer(self.new_window)
            
            
    def help_desk(self):
        self.new_window=Toplevel(self.root)
        self.app=Help(self.new_window)
            
                   
if __name__ == "__main__":
    root=Tk()
    obj=Face_Recognition_System(root)
    root.mainloop()