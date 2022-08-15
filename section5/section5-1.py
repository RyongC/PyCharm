# encapsulation-2.py

# This example builds on top of `encapsulation-1.py`.
# Here we see how we can set values in methods without
# going through the method itself, ie.. how we can break
# encapsulation.
# https://github.com/arvimal/Python-and-OOP/blob/master/02-encapsulation-2.py

# NOTE: BREAKING ENCAPSULATION IS BAD.


class MyClassParent(object):
    def __init__(self):
        pass

    def set_val(self, val):
        self.value = val

    def get_val(self):
        print(self.value)

    def print_test(self, i=10):
        print(i)
        print(i)
        print(i)


class MyClass(MyClassParent):
    pass


a = MyClass()
b = MyClass()

a.set_val(10)
b.set_val(1000)
a.value = 100    # <== Overriding `set_value` directly
# <== ie..  Breaking encapsulation

a.get_val()
b.get_val()
a.print_test()