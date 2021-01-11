try:
    import tkinter
except ImportError: # python 2
    import Tkinter as tkinter

# print(tkinter.TkVersion)
# print(tkinter.TclVersion)

# tkinter._test()

# Try something out of tkinter

main_window = tkinter.Tk()
main_window.title("INTRODUCTION TO TKINTER")
main_window.geometry('640x480+8+200')

label = tkinter.Label(main_window, text="HELLO WORLD")
label.pack(side="top")

leftframe = tkinter.Frame(main_window)
leftframe.pack(side="left", anchor="n", fill=tkinter.Y, expand=False)

rightframe = tkinter.Frame(main_window)
rightframe.pack(side="right", anchor="n", expand=True)

canvas = tkinter.Canvas(leftframe,relief="raised", borderwidth=1)
canvas.pack(side="left")

# now add some buttons to our tkinter canvas
button1 = tkinter.Button(rightframe, text="BUTTON1", background="black")
button2 = tkinter.Button(rightframe, text="BUTTON2")
button3 = tkinter.Button(rightframe, text="BUTTON3")
button4 = tkinter.Button(rightframe, text="BUTTON4")
button5 = tkinter.Button(rightframe, text="BUTTON5")

# add pack to the buttons

button1.pack(side="top")
button2.pack(side="top")
button3.pack(side="top")
button4.pack(side="top")
button5.pack(side="top")
main_window.mainloop()
# now buttons are well organised













