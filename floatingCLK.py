import tkinter as tk
from tkinter import filedialog, colorchooser
from pygame import mixer
from datetime import datetime

def center_window(root):
    # Gets the requested values of the height and width.
    windowWidth = root.winfo_reqwidth()
    windowHeight = root.winfo_reqheight()

    # Gets both half the screen width/height and window width/height
    positionRight = int(root.winfo_screenwidth() / 2 - windowWidth / 2)
    positionDown = int(root.winfo_screenheight() / 2 - windowHeight / 2)

    # Positions the window in the center of the page.
    root.geometry("+{}+{}".format(positionRight, positionDown))
    root.overrideredirect(True)
    root.geometry("150x80")
    root.configure(bg='black')
    root.attributes("-alpha", 0.9)

    # Add a rounded border to the window
    root.wm_attributes('-transparentcolor', root['bg'])
    root.wm_attributes('-alpha', 0.9)
    root.attributes("-transparent", "blue")
    root.attributes('-alpha', 0.9)
    root.wait_visibility(root)
    root.wm_attributes('-alpha', 1.0)
    root.update_idletasks()
    root.wm_attributes('-alpha', 0.9)
    root.update_idletasks()
    root.overrideredirect(False)

alarm_time_var = None
alarm_time = None

def update_clock():
    global alarm_time

    current_time = datetime.now().strftime('%H:%M:%S')
    clock_label.config(text=current_time)

    if alarm_time and current_time == alarm_time:
        mixer.music.load(song_file)
        mixer.music.play()

    root.after(1000, update_clock)


def set_alarm():
    global alarm_time
    global song_file
    alarm_time = f"{alarm_hour_var.get()}:{alarm_minute_var.get()}:{alarm_second_var.get()}"
    song_file = filedialog.askopenfilename()

    mixer.init()
    mixer.music.load(song_file)


def change_color():
    color = colorchooser.askcolor()
    root.configure(bg=color[1])


root = tk.Tk()
root.title('Clock')
center_window(root)

clock_label = tk.Label(root, font=('calibri', 40), background='black', foreground='white')
clock_label.pack(pady=20)

alarm_hour_var = tk.StringVar(root)
alarm_hour_var.set('00')

alarm_minute_var = tk.StringVar(root)
alarm_minute_var.set('00')

alarm_second_var = tk.StringVar(root)
alarm_second_var.set('00')

alarm_time_label = tk.Label(root, text='Alarm Time:', background='black', foreground='white')
alarm_time_label.pack()

alarm_hour_menu = tk.OptionMenu(root, alarm_hour_var, *[f'{h:02}' for h in range(25)])
alarm_hour_menu.pack(side='left')

tk.Label(root, text=':', background='black', foreground='white').pack(side='left')

alarm_minute_menu = tk.OptionMenu(root, alarm_minute_var, *[f'{m:02}' for m in range(60)])
alarm_minute_menu.pack(side='left')

tk.Label(root, text=':', background='black', foreground='white').pack(side='left')

alarm_second_menu = tk.OptionMenu(root, alarm_second_var, *[f'{s:02}' for s in range(60)])
alarm_second_menu.pack(side='left')

set_alarm_button = tk.Button(root, text='Set Alarm', command=set_alarm)
set_alarm_button.pack()

change_color_button = tk.Button(root, text='Change Color', command=change_color)
change_color_button.pack()

update_clock()

root.mainloop()
