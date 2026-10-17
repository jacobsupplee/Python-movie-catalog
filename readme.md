# Python Movie Catalog

A small Python program for keeping track of movie titles from the command line. You can add movies, view the list, and catch duplicate entries instead of adding the same title twice.

## Features

- Add movie titles to the collection
- View the movies in a numbered list
- Check for duplicate titles
- Handle invalid menu choices and non-numeric input
- Keep title formatting consistent

## Built with

- Python 3
- Lists and loops
- Input validation
- Exception handling

## Running it

Make sure Python 3 is installed, then run this from the project directory:

```bash
python movieRecommendations.py
```

No extra packages are needed.

## A few things to know

The movie list only exists while the program is running, so it resets when you close it. Despite the original filename, this version is a movie catalog, not a recommendation system. It doesn't currently recommend movies based on genres, ratings, or preferences.

## What I practiced

This project gave me practice with Python collections, control flow, validating user input, and building a simple menu-driven program. A logical next step would be saving the collection to a file so the list is still there the next time the program runs.
