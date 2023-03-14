import tkinter as tk
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


def update_clock():
    current_time = datetime.now().strftime('%H:%M:%S')
    clock_label.config(text=current_time)
    root.after(1000, update_clock)


root = tk.Tk()
root.title('Clock')
center_window(root)

clock_label = tk.Label(root, font=('calibri', 40), background='black', foreground='white')
clock_label.pack(pady=20)

update_clock()

root.mainloop()
