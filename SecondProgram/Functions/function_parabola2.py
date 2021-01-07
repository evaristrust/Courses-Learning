try:
    import tkinter
except ImportError:
    import tkinter as tkinter

def parabola(page, size):
    for x in range(-size, size):
        y = x * x / size
        plot(page, x, y)
# secondly, u will draw axes
def draw_axes(page):
    page.update()
    x_origin = page.winfo_width() / 2
    y_origin = page.winfo_height() / 2
    page.configure(scrollregion=(-x_origin, -y_origin, x_origin, y_origin))
    page.create_line(-x_origin, 0, x_origin, 0, fill="black")
    page.create_line(0, y_origin, 0, -y_origin, fill="black")
    print(locals()) # locals function to see the canvas variables

def plot(canvas, x, y):
    canvas.create_line(x, -y, x + 1, -y +1, fill="red") # y should be negative and x positive for a parabole

#First, create a tkinter and canvas
main_window = tkinter.Tk()
main_window.title("My crap parabola")
main_window.geometry("640x480")
#creating the variable canvas
canvas = tkinter.Canvas(main_window, width=640, height=480)
canvas.grid(row=0, column=0)

draw_axes(canvas) # calling the function

parabola(canvas, 100)
parabola(canvas, 200)

main_window.mainloop()