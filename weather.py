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

root.mainloop()