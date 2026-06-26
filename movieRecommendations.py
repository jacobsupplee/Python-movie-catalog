"""
Name: Jacob Supplee
Date: 06/26/2026
Project Title: Movie Recommendation System
Project Description: This program allows the user to create and manage a movie recommendation list. The user can add
movies to the catalogue, display the current movie catalogue, or exit the program.
"""

#Initialize the movie list and menu option input
movieList = []
userInput = 0

print("Welcome to JacobFlix!")

while userInput != 3:
    print("\n---Menu---")
    print("Choose from the following options:")
    print("1. Add a movie to the catalogue")
    print("2. Display the movie catalogue")
    print("3. Exit program")

    #INPUT: Get user selection
    try:
        userInput = int(input("Enter value 1, 2, or 3: "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        continue

    #PROCESS: Add a new movie to the catalogue
    if userInput == 1:
        movieTitle = input("Enter the movie title: ").title()

        #PROCESS: Check for duplicate movie titles
        if movieTitle in movieList:
            print(f"The movie '{movieTitle}' is already in the catalogue.")
        else:
            movieList.append(movieTitle)
            print(f"The movie '{movieTitle}' was added to the catalogue.")

    #OUTPUT: Display the movie catalogue
    elif userInput == 2:

        #Check whether the catalogue contains any movies
        if len(movieList) == 0:
            print("The catalogue contains no movies. Please add at least one movie.")
        else:
            print("\n---Movie Catalogue---")

            for i, movie in enumerate(movieList, start=1):
                print(f"{i}. {movie}")

    #OUTPUT: Exit the program
    elif userInput == 3:
        print("Thank you for using JacobFlix!")
        print("Exiting program...")

    #OUTPUT: Handle invalid menu selections
    else:
        print("Invalid selection. Please enter 1, 2, or 3.")