class Animal:
    def __init__(self):
        self.num_of_eyes=2

    def breathe(self):
        print("Animals inhale and exhale")

class Fish(Animal):
    def __init__(self):
        super().__init__()

    def swim(self):
        print("Can swim")

figo=Fish()
figo.swim()
figo.breathe()


