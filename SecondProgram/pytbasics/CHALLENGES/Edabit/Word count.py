# Count the word is the
str = "You will come after"
new_str = str.split()
print(len(new_str))

def word_count(str):
    user_input = str.split()
    return ("Your sentence contains {} words".format(len(user_input)))

# ask a user
user_input = input("Your sentence: ")
print(word_count(user_input))