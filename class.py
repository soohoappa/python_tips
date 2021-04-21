# creating a class

class Dog():
    def __init__(self, name):
        self.name = name
    def sit(self):
        print(f"{self.name} is sitting")
    
my_dog = Dog("Teddy")

print(f"{my_dog.name} is a great dog!")

my_dog.sit()

# creating a inheritance
class SARDog(Dog):
    def __init__(self, name):
        super().__init__(name)

    def search(self):
        print(f"{self.name} is searching.")

my_dog = SARDog("Willie")

print(f"{my_dog.name} is a search dog.")
my_dog.sit()
my_dog.search()