import operator

def calc():
    a = 100
    b = 200
    if a == b:
        return operator.add(a, b)
    elif a > b:
        return operator.sub(a, b)
    else:
        return operator.mul(a, b)

print(calc())