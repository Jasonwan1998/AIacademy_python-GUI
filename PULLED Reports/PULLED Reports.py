import tkinter as tk
import tkinter.font as tkFont

window = tk.Tk()
# window name is convertor1
window.title("PULLED Reports")

window.columnconfigure(0, minsize = 1080, weight = 1)

# the list to store icon path of the menue
menue_left = [tk.PhotoImage(file = "Dashboard.png"),
              tk.PhotoImage(file = "Convert.png"),
              tk.PhotoImage(file = "PUSH.png"),
              tk.PhotoImage(file = "PULLED Reports.png")]

menue_right = [tk.PhotoImage(file = "Help.png"),
               tk.PhotoImage(file = "Notifications.png"),
               tk.PhotoImage(file = "Settings.png")]

# setup the frame frame_head and frame_centre
frame_menue = tk.Frame(master = window, pady = 2, borderwidth = 5, bg = "grey")
frame_centre = tk.Frame(master = window, pady = 2, borderwidth = 5, bg = "white")
frame_menue.grid(row = 0, column = 0, sticky = "new")
frame_centre.grid(row = 1, column = 0, sticky = "nsew")


# add left icon on menue
for photo in menue_left:
    button = tk.Button(master = frame_menue, image = photo)
    button.pack(side = tk.LEFT, padx = 10)

# add right icon on menue
for photo in menue_right:
    button = tk.Button(master = frame_menue, image = photo)
    button.pack(side = tk.RIGHT, padx = 10)

label1 = tk.Label(master = frame_centre, bg = "white" , text = " 1. Bank Report")
label1.grid(row = 0, column = 0, sticky = "w")

label2 = tk.Label(master = frame_centre, bg = "white" , text = " 2. Report by name, date")
label2.grid(row = 1, column = 0, sticky = "w")

label3 = tk.Label(master = frame_centre, bg = "white" , text = " 3. Pull button to pull files from file server")
label3.grid(row = 2, column = 0, sticky = "w")

window.mainloop()
