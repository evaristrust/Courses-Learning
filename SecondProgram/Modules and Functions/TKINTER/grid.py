try:
    import tkinter
except ImportError: # python 2
    import tkinter as tkinter

# print(tkinter.TkVersion)
# print(tkinter.TclVersion)

# tkinter._test()

# Try something out of tkinter

main_window = tkinter.Tk()
main_window.title("INTRODUCTION TO TKINTER")
main_window.geometry('640x480-8-200')

#column 0 will be occupied by the Label
label = tkinter.Label(main_window, text="HELLO WORLD")
label.grid(row=0, column=0)

#left from will be occupied by canvas!
left_frame = tkinter.Frame(main_window)
left_frame.grid(row=1, column=1)

canvas = tkinter.Canvas(left_frame, relief="raised", borderwidth=1)
canvas.grid(row=1, column=0)

#rightFrame will be occupied by the buttons
right_frame = tkinter.Frame(main_window)
right_frame.grid(row=1, column=2, sticky="n") # sticky plays a role as anchor

# now add some buttons to our tkinter canvas
button1 = tkinter.Button(right_frame, text="BUTTON1", background="black")
button2 = tkinter.Button(right_frame, text="BUTTON2")
button3 = tkinter.Button(right_frame, text="BUTTON3")
button4 = tkinter.Button(right_frame, text="BUTTON4")
button5 = tkinter.Button(right_frame, text="BUTTON5")

# add pack to the buttons

button1.grid(row=1, column=0)
button2.grid(row=2, column=0)
button3.grid(row=3, column=0)
button4.grid(row=4, column=0)
button5.grid(row=5, column=0)

# configuring the columns
main_window.columnconfigure(0, weight=1)
main_window.columnconfigure(1, weight=1)
main_window.grid_columnconfigure(2, weight=1)

left_frame.config(relief="sunken", borderwidth=1)
right_frame.config(relief="sunken", borderwidth=1)
left_frame.grid(sticky="ns")
right_frame.grid(sticky="new")

right_frame.columnconfigure(0, weight=1)
button3.grid(sticky="ew")
main_window.mainloop()
# now buttons are well organised but are










