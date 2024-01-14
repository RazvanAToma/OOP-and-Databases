import tkinter as tk
from PIL import Image, ImageTk

top = tk.Tk()

# Title
top.title("GUI Application: Autonomy Class")

# Adjust size
top.geometry("500x300+500+50")

# Add color background
"""
top.configure(bg="red")
"""

# Add image
""" 
background_image = Image.open("C:/Users/razva/Documents/GitHub/OOP-and-Databases/Lab Exercises/Lab 2/usn.jpg")
background_image = ImageTk.PhotoImage(background_image)
background_label = tk.Label(top, image=background_image)
background_label.place(relwidth = 1, relheight = 1)
"""

# Buttons
def hello():
    print("Hello Python")

button = tk.Button(top, text="Hello", command=hello)
button.pack()

# Check buttons
check_button = tk.Checkbutton(top, text = "Sound")
check_button.pack()

# Label

grade_label = tk.Label(top, text = "Username")
grade_label.pack()

top.mainloop()