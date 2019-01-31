class Animal:
    def __init__(self, animal_id="", species="", weight=0):
        self.id = animal_id
        self.species = species
        self.weight = weight

    def get_id(self):
        return self.id

    def get_species(self):
        return self.species

    def get_weight(self):
        return self.weight

    def set_id(self, new_id):
        self.id = new_id

    def set_species(self, new_species):
        self.species = new_species

    def set_weight(self, new_weight):
        self.weight = new_weight

    def __repr__(self):
        return "{}: {}, {} kilograms".format(self.id, self.species, self.weight)

    # Breytti í __repr__ virkaði betur að prenta í Zoo þannig


class Zoo:
    def __init__(self):
        self.zoo_dict = {}

    def add_animal(self, animal_id="", species="", weight=0):
        new_animal = Animal(animal_id, species, weight)
        self.zoo_dict[animal_id] = new_animal

    def get_animal(self, animal_id):
        if animal_id in self.zoo_dict.keys():
            return self.zoo_dict[animal_id]

    def change_species(self, animal_id, new_species):
        new_animal = Animal(animal_id, new_species, self.zoo_dict[animal_id].get_weight())
        self.zoo_dict[animal_id] = new_animal

    def change_weight(self, animal_id, new_weight):
        new_animal = Animal(animal_id, self.zoo_dict[animal_id].get_species, new_weight)
        self.zoo_dict[animal_id] = new_animal

    def __str__(self):
        my_str = ""
        for animal_id, info in self.zoo_dict.items():
            my_str += "{}: {}, {}\n".format(info.get_id(), info.get_species(), info.get_weight())
        return my_str


my_zoo = Zoo()

my_zoo.add_animal("12", "giraffe", 410)
my_zoo.add_animal("142", "giraffe", 410)
my_zoo.add_animal("15", "giraffe", 410)
my_zoo.add_animal("2", "giraffe", 410)
my_zoo.add_animal("155", "giraffe", 410)
my_zoo.add_animal("1556", "giraffe", 410)
animal = my_zoo.get_animal("12")
animal.set_species("elephant")
print(my_zoo)
