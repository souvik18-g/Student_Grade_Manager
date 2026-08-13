import os
import pytest
from project import add_student, delete_student, calculate_average, save_students, load_students

TEST_FILE = 'test_data.csv'

@pytest.fixture(autouse=True)
def cleanup():
    if os.path.isfile(TEST_FILE):
        os.remove(TEST_FILE)
    yield
    if os.path.isfile(TEST_FILE):
        os.remove(TEST_FILE)

def test_add_student():
    students = []
    result = add_student(students, "Rahul", "85")
    assert result == {"name": "Rahul", "marks": 85}
    assert students == [{"name": "Rahul", "marks": 85}]
    bad = add_student(students, "Priya", "asdf")
    assert bad == None
    assert len(students) == 1

def test_delete_student():
    students = [
        {"name": "Rahul", "marks": 85},
        {"name": "Priya", "marks": 90}
    ]
    result = delete_student(students, "Rahul")
    assert result == [{"name": "Priya", "marks": 90}]
    result2 = delete_student(result, "Nobody")
    assert result2 == [{"name": "Priya", "marks": 90}]


def test_calculate_average():
    assert calculate_average([]) == None
    students = [{"name": "Rahul", "marks": 80}, {"name": "Priya", "marks": 90}, {"name": "Amit", "marks": 100}]
    assert calculate_average(students) == 90.0


def test_save_and_load_students():
    students = [{"name": "Rahul", "marks": 85}, {"name": "Priya", "marks": 90}]
    save_students(students, filename=TEST_FILE)
    loaded = load_students(filename=TEST_FILE)
    assert loaded == students