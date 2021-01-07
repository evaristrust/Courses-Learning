try:
    import tkinter
except ImportError:
    import tkinter as tkinter

def parabola(x):
    y = x * x / 100
    return y
# secondly, u will draw axes
def draw_axes(canvas):
    canvas.update()
    x_origin = canvas.winfo_width() / 2
    y_origin = canvas.winfo_height() / 2
    canvas.configure(scrollregion=(-x_origin, -y_origin, x_origin, y_origin))
    canvas.create_line(-x_origin, 0, x_origin, 0, fill="black")
    canvas.create_line(0, y_origin, 0, -y_origin, fill="black")
    print(locals()) # locals function to see the canvas variables

def plot(canvas, x, y):
    canvas.create_line(x, y, x + 1, y +1, fill="red")

#First, create a tkinter and canvas
main_window = tkinter.Tk()
main_window.title("My crap parabola")
main_window.geometry("640x480")
#creating the variable canvas
canvas = tkinter.Canvas(main_window, width=320, height=480)
canvas.grid(row=0, column=0)

# create a second canvas

canvas2 = tkinter.Canvas(main_window, width=320, height=480, background="green")
canvas2.grid(row=0, column=1)
print(repr(canvas), repr(canvas2)) # print the canvas objects
draw_axes(canvas)
draw_axes(canvas2)
for x in range(-100, 100):
    y = parabola(x) # calling and assigning a function to a varible
    plot(canvas, x, -y)

main_window.mainloop()