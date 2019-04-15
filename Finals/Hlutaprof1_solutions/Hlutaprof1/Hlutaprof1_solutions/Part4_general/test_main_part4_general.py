import solutions
from solutions import *


if "Book" in dir(solutions):
    print("\n......... TESTING Book/Library .........\n")

    library = Library()
    library.add_book("12345", "bokin min 1", 100)
    library.add_book("2345", "bokin min 2", 110)
    library.add_book("6534", "bokin min 3", 102)
    library.add_book("8674", "bokin min 4", 300)
    library.add_book("1342345", "bokin min 5", 105)

    print(library)

    print("\n")
    book = library.get_book("6534")
    print(book)
    book.set_name("bokin min 77")
    print(book)
    book.set_page_count(3000)
    print(book)
    book.set_isbn("65345")
    print(book)
    print("\n")

    print(library)

    library.change_page_count("8674", 1000)

    print(library)

    library.change_name("8674", "bokin min 44")

    print(library)

    library.add_book("2345", "bokin min 101", 2002)

    print(library)

    library.add_book("2346", "bokin min 10101", 2002002)

    print(library)


if "Car" in dir(solutions):
    print("\n......... TESTING Car/Rental .........\n")

    rental = Rental()
    rental.add_car("MP323", "toyota", 5)
    rental.add_car("CF345", "subaru", 7)
    rental.add_car("OP123", "kia", 5)
    rental.add_car("UIO56", "fiat", 3)
    rental.add_car("SM456", "renault", 45)

    print(rental)

    print("\n")
    car = rental.get_car("OP123")
    print(car)
    car.set_brand("datsun")
    print(car)
    car.set_passenger_count(9)
    print(car)
    car.set_plate_nr("OP345")
    print(car)
    print("\n")

    print(rental)

    rental.change_passenger_count("UIO56", 4)

    print(rental)

    rental.change_brand("UIO56", "citroen")

    print(rental)

    rental.add_car("CF345", "mitsubishi", 8)

    print(rental)

    rental.add_car("CF346", "ssangyong", 12)

    print(rental)



if "Animal" in dir(solutions):
    print("\n......... TESTING Animal/Zoo .........\n")

    zoo = Zoo()
    zoo.add_animal("12345", "giraffe", 1500)
    zoo.add_animal("2345", "elephant", 6000)
    zoo.add_animal("6534", "lion", 300)
    zoo.add_animal("8674", "tiger", 400)
    zoo.add_animal("1342345", "bear", 500)

    print(zoo)

    print("\n")
    animal = zoo.get_animal("2345")
    print(animal)
    animal.set_species("hippopotomus")
    print(animal)
    animal.set_weight(4000)
    print(animal)
    animal.set_id("65345")
    print(animal)
    print("\n")

    print(zoo)

    zoo.change_weight("8674", 350)

    print(zoo)

    zoo.change_species("8674", "leopard")

    print(zoo)

    zoo.add_animal("6534", "hyena", 50)

    print(zoo)

    zoo.add_animal("6535", "gopher", 1.5)

    print(zoo)


# print("Example usage .......................................")

# library = Library()
# library.add_book("978-1-118-29027-9", "Data Structures in Python", 750)
# book = library.get_book("978-1-118-29027-9")
# book.set_name("Data Structures and Algorithms in Python")
# print(library)

# zoo = Zoo()
# zoo.add_animal("12", "giraffe", 410)
# animal = zoo.get_animal("12")
# animal.set_species("elephant")
# print(zoo)

# rental = Rental()
# rental.add_car("MFT67", "chrysler", 5)
# car = rental.get_car("MFT67")
# car.set_brand("fiat")
# print(rental)

