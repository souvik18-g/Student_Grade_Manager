# Project Grade Manager

A simple command-line Student Grade Manager built with Python. It allows users to manage student names and marks, calculate average marks, and save/load student records using a CSV file.

## Features

* Add student records
* View all students
* Search for a student by name
* Delete a student
* Calculate average marks
* Save student records to a CSV file
* Load student records from a CSV file

## Technologies Used

* Python
* CSV

## Project Structure

```text id="m2u1qf"
Project Grade Manager/
│
├── project.py
├── test_project.py
└── data.csv
```

* **`project.py`** — Main application containing the student management functions.
* **`test_project.py`** — Test file for the project.
* **`data.csv`** — Stores student names and marks.

## How to Run

Make sure Python 3.x is installed.

Run the application:

```bash id="q3qj2k"
python project.py
```

The application provides a menu:

```text id="z7y6gk"
1 add
2 view
3 search
4 delete
5 avg
6 save
7 load
8 exit
```

Enter the number of the operation you want to perform.

## Testing

If `test_project.py` uses Pytest, run:

```bash id="2q0j1a"
pytest test_project.py
```

## Concepts Practiced

* Python functions
* Lists and dictionaries
* Loops and conditional statements
* Exception handling
* File handling
* CSV handling
* Command-line applications
* Basic testing
* Git and GitHub

## Future Improvements

* Add unique student IDs
* Validate marks within a valid range
* Prevent duplicate student records
* Improve error handling
* Add more comprehensive tests
