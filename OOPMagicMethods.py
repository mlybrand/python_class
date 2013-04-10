class Thing():

    population = 0
    
    def __init__(self, name):
        self.name = name
        Thing.population += 1
        print("I am being created.")

    def __del__(self):
        Thing.population -= 1
        print("I am being destroyed.")

    def __str__(self):
        return "Say my name! It is {0}.".format(self.name)

    def __gt__(self, other):
        return len(self.name) > len(other.name)

    def say_my_name(self):
        print("My name is {0}.".format(self.name))

    @staticmethod
    def say_how_many_things():
        print("There are {0} things around.".format(Thing.population))


if __name__ == "__main__":
    cousin_itt = Thing("Cousin Itt")
    alf = Thing("Alf")

    del cousin_itt

    print("My script is ending...")

    
