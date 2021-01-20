def spam1():

    def spam2():

        def spam3():
            z = " Value 3"
            print("In spam3: locals are {}".format(locals()))
            return z
        y = " Value 2" # y must exist before spam3 is called
        y += spam3() # please do not combine the assignments
        print("In spam2: locals are {}".format(locals()))
        return y
    x = " Value 1" # x must exist before spm2 is called
    x += spam2() # please do not combine the assignments
    print("In spam1: locals are {}".format(locals()))
    return x

print(spam1())

# In the module scope, locals and globals are exactly the same
print(locals())
print(globals())