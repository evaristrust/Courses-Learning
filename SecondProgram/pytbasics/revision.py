# # We are going to give chances for people with first_names begins with
# # E, P, K, C, B
#
# # random_names = 'EPKCB'
# # name_upper = random_names.upper()
# # name = input('What is your name dear? ')
# # first_letter = input('Hello {}, what\'s your first letter of your first name in CAPITAL LETTER! '.format(name))
# #
# # if first_letter in name_upper:
# #     print('You are among the winners of this rotor')
# # else:
# #     print('Sorry {}! You are not among the winners'.format(name))
#
# letter = ['E', 'V', 'A', 'R', 'I', 'S', 'T', 'E']
#
# full_name = ''.join(letter)
#
# print(full_name)
#
# number = "12 345678735679"
# print(number[0:6])
# # will have to understand this too
# print(number[1::3]) # access an item in the interval of three places
#
# # print months and their corresponding dates 28, 30, 31
#
# months = """
#          jan : {2}
#          feb : {0}
#          March : {2}
#          April : {1}
#          May : {2}
#          June : {1}
#          July : {2}
#          August : {2}
#          September : {1}
#          October : {2}
#          November : {1}
#          December : {2}
# """.format(28, 30, 31)
#
# print(months)
#
# # print the set of odd and even numbers
#
# even_numbers = set(range(0, 20, 2))
# print(even_numbers)
#
# # see something like discard and remove
#
# odd = set(range(1, 20, 2))
#
# print(odd)
#
# odd.discard(14) # discard will not throw an error
# print(odd)
#
# try:
#     odd.remove(16)
# except KeyError:
#     print('The element you are trying to remove is not there!')
#
# # find the intersection, union, difference between odd and multiple of three
#
# multiple_three = set(range(0,25, 3))
#
# print('The intersection is: ', odd.intersection(multiple_three))
#
# print('The union of them is: ', odd.union(multiple_three))
#
# print('The intersection can be: ', odd & multiple_three)
#
# print('The difference: ', odd - multiple_three)
# print('another difference is: ', odd.difference(multiple_three))
#
# #check if odd is the subset of the union
#
# print(odd.issubset(odd.union(multiple_three)))
#
# print(odd.union(multiple_three).issuperset(odd)) # checkin if the union is the superset
#
# # create a program that removes vowels from the sentence or paragraph
#
# sentence = 'Praise God from whom blessings flow! Praise him all creatures here below ?'
#
# v = frozenset('auoei')
#
# sentence_set = set(sentence)
# sentence_diff = (sentence_set.difference(v))
# print(sorted(sentence_diff))
#
# champions = {"epl": "Arsenal, Chelsea, Man utd",
#              "laliga": "Barcelona, Real Madrid, Atletico",
#              "serie_a": "Juventus, Inter, Ac Milan"}
# #
# # while True:
# #     check_teams = input('Enter the name of champions: ')
# #     if check_teams == 'quit':
# #         break
# #     if check_teams in champions:
# #         description = champions.get(check_teams)
# #         print('{} top teams are: {}'.format(check_teams, description))
# #     else:
# #         print('we are not able to find teams in {}'.format(check_teams))
#
#
# regions = {"Kigali city": "Gasabo, Kicukiro, Nyarugenge",
#              "South": "Nyaruguru, Gisagara, Huye",
#              "Noth": "Rulindo, Musanze, Gicumbi",
#              "East": "Kayonza, Rwamagana, Ngoma",
#              "West": "Rusizi, Nyamasheke, Karongi"}
# ordered_regions = sorted(list(regions.keys()))
# for provinces in ordered_regions:
#     print('{} districts are: {}'.format(provinces, regions[provinces]))
#
# my_tuple = regions.items()
# x = tuple(my_tuple)
#
# for tuple_1 in x:
#     provinces, districts = tuple_1
#     print('{} contains {}'.format(provinces, districts))

from turtle import circle, forward, backward, left, right, done

import time
#
# forward(100)
# backward(120)
# left(240)
# right(60)
# circle(100)
# time.sleep(10)
# done()
#
#
# import time
# import random
#
# from time import perf_counter as my_time
# input('press enter to start: ')
# wait_time = random.randint(1, 6)
# time.sleep(wait_time)
# start_time = my_time()
#
# input('press enter to stop: ')
# end_time = my_time()
#
# print('you started at ', time.strftime('%X',time.localtime(start_time)))
# print('you ended aat ', time.strftime('%X', time.localtime(end_time)))
# print('You used {} seconds'.format(end_time - start_time))

print(round(1.73))





