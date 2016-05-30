class Parent():
    def __init__(self, first_name, fur_length):
        print('parent constructor called')
        self.first_name = first_name
        self.fur_length = fur_length
        
    def show_info(self):
        print('First name - ' + self.first_name)
        print('Eye color - ' + self.fur_length)


class Child(Parent):
    def __init__(self, first_name, fur_length, favorite_snack):
        print('child constructor called')
        Parent.__init__(self, first_name, fur_length)
        self.favorite_snack = favorite_snack

papa_bear = Parent("papa", "long")
boop_bear = Child("boop", "short", "humans")

papa_bear.show_info()
