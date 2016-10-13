from random import choice, randint

from string import digits
from string import ascii_letters

class Generator:

    def __init__(self):
        self.types = ['int', 'int', 'int', 'short', 'long', 'char', '']
        self.letters = ascii_letters + digits
        self.helpers = [',', '(',')']

    def gen_empty(f):
        def wraped(self):
            result = f(self)
            return result + "".join(" " for i in range(randint(0, 4)))
        return wraped

    @gen_empty
    def gen_type(self):
        return "".join(choice(self.types))

    @gen_empty
    def gen_name(self):
        return "".join(choice(self.letters) for i in range(randint(0, 17)))

    @gen_empty
    def gen_helpers(self):
        return "".join(choice(self.helpers))


    def gen_params(self):
        result = ""
        self.count_params = randint(0, 3)
        for i in range(randint(0, self.count_params)):
            result += self.gen_type()
            result += self.gen_name()
            if i+1 < self.count_params:
                result += choice([self.gen_helpers(), ',', ',', ','])
        return result


    def generate_str(self):
        result =  self.gen_type()
        result += self.gen_name()
        result += choice([self.gen_helpers(), '(', '(', '(', '(', '(', '('])
        result += self.gen_params()
        result += choice([self.gen_helpers(), ')', ')', ')', ')', ')', ')'])
        result += ';'
        return result


    def generate_list(self, n):
        list = []
        for i in range(n):
            list.append(self.generate_str())
        return list

if __name__ == '__main__':
    g = Generator()
    for i in range(20):
        g.generate_str()