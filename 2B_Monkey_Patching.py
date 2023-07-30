class Omnicreate:

    def __init__(self, val1, val2):

        self.val1 = val1
        self.val2 = val2

    def addition_to_min(self):

        return self.val1 + self.val2



def add_to_declate(self):

    return self.val1 - self.val2


create = Omnicreate(2, 5)

print(create.addition_to_min())

Omnicreate.addition_to_min = add_to_declate

print(create.addition_to_min())

