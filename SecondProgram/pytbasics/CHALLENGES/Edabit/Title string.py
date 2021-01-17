# Check if a string txt is a title text or not.
# A title text is one which has all the words in
# the text start with an upper case letter.
def my_text(text):
    if text == text.title():
        print("The text is title")
    else:
        print("The text is not title")

my_text("World Health Organization")
my_text("World of Economy")

# or use istitle()
print("**" * 40)
# using the function and user_name!
full_name = input("Enter your name: ")
def your_text(text):
    text = full_name
    if text.istitle():
        print("Your name format is a Title!")
    else:
        print("Your name needs to be Capitalized")
your_text(full_name)

print("--" * 40)
my_name = "People Of Rwanda"
def is_title(str):
    # if str.istitle():
    if str == str.title():
        return ("You are right!")
    else:
        return ("You are wrong!")
print(is_title(my_name))

























