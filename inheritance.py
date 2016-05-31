class Parent():
    def __init__(self, first_name, fur_length):
        print('parent constructor called')
        self.first_name = first_name
        self.fur_length = fur_length

    def show_info(self):
        print('First name - ' + self.first_name)
        print('Fur length - ' + self.fur_length)
        print('\n')


class Child(Parent):
    def __init__(self, first_name, fur_length, favorite_snack):
        print('child constructor called')
        Parent.__init__(self, first_name, fur_length)
        self.favorite_snack = favorite_snack

    def show_info(self):
        print('First name - ' + self.first_name)
        print('Fur length - ' + self.fur_length)
        print('Favorite snack - ' + self.favorite_snack)
        print('\n')

papa_bear = Parent("papa", "long")
boop_bear = Child("boop", "short", "humans")

papa_bear.show_info()
boop_bear.show_info()
