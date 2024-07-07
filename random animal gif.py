import tkinter as tk
from tkinter import colorchooser
from PIL import Image, ImageTk
import requests
from io import BytesIO

def fetch_animal_gif(color):
    url = f"https://api.pexels.com/v1/search?query=animal+{color}&per_page=1"
    headers = {
        "Authorization": "tCEN0qmdQsBEJ7OdoI1SNASx42M34d3m9mYlesdc"
    }
    
    response = requests.get(url, headers=headers)
    data = response.json()
    
    if data['photos']:
        image_url = data['photos'][0]['src']['medium']
        response = requests.get(image_url)
        img_data = response.content
        
        img = Image.open(BytesIO(img_data))
        img = img.resize((400, 400), Image.ANTIALIAS)
        img_tk = ImageTk.PhotoImage(img)
        
        img_label.config(image=img_tk)
        img_label.image = img_tk
    else:
        img_label.config(text="No GIF found for the chosen color")

def choose_color():
    color_code = colorchooser.askcolor(title="Choose color")
    color = color_code[1]
    color_label.config(text=f"Chosen Color: {color}", bg=color)
    fetch_animal_gif(color)

root = tk.Tk()
root.title("Random Animal GIF Generator")

color_label = tk.Label(root, text="Choose a color", font=("Arial", 14))
color_label.pack(pady=10)

choose_color_button = tk.Button(root, text="Choose Color", command=choose_color, font=("Arial", 14))
choose_color_button.pack(pady=10)

img_label = tk.Label(root, text="", font=("Arial", 14))
img_label.pack(pady=20)

root.mainloop()
