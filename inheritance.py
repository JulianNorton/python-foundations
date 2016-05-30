class Parent(object):
    def __init__(self, last_name, fur_length):
        print('parent constructor called')
        self.last_name = last_name
        self.fur_length = fur_length

papa_bear = Parent("papa", "long")

print(papa_bear.last_name)