try:
    import tkinter
except ImportError: # python 2
    import tkinter as tkinter
import os

# print(tkinter.TkVersion)
# print(tkinter.TclVersion)

# tkinter._test()

# Try something out of tkinter

main_window = tkinter.Tk()
main_window.title("GRID ASSHOLE")
main_window.geometry('640x480-8-200')
main_window["padx"] = 8
label = tkinter.Label(main_window, text="Tkinter Grid Asshole")
label.grid(row=0, column=0, columnspan=3)

#configure rows and columns

main_window.columnconfigure(0, weight=1)
main_window.columnconfigure(1, weight=1)
main_window.columnconfigure(2, weight=3)
main_window.columnconfigure(3, weight=3)
main_window.columnconfigure(4, weight=3)
main_window.rowconfigure(0, weight=1)
main_window.rowconfigure(1, weight=10)
main_window.rowconfigure(2, weight=1)
main_window.rowconfigure(3, weight=3)
main_window.rowconfigure(4, weight=3)

# going to add a listbox

file_list = tkinter.Listbox(main_window)
file_list.grid(row=1, column=0, sticky="nsew", rowspan=2)
file_list.config(border=2, relief="sunken")
for zone in os.listdir("/Windows/System32"): # On mac, /usr/bin
    file_list.insert(tkinter.END, zone)

# adding the scrolling option

list_scroll = tkinter.Scrollbar(main_window, orient=tkinter.VERTICAL,
                                command=file_list.yview)
list_scroll.grid(row=1, column=1, sticky="nsw", rowspan=2)
file_list["yscrollcommand"] = list_scroll.set

#let's do an option frame

option_frame = tkinter.LabelFrame(main_window, text="File Details")
option_frame.grid(row=1, column=2, sticky="ne")

# create a variable of rbValue to create 3 similar radio buttons
rb_value = tkinter.IntVar()
rb_value.set(1)
#3 radio buttons
radio1 = tkinter.Radiobutton(option_frame, text="FileName", value=1, variable=rb_value)
radio2 = tkinter.Radiobutton(option_frame, text="FilePath", value=2, variable=rb_value)
radio3 = tkinter.Radiobutton(option_frame, text="Timestamp", value=3, variable=rb_value)
radio1.grid(row=0, column=0, sticky="w")
radio2.grid(row=1, column=0, sticky="w")
radio3.grid(row=2, column=0, sticky="w")

# Do the result label
# Widget to display the results

result_label = tkinter.Label(main_window, text="Results")
result_label.grid(row=2, column=2, sticky="nw")
results = tkinter.Entry(main_window)
results.grid(row=2, column=2, sticky="sw")

#Frame for the time spinners
time_frame = tkinter.LabelFrame(main_window, text="Time")
time_frame.grid(row=3, column=0, sticky="new")

#Time spinners
hour_spinner = tkinter.Spinbox(time_frame, width=2, value=tuple(range(0, 24)))
minute_spinner = tkinter.Spinbox(time_frame, width=2, from_=0, to_=59)
second_spinner = tkinter.Spinbox(time_frame, width=2, from_=0, to_=59) # using to_ and from_ not range()
hour_spinner.grid(row=0, column=0)
tkinter.Label(time_frame, text=":").grid(row=0, column=1)
minute_spinner.grid(row=0, column=2)
tkinter.Label(time_frame, text=":").grid(row=0, column=3)
second_spinner.grid(row=0, column=4)
# add padding
time_frame["padx"] = 36

# add frame for the date spinners
date_frame = tkinter.Frame(main_window)
date_frame.grid(row=4, column=0, sticky="new")
# date labels
day_label = tkinter.Label(date_frame, text="Day")
month_label = tkinter.Label(date_frame, text="Month")
year_label = tkinter.Label(date_frame, text="Year")
day_label.grid(row=0, column=0, sticky="w")
month_label.grid(row=0, column=1, sticky="w")
year_label.grid(row=0, column=2, sticky="w")
#date spinners
day_spinner = tkinter.Spinbox(date_frame, width=5, from_=1, to_=31)
month_spinner = tkinter.Spinbox(date_frame, width=5, value=("Jan", "Feb", "Mar", "Apr",
                                                            "May", "June", "July", "Aug",
                                                            "Sep", "Oct", "Nov", "Dec"))
year_spinner = tkinter.Spinbox(date_frame, width=5, from_=2000, to_=2099)
day_spinner.grid(row=1, column=0)
month_spinner.grid(row=1, column=1)
year_spinner.grid(row=1, column=2)

# Ok and Cancel Buttons

ok_button = tkinter.Button(main_window, text="OK")
cancel_button = tkinter.Button(main_window, text="CANCEL", command=main_window.quit) # you can use destroy. without ()
ok_button.grid(row=4, column=3, sticky="e")
cancel_button.grid(row=4, column=4, sticky="w")
main_window.mainloop()
print(rb_value.get()) # this will print out the value of the radio buttons that is ticked

