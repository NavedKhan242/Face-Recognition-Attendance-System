from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2




class developer:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")
        
        
        title_lbl=Label(self.root,text="DEVELOPER",font=("times new roman",35,"bold"),bg="white",fg="BLUE")
        title_lbl.place(x=0,y=0,width=1530,height=45) 
        
        img_top=Image.open(r"c:\Users\dell\Desktop\Face Recognition system\college_images\dev.jpg")
        img_top=img_top.resize((1530,720),Image.Resampling.LANCZOS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)
        
        
        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=55,width=1530,height=720)
        
        
        #Frame
        
        main_frame=Frame(f_lbl,bd=2,bg="white")
        main_frame.place(x=1000,y=0,width=500,height=600)    
        
        
        img=Image.open(r"c:\Users\dell\Desktop\Face Recognition system\college_images\LoginIconAppl.png")
        img=img.resize((200,200),Image.Resampling.LANCZOS)
        self.photoimg_as=ImageTk.PhotoImage(img)
        
        
        f_lbl=Label(main_frame,image=self.photoimg_as)
        f_lbl.place(x=300,y=0,width=200,height=200)
        
        #######Developer info
        
        developerr_label=Label(main_frame,text="Hello My Name is Naved Khan",font=("times new roman",17,"bold"),bg="white",fg="blue")
        developerr_label.place(x=0,y=5)
        
        developerr_label=Label(main_frame,text="",font=("times new roman",17,"bold"),bg="white",fg="blue")
        developerr_label.place(x=0,y=40)
        
        img2=Image.open(r"c:\Users\dell\Desktop\Face Recognition system\A\pngtree-cyberpunk-emotion-detection-interface-with-face-analyzer-picture-image_16700708.jpg")
        img2=img2.resize((500,400),Image.Resampling.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        
        
        f_lbl=Label(main_frame,image=self.photoimg2)
        f_lbl.place(x=0,y=210,width=500,height=400)
    
        
if __name__ == "__main__":
    root=Tk()
    obj=developer(root)
    root.mainloop() 