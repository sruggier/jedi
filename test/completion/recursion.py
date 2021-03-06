"""
Code that might cause recursion issues (or has caused in the past).
"""

def Recursion():
    def recurse(self):
        self.a = self.a
        self.b = self.b.recurse()

#?
Recursion().a

#?
Recursion().b


class X():
    def __init__(self):
        self.recursive = [1, 3]

    def annoying(self):
        self.recursive = [self.recursive[0]]

    def recurse(self):
        self.recursive = [self.recursive[1]]

#? int()
X().recursive[0]


def to_list(iterable):
    return list(set(iterable))


def recursion1(foo):
    return to_list(to_list(foo)) + recursion1(foo)

#? int()
recursion1([1,2])[0]


class FooListComp():
    def __init__(self):
        self.recursive = [1]

    def annoying(self):
        self.recursive = [x for x in self.recursive]


#? int()
FooListComp().recursive[0]
