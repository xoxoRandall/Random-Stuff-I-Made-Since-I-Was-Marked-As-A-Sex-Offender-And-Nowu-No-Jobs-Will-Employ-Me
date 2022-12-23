import tkinter as tk
import datetime
import threading

# I'm  very sad and lonely I didn't mean to touch him

dc_time = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=-5)))
sf_time = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=-8)))

window = tk.Tk()
window.title("Time in Washington D.C. and San Francisco")
window.geometry("1920x1080")
window.configure(background='#3CB371')
window.attributes("-fullscreen", True)

dc_label = tk.Label(window, text=f"Time in Washington D.C. ({dc_time.strftime('%A')}): {dc_time.strftime('%I:%M %p')}", font=("Helvetica", 30, "bold"), fg="#FFFFFF", bg="#3CB371", anchor="center")
sf_label = tk.Label(window, text=f"Time in San Francisco ({sf_time.strftime('%A')}): {sf_time.strftime('%I:%M %p')}", font=("Helvetica", 30, "bold"), fg="#FFFFFF", bg="#3CB371", anchor="center")
second_timer = tk.Label(window, text="0", font=("Helvetica", 20), fg="#FFFFFF", bg="#3CB371", anchor="center")
dc_label.grid(row=0, column=0, sticky="ew")
second_timer.grid(row=1, column=0, sticky="nsew")
sf_label.grid(row=2, column=0, sticky="ew")

window.columnconfigure(0, weight=1)
window.rowconfigure(1, weight=1)

def update_time():
    global dc_label, sf_label, second_timer
    dc_time = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=-5)))
    sf_time = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=-8)))
    dc_label.config(text=f"Time in Washington D.C. ({dc_time.strftime('%A')}): {dc_time.strftime('%I:%M %p')}")
    sf_label.config(text=f"Time in San Francisco ({sf_time.strftime('%A')}): {sf_time.strftime('%I:%M %p')}")
    second_timer.config(text=f"Seconds since last minute: {datetime.datetime.now().second}")
    window.after(60, update_time)

update_time()


window.mainloop()
