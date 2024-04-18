from tkinter import *
import tkinter as tk   # Import both for compatibility
from altair import Latitude    # Not used in this code
from geopy.geocoders import Nominatim     # For geocoding city names
from tkinter import ttk,messagebox        # For widgets and error messages
from timezonefinder import TimezoneFinder   # To find timezones based on location
from datetime   import datetime   # For handling date and time
import requests    # For making API requests
import pytz    # For working with timezones


# Create the main window
root=Tk()
root.title("Weather App OI")
root.geometry("900x500+300+200")
root.resizable(False,False)     #Disable window resizing



# Function to get weather data based on city name
def getWeather():
    try:
       city= textfield.get()   # Get city name from the text field
    
       geoloctor = Nominatim(user_agent="geoapoExcercises")  # Use Nominatim to geocode the city and get location details
       location= geoloctor.geocode(city)
       
       obj = TimezoneFinder()     # Find the timezone based on location coordinates
       result  = obj.timezone_at(lng=location.longitude,lat=location.latitude)
       home=pytz.timezone(result)
       
       local_time=datetime.now(home)   # Get the current local time in the city's timezone
       current_time=local_time.strftime("%I:%M %p")  # Format time (12-hour format with AM/PM)
       
       clock.config(text=current_time)  # Update the clock label with the current local time
       name.config(text="CURRENT WEATHER")  # Update label to "CURRENT WEATHER"
    
    
       #weather
       # Construct the weather API URL using the city name and API key
       api="https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=44ce42b15cddcb145961d2a9270bd57b"
    
       # Make a GET request to the weather API
       # Extract weather data from the JSON response
       json_data = requests.get(api).json()
       condition = json_data['weather'][0]['main']
       description = json_data['weather'][0]['description']
       temp = int(json_data['main']['temp']-273.15)  # Convert Kelvin to Celsius
       pressure = json_data['main']['pressure']
       humidity = json_data['main']['humidity']
       wind = json_data['wind']['speed']
    
       # Update weather labels with the retrieved data
       t.config(text=(temp,"°"))
       c.config(text=(condition, "|","FEELS","LIKE",temp,"°"))
    
       w.config(text=wind)
       h.config(text=humidity)
       d.config(text=description)
       p.config(text=pressure)
       
    except Exception as e: # Handle errors (e.g., invalid city name)
       messagebox.showerror("weather app OI","Invalid Entry!!")



#search box elements
Search_image=PhotoImage(file="search.png")
myimage=Label(image=Search_image)
myimage.place(x=20,y=20)

textfield=tk.Entry(root,justify="center",width=17,font=("poppins",25,"bold"),bg="#404040",border=0,fg="white")
textfield.place(x=50,y=40)
textfield.focus()  # Set focus to the text field

Search_icon=PhotoImage(file="search_icon.png")
myimage_icon=Button(image=Search_icon,borderwidth=0,cursor="hand2",bg="#404040",command=getWeather)
myimage_icon.place(x=400,y=34)

#logo image
Logo_image=PhotoImage(file="logo.png")
logo=Label(image=Logo_image)
logo.place(x=150,y=100)

#Bottom box
Frame_image=PhotoImage(file="box.png")
frame_myimage=Label(image=Frame_image)
frame_myimage.pack(padx=5,pady=5,side=BOTTOM)

#time
name=Label(root,font=("arial",15,"bold"))
name.place(x=30,y=100)
clock=Label(root,font=("Helvetica",20))
clock.place(x=30,y=130)


#label
color_code = "#1ab5ef"
Label1=Label(root,text="WIND",font=("Helvetica",15,'bold'),fg="white",bg=color_code)
Label1.place(x=120,y=400)

Label2=Label(root,text="HUMIDITY",font=("Helvetica",15,'bold'),fg="white",bg=color_code)
Label2.place(x=250,y=400)

Label3=Label(root,text="DESCRIPTION",font=("Helvetica",15,'bold'),fg="white",bg=color_code)
Label3.place(x=430,y=400)

Label4=Label(root,text="PRESSURE",font=("Helvetica",15,'bold'),fg="white",bg=color_code)
Label4.place(x=650,y=400)

t=Label(font=("arial",70,"bold"),fg="#ee666d")
t.place(x=400,y=150)
c=Label(font=("arial",15, 'bold'))
c.place(x=400,y=250)

w=Label(text="...",font=("arial",20,"bold"),bg=color_code)
w.place(x=120,y=430)

h=Label(text="...",font=("arial",20,"bold"),bg=color_code)
h.place(x=280,y=430)

d=Label(text="...",font=("arial",20,"bold"),bg=color_code)
d.place(x=450,y=430)

p=Label(text="...",font=("arial",20,"bold"),bg=color_code)
p.place(x=670,y=430)

root.mainloop()