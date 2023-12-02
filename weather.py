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

def getWether():
        try:
                city=textfield.get()
                
                geolocator=Nominatim(user_agent="nimmaZ-weather-app")
                location=geolocator.geocode(city)
                obj=TimezoneFinder()
                result=obj.timezone_at(lng=location.longitude,lat=location.latitude)

                home=pytz.timezone(result)
                local_time=datetime.now(home)
                current_time=local_time.strftime("%I:%M %p")
                clock.config(text=current_time)
                name.config(text="CURRENT WEATHER")

                #weather
                api="https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=f85b5bd8a72b35456680ed64a5dcbee1"

                json_data=requests.get(api).json()
                condition=json_data['weather'][0]['main']
                description=json_data['weather'][0]['description']
                temp=int(json_data['main']['temp']-273.15)
                pressure=json_data['main']['pressure']
                humidity=json_data['main']['humidity']
                wind=json_data['wind']['speed']

                t.config(text=(temp,"°C"))
                c.config(text=(condition,"|","FEELS","LIKE",temp,"°C"))

                w.config(text=str(wind)+" km/h")
                p.config(text=str(pressure)+" hPa")
                h.config(text=str(humidity)+" %")
                d.config(text=description)

        except Exception as e:
                messagebox.showerror("Error","Please enter a valid city name")


#search box
search_image=PhotoImage(file="assets/search.png")
my_image=Label(image=search_image)
my_image.place(x=20,y=20)

textfield=tk.Entry(root,justify=CENTER,font=("poppins",25,"bold"),width=17,bg="#404040",fg="white",border=0)
textfield.place(x=50,y=40)
textfield.focus()

search_icon=PhotoImage(file="assets/search_icon.png")
my_image_icon=Button(image=search_icon,borderwidth=0,cursor="hand2",bg="#404040",command=getWether)
my_image_icon.place(x=400,y=34)

#logo
logo_image=PhotoImage(file="assets/logo.png")
logo_label=Label(image=logo_image,)
logo_label.place(x=150,y=100)

#bottom box
frame_image=PhotoImage(file="assets/frame.png")
frame_my_image=Label(image=frame_image,)
frame_my_image.pack(padx=5,pady=5,side=BOTTOM)

#time
name=Label(root,font=("arial",15,"bold"))
name.place(x=30,y=100)
clock=Label(root,font=("Helvetica",20))
clock.place(x=30,y=130)

#label
label_1=Label(root,text="WIND",font=("Helvetica",15,"bold"),bg="#1ab5ef",fg="white")
label_1.place(x=110,y=400)

label_2=Label(root,text="HUMIDITY",font=("Helvetica",15,"bold"),bg="#1ab5ef",fg="white")
label_2.place(x=270,y=400)

label_3=Label(root,text="DESCRIPTION",font=("Helvetica",15,"bold"),bg="#1ab5ef",fg="white")
label_3.place(x=410,y=400)

label_4=Label(root,text="PRESSURE",font=("Helvetica",15,"bold"),bg="#1ab5ef",fg="white")
label_4.place(x=660,y=400)

t=Label(font=("arial",70,"bold"),fg="#fc5c65")
t.place(x=400,y=150)
c=Label(font=("arial",15,"bold"))
c.place(x=400,y=250)

w=Label(text="...",font=("arial",16,"bold"),bg="#1ab5ef")
w.place(x=110,y=430)
h=Label(text="...",font=("arial",16,"bold"),bg="#1ab5ef")
h.place(x=270,y=430)
d=Label(text="...",font=("arial",16,"bold"),bg="#1ab5ef")
d.place(x=410,y=430)
p=Label(text="...",font=("arial",16,"bold"),bg="#1ab5ef")
p.place(x=660,y=430)

root.mainloop()