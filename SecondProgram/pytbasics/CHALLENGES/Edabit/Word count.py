# Count the word is the
str = "You will come after"
new_str = str.split()
print(len(new_str))
print("//" * 40)
# count the number of words in a sentence!
# tell the user the sentence is short when less than 6 words
def word_count(str):
    user_input = str.split()
    if len(user_input) < 6:
        return ("That's so short sentence! "
                "You need at least 8 words")
    else:
        return ("Your sentence contains {} words".format(len(user_input)))
user_input = input("Your sentence: ")
print(word_count(user_input))

