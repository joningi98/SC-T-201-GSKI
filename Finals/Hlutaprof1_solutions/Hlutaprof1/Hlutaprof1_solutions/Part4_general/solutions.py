
#BOOK / LIBRARY

class Book:
    def __init__(self, ISBN="", name="", page_count=0):
        self.ISBN = ISBN
        self.name = name
        self.page_count = page_count

    def set_isbn(self, ISBN):
        self.ISBN = ISBN

    def set_name(self, name):
        self.name = name

    def set_page_count(self, page_count):
        self.page_count = page_count

    def get_isbn(self):
        return self.ISBN

    def get_name(self):
        return self.name

    def get_page_count(self):
        return self.page_count

    def __str__(self):
        return (str(self.ISBN) + ": " + str(self.name)
            + ", " + str(self.page_count) + " pages")

class Library:
    def __init__(self):
        self.books = []
    
    def add_book(self, ISBN, name, page_count):
        book = self.get_book(ISBN)
        if book == None:
            self.books.append(Book(ISBN, name, page_count))
        else:
            self.change_name(ISBN, name)
            self.change_page_count(ISBN, page_count)
    
    def get_book(self, ISBN):
        for book in self.books:
            if book.get_isbn() == ISBN:
                return book
        return None

    def change_name(self, ISBN, new_name):
        book = self.get_book(ISBN)
        if book != None:
            book.set_name(new_name)

    def change_page_count(self, ISBN, count):
        book = self.get_book(ISBN)
        if book != None:
            book.set_page_count(count)

    def __str__(self):
        st = ""
        for book in self.books:
            st += str(book) + "\n"
        return st



#CAR / RENTAL

class Car:
    def __init__(self, plate_nr="", brand="", passenger_count=0):
        self.plate_nr = plate_nr
        self.brand = brand
        self.passenger_count = passenger_count

    def set_plate_nr(self, plate_nr):
        self.plate_nr = plate_nr

    def set_brand(self, brand):
        self.brand = brand

    def set_passenger_count(self, passenger_count):
        self.passenger_count = passenger_count

    def get_plate_nr(self):
        return self.plate_nr

    def get_brand(self):
        return self.brand

    def get_passenger_count(self):
        return self.passenger_count

    def __str__(self):
        return (str(self.plate_nr) + ": " + str(self.brand)
            + ", " + str(self.passenger_count) + " passengers")

class Rental:
    def __init__(self):
        self.cars = []
    
    def add_car(self, plate_nr, brand, passenger_count):
        car = self.get_car(plate_nr)
        if car == None:
            self.cars.append(Car(plate_nr, brand, passenger_count))
        else:
            self.change_brand(plate_nr, brand)
            self.change_passenger_count(plate_nr, passenger_count)
    
    def get_car(self, plate_nr):
        for car in self.cars:
            if car.get_plate_nr() == plate_nr:
                return car
        return None

    def change_brand(self, plate_nr, new_brand):
        car = self.get_car(plate_nr)
        if car != None:
            car.set_brand(new_brand)

    def change_passenger_count(self, plate_nr, count):
        car = self.get_car(plate_nr)
        if car != None:
            car.set_passenger_count(count)

    def __str__(self):
        st = ""
        for car in self.cars:
            st += str(car) + "\n"
        return st



#ANIMAL / ZOO

class Animal:
    def __init__(self, ID="", species="", page_count=0):
        self.ID = ID
        self.species = species
        self.weight = page_count

    def set_id(self, ID):
        self.ID = ID

    def set_species(self, species):
        self.species = species

    def set_weight(self, page_count):
        self.weight = page_count

    def get_id(self):
        return self.ID

    def get_species(self):
        return self.species

    def get_weight(self):
        return self.weight

    def __str__(self):
        return (str(self.ID) + ": " + str(self.species)
            + ", " + str(self.weight) + " kilograms")

class Zoo:
    def __init__(self):
        self.animals = []
    
    def add_animal(self, ID, species, weight):
        animal = self.get_animal(ID)
        if animal == None:
            self.animals.append(Animal(ID, species, weight))
        else:
            self.change_species(ID, species)
            self.change_weight(ID, weight)
    
    def get_animal(self, ID):
        for animal in self.animals:
            if animal.get_id() == ID:
                return animal
        return None

    def change_species(self, ID, new_species):
        animal = self.get_animal(ID)
        if animal != None:
            animal.set_species(new_species)

    def change_weight(self, ID, weight):
        animal = self.get_animal(ID)
        if animal != None:
            animal.set_weight(weight)

    def __str__(self):
        st = ""
        for animal in self.animals:
            st += str(animal) + "\n"
        return st

