import tkinter as tk
import time
import math

root = tk.Tk()
root.title("Analog Clock")
root.geometry("500x600")
root.configure(bg="black")

canvas = tk.Canvas(root, width=500, height=600, bg="black", highlightthickness=0)
canvas.pack()

center_x = 250
center_y = 250
radius = 200

# Clock circle
canvas.create_oval(center_x - radius, center_y - radius,
                   center_x + radius, center_y + radius,
                   outline="white", width=3)

# Numbers 1–12
for i in range(1, 13):
    angle = math.radians(i * 30)
    x = center_x + 170 * math.sin(angle)
    y = center_y - 170 * math.cos(angle)
    canvas.create_text(x, y, text=str(i),
                       fill="white", font=("Arial", 14, "bold"))

# Better spaced text positions
date_text = canvas.create_text(250, 460, fill="white", font=("Arial", 16, "bold"))
day_text  = canvas.create_text(250, 500, fill="white", font=("Arial", 14))
time_text = canvas.create_text(250, 540, fill="white", font=("Arial", 14, "bold"))

def update_clock():
    canvas.delete("hands")

    t = time.localtime()
    sec = t.tm_sec
    minute = t.tm_min
    hour = t.tm_hour % 12

    # Date / Day / Time
    canvas.itemconfig(date_text, text="" + time.strftime("%d-%m-%Y"))
    canvas.itemconfig(day_text, text="" + time.strftime("%A"))
    canvas.itemconfig(time_text, text="" + time.strftime("%I:%M:%S %p"))

    # Angles
    sec_angle = math.radians(sec * 6)
    min_angle = math.radians(minute * 6 + sec * 0.1)
    hour_angle = math.radians(hour * 30 + minute * 0.5)

    # Second hand
    sec_x = center_x + 180 * math.sin(sec_angle)
    sec_y = center_y - 180 * math.cos(sec_angle)
    canvas.create_line(center_x, center_y, sec_x, sec_y,
                       fill="red", width=2, tag="hands")

    # Minute hand
    min_x = center_x + 140 * math.sin(min_angle)
    min_y = center_y - 140 * math.cos(min_angle)
    canvas.create_line(center_x, center_y, min_x, min_y,
                       fill="white", width=4, tag="hands")

    # Hour hand
    hour_x = center_x + 100 * math.sin(hour_angle)
    hour_y = center_y - 100 * math.cos(hour_angle)
    canvas.create_line(center_x, center_y, hour_x, hour_y,
                       fill="white", width=6, tag="hands")

    # Center dot
    canvas.create_oval(center_x-6, center_y-6,
                       center_x+6, center_y+6,
                       fill="white", tag="hands")

    root.after(1000, update_clock)

update_clock()
root.mainloop()

