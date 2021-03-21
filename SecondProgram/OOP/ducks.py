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

    def __int__(self):
        self._wing = Wing(1.8)

    def walk(self):
        print('I will walk till I die')

    def swim(self):
        print('This water is so woww to go through')

    def quack(self):
        print('Boom!! such sound\'s is terrible')

    def fly(self):
        try:
            self._wing.fly()
        except AttributeError:
            pass


class Pinguin(object):

    def walk(self):
        print('I like to see people when I am walking')

    def swim(self):
        print('This ocean is too large, I can\'t manage it')

    def quack(self):
        print('OMG, Can I really play such music with my voice?')


class Flock(object):
    def __int__(self):
        try:
            self.flock = []
        except AttributeError:
            pass

    def add_duck(self, duck):
        try:
            self.flock.append(duck)
        except AttributeError:
            pass

    def migrate(self):
        for duck in self.flock:
            try:
                duck.fly()
            except AttributeError:
                pass

if __name__ == '__main__':
    donald = Duck()
    donald.fly()

 
