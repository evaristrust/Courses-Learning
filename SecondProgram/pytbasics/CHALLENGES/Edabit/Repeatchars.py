# Return a string doubled, you can use either function
# or just create a variable at the beginning
#
txt =input("Enter your word here: ")
results = " "
for x in txt:
     results += x * 2
print("{0} doubled is {1}".format(txt,results))

print("--" * 40)
txt =input("Enter your word here: ")
def double_name(wrd):
    final_results = " "
    wrd = txt

    for y in wrd:
        final_results += y * 2
    return final_results
print(double_name(txt))


my_original_text = input("Enter any word and see the double: ")
def create_double(name_):
    my_result = " "
    my_original_text = name_

    for x in name_:
        my_result += x * 2
    return my_result

print(create_double(my_original_text))










