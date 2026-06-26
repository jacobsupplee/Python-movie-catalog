"""
Name: Jacob Supplee
Date: 06/26/2026
Project Title: Movie Recommendation System
Project Description: This program allows the user to create and display a movie recommendation system. The user has
three abilities; insert a movie to the list, display the current list, or exit the program.
"""

#Initialize the movie list and menu option input
movieList = []
userInput = 0

print("Welcome to JacobFlix!")

while userInput != 3:
    print("---Menu---")
    print("1. Add movie to list")
    print("2. Display movie list")
    print("3. Exit program")

    userInput = int(input("Enter value 1, 2, or 3: "))

    if userInput == 3:
        print("Thank you for using JacobFlix!")
        print("Exiting Program...")

