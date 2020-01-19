class animal(object):
    def __init__(self, number_of_legs, has_fur):
        self.number_of_legs = None
        self.has_fur = None

    def get_num_legs(self):
        return self.number_of_legs

class cat(animal):
    def __init__(self):
        self.number_of_legs = 4
        self.has_fur = True

class chicken(animal):
    def __init__(self):
        self.number_of_legs = 2
        self.has_fur = false

def func_animal(num_legs):
    def a(has_fur):
        return {
            'number_of_legs': num_legs,
            'has_fur': has_fur,
            'get_num_legs': lambda: num_legs,
        }
    return a

kitty = func_animal(4)(True)
print(kitty['number_of_legs'])
print(kitty['has_fur'])
print(kitty['get_num_legs']())
