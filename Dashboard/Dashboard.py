import tkinter as tk
import tkinter.font as tkFont

window = tk.Tk()
# window name is convertor1
window.title("Dashboard")

window.columnconfigure(0, minsize = 1080, weight = 1)

# the list to store icon path of the menue
menue_left = [tk.PhotoImage(file = "Dashboard.png"),
              tk.PhotoImage(file = "Convert.png"),
              tk.PhotoImage(file = "PUSH.png"),
              tk.PhotoImage(file = "PULLED Reports.png")]

menue_right = [tk.PhotoImage(file = "Help.png"),
               tk.PhotoImage(file = "Notifications.png"),
               tk.PhotoImage(file = "Settings.png")]
# the dictionary to store title of table1
table1 = {0:"Date", 1:"Data Source", 2:"Output Folder", 3:"Converted Format", 4:"Size (KB)",
          5:"No of Transaction", 6:"Check Sum", 7:"Status", 8:"Extended Information",
          9:"Details", 10:"User"}
# the dictionary to store title of table2
table2 = {0: "Upload Date", 1: "Output Folder", 2: "File Format", 3:"File Name", 4:"Size (KB)",
          5:"No of Transaction", 6:"Check Sum", 7:"PUID", 8:"Status", 9:"Extended Information",
          10:"Details", 11:"Action"}

# setup the frame frame_head and frame_centre
frame_menue = tk.Frame(master = window, pady = 2, borderwidth = 5, bg = "grey")
frame_centre = tk.Frame(master = window, pady = 2, borderwidth = 5, bg = "white")
frame_table1 = tk.Frame(master = frame_centre, pady = 30, borderwidth = 1, bg = "white")
frame_table2 = tk.Frame(master = frame_centre, pady = 2, borderwidth = 4, bg = "white")
frame_menue.grid(row = 0, column = 0, sticky = "new")
frame_centre.grid(row = 1, column = 0, sticky = "nsew")
frame_table1.pack()
frame_table2.pack()

# add left icon on menue
for photo in menue_left:
    button = tk.Button(master = frame_menue, image = photo)
    button.pack(side = tk.LEFT, padx = 10)

# add right icon on menue
for photo in menue_right:
    button = tk.Button(master = frame_menue, image = photo)
    button.pack(side = tk.RIGHT, padx = 10)

# allocate data to table 1
for index_y in range (3):
    # show title
    if index_y == 0:
        for index_x, head in table1.items():
            table1_title = tk.Label(master = frame_table1, text = head, padx = 5, pady = 5, font = tkFont.Font(size = 12))
            table1_title.grid(row = index_y, column = index_x, sticky = "n")

    else:
        # show contents
        for index_x in range(11):
            # show buttons in the corresponding index
            if index_x ==  1 or index_x == 2 or index_x == 9:
                table1_button = tk.Button(master = frame_table1, text = " button ", padx = 5, pady = 5, bg = "white", font = tkFont.Font(size = 12))
                table1_button.grid(row = index_y, column = index_x, sticky = "n")
            # show label in the corresponding index
            else:
                table1_content = tk.Label(master = frame_table1, text = "  data ", padx = 5, pady = 5, bg = "white", font = tkFont.Font(size = 12))
                table1_content.grid(row = index_y, column = index_x, sticky = "n")

# allocate data to table 2
for index_y in range (3):
    if index_y == 0:
        # show table title
        for index_x, head in table2.items():
            table1_title = tk.Label(master = frame_table2, text = head, padx = 5, pady = 5, font = tkFont.Font(size = 12))
            table1_title.grid(row = index_y, column = index_x, sticky = "n")

    else:
        # show contents
        for index_x in range(12):
            # show buttons
            if index_x ==  1 or index_x == 2 or index_x == 9:
                table1_button = tk.Button(master = frame_table2, text = " button ", padx = 5, pady = 5, bg = "white", font = tkFont.Font(size = 12))
                table1_button.grid(row = index_y, column = index_x, sticky = "n")
            # show labels
            else:
                table1_content = tk.Label(master = frame_table2, text = "  data ", padx = 5, pady = 5, bg = "white", font = tkFont.Font(size = 12))
                table1_content.grid(row = index_y, column = index_x, sticky = "n")

window.mainloop()
