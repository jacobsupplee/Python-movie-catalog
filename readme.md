# Movie Catalog CLI

A lightweight Python command-line application for maintaining a movie catalogue. Users can add titles, review the current collection, and receive feedback when input is invalid or a duplicate title is entered.

> **Project context:** Personal portfolio documentation for a learning project. This is an in-memory CLI application, not a deployed recommendation engine or persistent database.

## Capabilities

- Add movie titles to an in-session catalogue
- Display saved titles in a numbered list
- Detect duplicate entries
- Validate menu input and handle non-numeric selections
- Normalize title casing for more consistent presentation

## Technology

- Python 3
- Lists and iteration
- Input validation and exception handling
- Command-line interaction

## Run locally

1. Install Python 3.
2. Clone this repository.
3. From the project directory, run:

   ```bash
   python movieRecommendations.py
   ```

No third-party packages are required.

## Current limitations

- Catalogue entries are held in memory and reset when the program exits.
- This is a catalogue manager; it does not currently generate recommendations from ratings, genres, or user preferences.
- This is not an authentication-enabled or multi-user application.

## Potential next steps

- Persist catalogue data in JSON or SQLite
- Add search, removal, and sorting
- Add unit tests for duplicate detection and input validation
- Separate catalogue logic from CLI input/output

## Skills demonstrated

Python fundamentals, collections, control flow, defensive input handling, and designing a small interactive command-line workflow.