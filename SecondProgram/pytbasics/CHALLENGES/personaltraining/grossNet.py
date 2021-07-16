#ask a user their gross salary to output their net salary (Rwandan)
#try and see if you can compute their gross pay from their net pay
class Net:

    def __init__(self, balance):
        self._balance = balance

    def getNet(self):
        low = 30000 # lower earning (zero taxed)
        med = 100000 # medium earning (20% taxed)
        p = int(input('What\'s your gross salary? ')) # the amount in gross
        s = p * 0.033 # social security contribution in rwanda
        if p <= low:
            print('Your Net Salary is {}'.format(round(p - s))) #rounding to get whole number Net pay
        elif p <= med:
            print('Your Net Salary is {}'.format(round(p - ((p-low)*0.2 + s))))
        else:
            print('Your Net Salary is {}'.format(round(p - ((p-med)*0.3 + (70000*0.2) + s))))

if __name__ == '__main__':
    check = Net(0)

while check:
    user = input('Wanna check your net or your gross? ')
    if user.upper() == 'NET':
        check.getNet()
    else:
        print('sorry, we don\'t have that option')
        break
