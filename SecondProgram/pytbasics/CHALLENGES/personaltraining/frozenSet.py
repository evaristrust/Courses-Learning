#from a sentence, show only consonents
sentence_input = input('Enter your full sentence: ').lower()
vowels = frozenset('aueio ') #frozen sent for the vowels
sentence_set = set(sentence_input) # set for the entire sentence
final_result = sentence_set.difference(vowels)
# print(sorted(final_result))
for cons in sorted(final_result):
    print(cons, end=' ')
