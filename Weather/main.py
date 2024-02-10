import tkinter as tk
import customtkinter
from opencage.geocoder import OpenCageGeocode
import requests

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
weather_api_key = "03d467126321464d4ae9f8fde21ed351"
location_api_key = 'da9cc3fa89d64c8c91d2eaad00bcb85c'
location_to_search = 'Agalpur,Balangir'




def get_geolocation(location_api_key, location):
    global lat
    global lng
    global formatted_address
    geocoder = OpenCageGeocode(location_api_key)
    results = geocoder.geocode(location)

    if results and results[0]['geometry']:
        result = results[0]
        formatted_address = result['formatted']
        lat = result['geometry']['lat']
        lng = result['geometry']['lng']
        # location_label.configure(text = f"{formatted_address}")
        # print(f"Formatted Address: {formatted_address}")
        # print(f"Latitude: {lat}, Longitude: {lng}")
        global weather_params
        weather_params = {
            "lat": lat,
            "lon": lng,
            "units":"metric",
            "appid": weather_api_key,
        }
    else:
        location.configure(text = "No result found.")
        # print("No results found.")


get_geolocation(location_api_key, location_to_search)

serial_no=0

def weather_fun():
    global temperature
    global environment
    global environment_desc
    global wind_speed
    global date
    global time
    global times_list
    # global serial_no
    global prev_button
    response = requests.get(OWM_Endpoint, params=weather_params)
    weather_data = response.json()
    weather = weather_data["list"]
    times_list = []
    temp_list = []
    humidity_list = []
    wind_speed_list = []
    weather_list = []
    weather_desc_list = []
    

    # serial_no=0
    for day in weather:
        times_list.append(day['dt_txt'])
        temp_list.append(day['main']['temp'])
        humidity_list.append(day['main']['humidity'])
        wind_speed_list.append(day['wind']['speed'])
        weather_list.append(day['weather'][0]['main'])
        weather_desc_list.append(day['weather'][0]['description'])
        
    temperature = temp_list[serial_no]
    time = times_list[serial_no][11:]
    date = times_list[serial_no][:10]
    environment = weather_list[serial_no]
    environment_desc = weather_desc_list[serial_no]
    wind_speed = round(float(wind_speed_list[serial_no]),2)
    

        
    
    # time_label.config(text="Time: "+times_list[serial_no][11:])
    # date_label.config(text="Date: "+times_list[serial_no][:10])
    # temp_label.config(text="Temperature: "+str(temperature)+"K")
    # env_label.config(text="Environment: "+environment)
    # env_desc_label.config(text = "("+environment_desc+")")
    # wind_label.config(text="Wind Speed: "+str(wind_speed)+" m/s")
    # temperature = (weather[1]["main"]["temp"])+2    # Temperature
    # environment = weather[1]["weather"][0]["main"]   # Environment
    # environment_desc = (weather[1]["weather"][0]["description"]).title()    #Environment Description
    # wind_speed = weather[1]["wind"]["speed"]    # Wind Speed in m/s
    


# print(temperature)

weather_fun()



def center_window(app, width, height):
    screen_width = app.winfo_screenwidth()
    screen_height = app.winfo_screenheight()
    x_position = (screen_width - width) // 2
    y_position = (screen_height - height) // 2

    app.geometry(f"{width}x{height}+{x_position}+{y_position}")
    customtkinter.set_appearance_mode("dark")
    
def submit():
    # global serial_no
    # serial_no=0
    locations = location_entry.get()
    if serial_no == 0:
        prev_button.configure(state='disabled',border_color="grey")
    
    get_geolocation(location_api_key, locations)
    location.configure(text = f"{formatted_address}")
    weather_fun()
    wind_speed_label.configure(text=f"Wind Speed: {wind_speed} m/s")
    temperature_label.configure(text=f"{temperature}")
    env_label.configure(text=f"{environment}")
    env_desc_label.configure(text=f"{environment_desc}")
    # date_label.configure(text=f"{date}")
    time_label.configure(text=f"Updated on: {time} , {date}")
    
def next_time():
    # locations = location_entry.get()
    # get_geolocation(location_api_key, locations)
    # location.configure(text = f"{formatted_address}")
    global serial_no
    serial_no += 1
    if serial_no == 0:
        prev_button.configure(state='disabled') 
    elif serial_no >= len(times_list):
        serial_no = 0    
    else:
        prev_button.configure(state='normal')
        
    weather_fun()
    wind_speed_label.configure(text=f"Wind Speed: {wind_speed} m/s")
    temperature_label.configure(text=f"{temperature}")
    env_label.configure(text=f"{environment}")
    env_desc_label.configure(text=f"{environment_desc}")
    # date_label.configure(text=f"{date}")
    time_label.configure(text=f"Updated on: {time} , {date}")
    
