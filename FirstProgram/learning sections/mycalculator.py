import re

print("Our Magical calculator")

# Create a way to end or quit the run
print("Type 'quit' to exit\n")
previous = 0
run = True


def perform_math():
    # Trying to access the global variables run and previous
    global run
    global previous
    equation = ""
    if previous == 0:
        equation = input("Enter equation:")
    else:
        equation = input(str(previous))

    # check if someone type quit
    if equation == "quit":
        run = False
    else:
        # using REGEX just to remove some characters
        equation = re.sub("[a-zA-Z,.:()" "]", " ", equation)
        # using eval to return an integer when string is entered
        if previous == 0:
            previous = eval(equation)
        else:
            previous = eval(str(previous) + equation)
        # print("You typed", previous)


while run:
    perform_math()
