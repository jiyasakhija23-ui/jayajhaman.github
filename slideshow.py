from itertools import cycle
from PIL import Image, ImageTk
import tkinter as tk

root = tk.Tk()
root.title("Image Slideshow Viewer")
root.geometry("800x800")

# List of image paths
image_paths = [
    r"C:\Users\Lenovo P52S\OneDrive\Pictures\133858187290553161.jpg",
    r"C:\Users\Lenovo P52S\OneDrive\Pictures\133865483458303624.jpg",
    r"C:\Users\Lenovo P52S\OneDrive\Pictures\133865483499664054.jpg",
    r"C:\Users\Lenovo P52S\OneDrive\Pictures\133879009306206560.jpg",
    r"C:\Users\Lenovo P52S\OneDrive\Pictures\download (1).jpg",
]

# Resize images
image_size = (700, 700)
images = [Image.open(path).resize(image_size) for path in image_paths]
photo_images = [ImageTk.PhotoImage(image) for image in images]

# Label to display images
label = tk.Label(root)
label.pack()

# Create cycle iterator
slideshow = cycle(photo_images)

def update_image():
    photo = next(slideshow)
    label.config(image=photo)
    label.image = photo  # prevent garbage collection
    root.after(3000, update_image)  # change every 3 seconds

# Button to start slideshow
play_button = tk.Button(root, text="Play Slideshow", command=update_image)
play_button.pack(pady=10)

root.mainloop()