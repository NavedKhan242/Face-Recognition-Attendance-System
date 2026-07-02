from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
from time import strftime
from datetime import datetime
import numpy as np
 



class Face_Recognition:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")
        
        title_lbl=Label(self.root,text="Face  Recognition  ",font=("times new roman",35,"bold"),bg="white",fg="green")
        title_lbl.place(x=0,y=0,width=1530,height=45) 
        
        
        img_top=Image.open(r"c:\Users\dell\Desktop\Face Recognition system\college_images\A/WhatsApp Image 2025-10-23 at 3.07.37 AM (1).jpeg")
        img_top=img_top.resize((650,700),Image.Resampling.LANCZOS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)
        
        
        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=55,width=650,height=700)
        
        
        
        
         
        img_side=Image.open(r"c:\Users\dell\Desktop\Face Recognition system\college_images\facial_recognition_system_identification_digital_id_security_scanning_thinkstock_858236252_3x3-100740902-large.jpg")
        img_side=img_side.resize((950,700),Image.Resampling.LANCZOS)
        self.photoimg_side=ImageTk.PhotoImage(img_side)
        
        
        f_lbl=Label(self.root,image=self.photoimg_side)
        f_lbl.place(x=650,y=55,width=950,height=700)
        
        
        b1_1=Button(f_lbl,text="Face Recognition",cursor="hand2",command=self.face_rec,font=("times new roman",18,"bold"),fg="white",bg="dark green")
        b1_1.place(x=370,y=620,width=200,height=40)
        
        #aTTEBDANCE
    def mark_attendance(self,i,d,rol,i_d):
        with open(r"c:\Users\dell\Desktop\Face Recognition system\Naved.csv","r+",newline="\n") as f:   
            myDataList=f.readlines()
            name_list=[]
            for line in myDataList:
                entry=line.split(',')
                name_list.append(entry[0])
            if((i not in name_list) and (rol not in name_list) and (i_d not in name_list) and (d not in name_list)):
                now=datetime.now()
                d1=now.strftime("%d/%m/%Y")
                dtString=now.strftime("%H:%M:%S")
                f.writelines(f"\n{i},{rol},{d},{i_d},{dtString},{d1},Present")
                
        
         
        ##########Face recognition
        
    def face_rec(self):
        def draw_boundary(img,classifier,scaleFactor,minNeighbors,color,text,clf):
            gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            feature=classifier.detectMultiScale(gray_image,scaleFactor,minNeighbors)
            coord=[]
            
            for (x,y,w,h) in feature:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                id,predict=clf.predict(gray_image[y:y+h,x:x+w])
                confidence=int((100*(1-predict/300)))
                
                
                conn=mysql.connector.connect(host="localhost",username="root",password="navedkhan8888",database="face_recognition")
                my_cursor=conn.cursor()
                
                
                
                my_cursor.execute("select name from student where id="+str(id))
                i=my_cursor.fetchone()
                i=str(i)
                
                
                my_cursor.execute("select roll from student where id="+str(id))
                rol=my_cursor.fetchone()
                rol=str(rol)
                
                my_cursor.execute("select dep from student where id="+str(id))
                d=my_cursor.fetchone()
                d=str(d)
                
                
                my_cursor.execute("select id from student where id="+str(id))
                i_d=my_cursor.fetchone()
                i_d=str(i_d)
                            
                
                if confidence>60:
                    cv2.putText(img,f"id:{i_d}",(x,y-75),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Roll:{rol}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Name:{i}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Dep:{d}",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    self.mark_attendance(i,rol,d,i_d)
                    
                else:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                    cv2.putText(img,"Unknown face",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                coord=[x,y,w,h]
            return coord
        def recognizer(img,clf,faceCascade):
            coord=draw_boundary(img,faceCascade,1.1,10,(255,25,255),"Face",clf)
            return img
        faceCascade = cv2.CascadeClassifier(r"c:\Users\dell\Desktop\Face Recognition system\haarcascade_frontalface_default.xml")
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.read(r"c:\Users\dell\Desktop\Face Recognition system\classifier.xml")
        
        video_cap=cv2.VideoCapture(0)
        
        while True:
            ret,img=video_cap.read()
            img=recognizer(img,clf,faceCascade)
            cv2.imshow("Welcome to face recognition",img)
            
            
            
            if cv2.waitKey(1)==13:
                break
        video_cap.release()
        cv2.destroyAllWindows()
        
        
if __name__ == "__main__":
    root=Tk()
    obj=Face_Recognition(root)
    root.mainloop() 