def prev_time():
    # locations = location_entry.get()
    # get_geolocation(location_api_key, locations)
    # location.configure(text = f"{formatted_address}")
    global serial_no
    serial_no -= 1

    weather_fun()
    wind_speed_label.configure(text=f"Wind Speed: {wind_speed} m/s")
    temperature_label.configure(text=f"{temperature}")
    env_label.configure(text=f"{environment}")
    env_desc_label.configure(text=f"{environment_desc}")
    # date_label.configure(text=f"{date}")
    time_label.configure(text=f"Updated on: {time} , {date} ")
    if serial_no == 0:
        prev_button.configure(state='disabled')
    
    



    
def create_boxes():
    app = customtkinter.CTk()
    app.title("Wether Forecast")
    icon_path = "weather.ico"
    app.iconbitmap(icon_path)
    global wind_speed_label
    global temperature_label
    global env_label
    global env_desc_label
    global location
    global location_entry
    global prev_button
    global time_label
    
    # main_frame = customtkinter.CTkFrame(app, fg_color="transparent",width=650,height=500)

    # main_frame.pack()
    
    
    cloud_frame = customtkinter.CTkFrame(app, fg_color="transparent", border_width=2,corner_radius=50,border_color="#40A2E3",width=500, height=300)
    cloud_frame.grid(row=2,column=0,columnspan=3)
    
    temp_frame = customtkinter.CTkFrame(cloud_frame, fg_color="transparent", bg_color="transparent")
    temp_frame.grid(row=0, column=0, padx=20, pady=20)
    
    temperature_label =  customtkinter.CTkLabel(temp_frame, text=f"{temperature}", font=("Century Gothic", 60))
    temperature_label.grid(row=0, column=0)
    
    temperature_label_symbol =  customtkinter.CTkLabel(temp_frame, text="°C", font=("Century Gothic", 30))
    temperature_label_symbol.grid(row=0, column=1, padx=10, pady=10)
    
    env_frame = customtkinter.CTkFrame(cloud_frame, fg_color="transparent")
    env_frame.grid(row=1, column=0, padx=10, pady=20)
    
    env_label = customtkinter.CTkLabel(env_frame, text=f"{environment}", font=("Century Gothic", 20))
    env_label.grid(row=0, column=0)
    
    env_desc_label = customtkinter.CTkLabel(env_frame, text=f"{environment_desc}", font=("Century Gothic", 15))
    env_desc_label.grid(row=1, column=0)
    
    wind_speed_label = customtkinter.CTkLabel(env_frame, text=f"Wind Speed: {wind_speed} m/s", font=("Century Gothic", 15))
    wind_speed_label.grid(row=2, column=0)
    
    location_frame = customtkinter.CTkFrame(app,fg_color="transparent",width=150, height=50)
    location_frame.grid(row=1,column=4)
    
    
    location_label = customtkinter.CTkLabel(app, text="Location :", font=("Century Gothic", 15))
    location_label.grid(row=4,column=0,padx=20)
    
    
    location_entry = customtkinter.CTkEntry(app, width=150)
    location_entry.grid(row=4,column=1)
    
    submit_button = customtkinter.CTkButton(app, text="Submit", command=submit,width=100)
    submit_button.grid(row=4,column=2,padx=20,pady=20)
    
    
    location = customtkinter.CTkLabel(app, text=f"{location_to_search}", font=("Century Gothic", 15))
    location.grid(row=0, column=0,padx=20,pady=20,columnspan=5,sticky='wn')
    
    
    # date_time_frame = customtkinter.CTkFrame(app, fg_color="transparent")
    # date_time_frame.grid(row=1,column=0,sticky='n')
    
    # date_label = customtkinter.CTkLabel(date_time_frame, text=f"{date}", font=("Century Gothic", 15))
    # date_label.grid(row=0, column=0)
    
    time_label = customtkinter.CTkLabel(app, text=f"{time}", font=("Century Gothic", 15))
    time_label.grid(row=1, column=0,sticky='wn',padx=20,columnspan=5)
    
    button_frame = customtkinter.CTkFrame(app, fg_color="transparent")
    button_frame.grid(row=3, column=0,columnspan=3)
    
    next_button = customtkinter.CTkButton(button_frame, text=">", command=next_time, width=50,height=30,corner_radius=50,fg_color='transparent',border_width=2,border_color="#40A2E3")
    next_button.grid(row=0, column=1, padx=20, pady=20)
    
    prev_button = customtkinter.CTkButton(button_frame, text="<", command=prev_time, width=50,height=30,corner_radius=50,fg_color='transparent',border_width=2,border_color="#40A2E3")
    prev_button.grid(row=0, column=0,padx=20, pady=20)
    
    
    







    # center_frame(app,main_frame,650,500)

    center_window(app, 400, 500)

    app.mainloop()
    
create_boxes()