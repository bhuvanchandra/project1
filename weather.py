import tkinter as tk
from tkinter import messagebox
import requests


def get_weather(city):
    url = f"https://wttr.in/{city}?format=j1"
    
    try:
        data = requests.get(url).json()
        c = data["current_condition"][0]

        return {
            "desc": c["weatherDesc"][0]["value"],
            "temp": c["temp_C"],
            "feels": c["FeelsLikeC"],
            "humidity": c["humidity"],
            "wind": c["windspeedKmph"],
        }

    except:
        return None


def search_weather():
    city = city_entry.get().strip()
    if not city:
        messagebox.showwarning("Error", "Please enter a city.")
        return

    weather = get_weather(city)
    if weather is None:
        messagebox.showerror("Error", "Couldn't fetch weather. Try another city.")
        return

    result_label.config(
        text=f"Weather in {city.title()}:\n"
             f"→ {weather['desc']}\n"
             f"→ Temperature: {weather['temp']}°C\n"
             f"→ Feels Like: {weather['feels']}°C\n"
             f"→ Humidity: {weather['humidity']}%\n"
             f"→ Wind: {weather['wind']} km/h"
    )


# ---------------- GUI ---------------- #

root = tk.Tk()
root.title("Weather App ")
root.geometry("400x300")
root.resizable(False, False)

tk.Label(root, text="Weather App", font=("Arial", 18, "bold")).pack(pady=10)

city_entry = tk.Entry(root, font=("Arial", 14), justify="center")
city_entry.pack(pady=10)

tk.Button(root, text="Get Weather", font=("Arial", 14), command=search_weather).pack(pady=5)

result_label = tk.Label(root, font=("Arial", 12), justify="left")
result_label.pack(pady=10)

root.mainloop()

