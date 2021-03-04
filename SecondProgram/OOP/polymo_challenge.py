# there are two birds here: duck and pinguin
# They both walk, swim, and quack
# they can also fly
# do a program
class Wing(object):
    def __int__(self, ratio):
        self.ratio = ratio
    def fly(self):
        if self.ratio > 1:
            print('I will fly easily yollaaaa')
        elif self.ratio == 1:
            print('It is hard but I will try to fly')
        else:
            print('I think i can just walk')

class Duck(object):
    def walk(self):
        print('I will walk till I die')
    def swim(self):
        print('This water is so woww to go through')
    def quack(self):
        print('Boom!! such sound\'s is terrible')
    # def fly(self):
    #     self._wing.fly()

class Pinguin(object):
    def walk(self):
        print('I like to see people when I am walking')
    def swim(self):
        print('This ocean is too large, I can\'t manage it')
    def quack(self):
        print('OMG, Can I really play such music with my voice?')
#create a function to test
def test_duck(duck):
    duck.walk()
    duck.swim()
    duck.quack()

if __name__ == '__main__':
    duck_obj = Duck()
    ping_obj = Pinguin()
    #invoking the function test_duck down here
    test_duck(duck_obj)
    test_duck(ping_obj)
 
