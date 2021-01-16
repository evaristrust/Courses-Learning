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
def your_text(text):
    text = full_name
    if text.istitle():
        print("Your name format is correct!")
    else:
        print("Your name needs to be Capitalized")

full_name = input("Enter your name: ")

your_text(full_name)




