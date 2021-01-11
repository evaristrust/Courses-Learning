try:
    import tkinter
except ImportError: # python 2
    import Tkinter as tkinter
import os

keys = [[("C", 1), ("CE", 1)],
        [("7", 1), ("8", 1), ("9", 1), ("+", 1)],
        [("4", 1), ("5", 1), ("6", 1), ("-", 1)],
        [("1", 1), ("2", 1), ("3", 1), ("*", 1)],
        [("0", 1), ("=", 1), ("/", 1)]
        ]
# start by adding padding

main_window_padding = 40
main_window = tkinter.Tk()
main_window.title("Eva Calculator")
main_window.geometry("480x480-8-200")
main_window["padx"] = main_window_padding

results = tkinter.Entry(main_window)
results.grid(row=0, column=0, sticky="nsew")

key_pad = tkinter.Frame(main_window)
key_pad.grid(row=1, column=0, sticky="nsew")

# our loop
row = 0
for key_row in keys:
    col = 0
    for key in key_row:
        tkinter.Button(key_pad, height=2, width=3, text=key[0]).grid(row=row, column=col,
                                                  columnspan=key[1], sticky=tkinter.E + tkinter.W)
        col += key[1] # key[1] is always 1 in the keys..
    row += 1
main_window.update()
main_window.minsize(key_pad.winfo_width() + main_window_padding, results.winfo_height() + key_pad.winfo_height())
main_window.maxsize(key_pad.winfo_width() + 50 + main_window_padding, results.winfo_height() + 50 + key_pad.winfo_height())
# 50 added on left and right to limit the maximum length of the window! if it's removed, it will be set to the calculator
# height and width by default
main_window.mainloop()