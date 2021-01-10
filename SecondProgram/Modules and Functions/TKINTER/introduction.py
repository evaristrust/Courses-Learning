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
main_window.geometry('640x480')

label = tkinter.Label(main_window, text="HELLO WORLD")
label.pack(side="top")

canvas = tkinter.Canvas(main_window,relief="raised", borderwidth=1)
# canvas.pack(side="left", fill=tkinter.BOTH, expand=True) # it's now expanded both X and Y
# now add some buttons to our tkinter canvas
canvas.pack(side="left")
button1 = tkinter.Button(main_window, text="BUTTON1")
button2 = tkinter.Button(main_window, text="BUTTON2")
button3 = tkinter.Button(main_window, text="BUTTON3")
button4 = tkinter.Button(main_window, text="BUTTON4")
button5 = tkinter.Button(main_window, text="BUTTON5")

# add pack to the buttons

button1.pack(side="left", anchor="n") # it means the button is north left
button2.pack(side="left", anchor="s")
button3.pack(side="left", anchor="e")
button4.pack(side="top")
button5.pack(side="right", anchor="s")
main_window.mainloop()















