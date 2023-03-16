# FloatingClock
This Python code creates a `clock with a rounded GUI window that displays` **hours**, **minutes**, and **seconds**.
This code imports the `Tkinter module` as `tk` and the `datetime module` from the standard library.

The code defines a function called `center_window`, which takes a **root parameter** representing the root window of the application. The function is used to center the root window on the screen. It first gets the **requested width and height** of the root window and then calculates the position of the window on the screen using the screen width and height. It then sets the geometry of the root window to this position, with a size of `150x80`. It also sets the **background color** of the root window to `black` and makes the window **slightly transparent** with an `alpha value of` **0.9**. Finally, it adds a rounded border to the window.

The code defines another function called `update_clock`, which **updates the label on the root window with the current time every second**. It gets the `current time using `**the datetime module** and formats it to show the `hours`,` minutes`, and `seconds`. It then sets the text of the `clock_label label` to this current time.

The code creates a new instance of the **Tk class** called `root `and sets its title to **"Clock"**. It then calls the `center_window` function to **center the window on the screen**. It creates a new Label widget called` clock_label` and sets its font to '**calibri**' with a **size of 40**, its `background` to **black**, and its `foreground` to **white**. It packs the clock_label widget with a `padding `of **20 pixels**. Finally, it calls the `update_clock` function to **start updating the clock** label every second and starts the **Tkinter event loop** using the `mainloop()` method on the root window.
![image](https://user-images.githubusercontent.com/106637184/225600713-bd81c7aa-ae38-43df-b560-ec3c5769d388.png)
