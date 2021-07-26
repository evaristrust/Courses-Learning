#ask a user their gross salary to output their net salary (Rwandan)
#ask a user their gross also to get their pay as you earn (PAYE) (rwanda)
class Net:

    def __init__(self, balance):
        self._balance = balance

    #function to compute the net salary
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

    #function to compute the pay as you earn (PAYE)
    def getPaye(self):
            low = 30000 # lower earning (zero taxed)
            med = 100000 # medium earning (20% taxed)
            p = int(input('What\'s your gross salary? ')) # the amount in gross
            if p <= low:
                print('Your PAYE is 0') #rounding to get whole number Net pay
            elif p <= med:
                print('Your PAYE is {}'.format((p-low)*0.2))
            else:
                print('Your PAYE is {}'.format((p-med)*0.3 + (70000*0.2)))

if __name__ == '__main__':
    check = Net(0)

while check:
    user = input('Wanna check your PAYE or NET Salary? ')
    if user.upper().strip() == 'NET':
        check.getNet()
    elif user.lower().strip() == 'paye':
        check.getPaye()
    else:
        print('sorry, we don\'t have that option')
        break
