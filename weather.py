from tkinter import *
import tkinter as tk
from geopy.geocoders import Nominatim
from tkinter import messagebox,ttk
from timezonefinder import TimezoneFinder
from datetime import datetime
import requests
import pytz

root=Tk()
root.title("Weather App")
root.geometry("900x500+300+200")
root.resizable(False,False)

#search box
search_image=PhotoImage(file="assets/search.png")
my_image=Label(image=search_image)
my_image.place(x=20,y=20)

textfield=tk.Entry(root,justify=CENTER,font=("poppins",25,"bold"),width=17,bg="#404040",fg="white",border=0)
textfield.place(x=50,y=40)
textfield.focus()

search_icon=PhotoImage(file="assets/search_icon.png")
my_image_icon=Button(image=search_icon,borderwidth=0,cursor="hand2",bg="#404040")
my_image_icon.place(x=400,y=34)

#logo
logo_image=PhotoImage(file="assets/logo.png")
logo_label=Label(image=logo_image,borderwidth=0)
logo_label.place(x=150,y=100)

#bottom box
frame_image=PhotoImage(file="assets/frame.png")
frame_my_image=Label(image=frame_image,borderwidth=0)
frame_my_image.pack(padx=5,pady=5,side=BOTTOM)

#label
label_1=Label(root,text="WIND",font=("Helvetica",15,"bold"),bg="#1ab5ef",fg="white")
label_1.place(x=120,y=400)

label_2=Label(root,text="HUMIDITY",font=("Helvetica",15,"bold"),bg="#1ab5ef",fg="white")
label_2.place(x=250,y=400)

label_3=Label(root,text="DESCRIPTION",font=("Helvetica",15,"bold"),bg="#1ab5ef",fg="white")
label_3.place(x=430,y=400)

label_4=Label(root,text="PRESSURE",font=("Helvetica",15,"bold"),bg="#1ab5ef",fg="white")
label_4.place(x=650,y=400)


root.mainloop()