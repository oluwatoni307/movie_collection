print("Pick an option")

movies = []

def selection():
    menu = ["A. Add Movie", "B. List Movies", "C. Search for Movie"]

    for option in menu:
        print(option)

def add():
    name = input("Name of the movie: ")
    director = input("Who is the director of the movie: ")
    rating = input("What is the rating of the movie: ")
    movie = {
        "name": name,
        "director": director,
        "rating": rating
    }
    movies.append(movie)
    print("Movie added successfully:", movie)


def list1():
    for movie in movies:
        print(movie["name"])
    return

def search(name):
    for movie in movies:
        if movie["name"] == name:
            for key, value in movie.items():
                print(key, "->", value)

while True:
    selection()
    choice = input("What is your choice: ")
    choice1 = choice.upper()
    if choice1 == "A":
        add()
    elif choice1 == "B":
        list1()
    elif choice1 == "C":
        name = input("Name of movie: ")
        search(name)
    elif choice1 == "Q":
        print("Thank you for visiting our movie stand")
        break
    else:
        print("Invalid choice. Please try again.")
