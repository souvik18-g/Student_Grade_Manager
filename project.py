import csv

FILENAME = "data.csv"
# TODO: maybe add student IDs later so duplicate names dont clash


def main():
    students = []
    while True:
        print("1 add")
        print('2 view')
        print("3 search")
        print('4 delete')
        print("5 avg")
        print("6 save")
        print("7 load")
        print("8 exit")

        choice = input("enter your choice: ")

        if choice == "1":
            name = input("enter name: ")
            marks = input('enter marks: ')
            student = add_student(students, name, marks)
            if student:
                print("student added succesfully!")
            else:
                print("invalid marks")

        elif choice == "2":
            view_students(students)

        elif choice=="3":
            name = input("enter name to search: ")
            search_student(students, name)

        elif choice == "4":
            name = input("delete name: ")
            students = delete_student(students, name)
            print("deleted")

        elif choice == "5":
            avg = calculate_average(students)
            if avg == None:
                print("no data")
            else:
                print("avg:", avg)

        elif choice == "6":
            save_students(students)

        elif choice == "7":
            students = load_students()

        elif choice == "8":
            break

        else:
            print("Invalid choice")


def add_student(students, name, marks):

    try:
        marks = int(marks)
    except:
        return None

    student = {"name": name, "marks": marks}
    students.append(student)
    return student


def view_students(students):
    if len(students) == 0:
        print("no student found")
        return
    for s in students:
        print(s["name"], "-", s["marks"])


def search_student(students, name):
    for s in students:
        if s["name"] == name:
            print("found:", s["name"], s["marks"])
            return True
    print("Not found")
    return False


def delete_student(students, name):
    new_list = []
    for s in students:
        if s["name"] != name:
            new_list.append(s)
    return new_list


def calculate_average(students):
    if len(students) == 0:
        return None
    total = 0
    for s in students:
        total = total + s["marks"]
    avg = total / len(students)
    return round(avg, 2)


def save_students(students, filename=FILENAME):
    f = open(filename, "w", newline="")
    writer = csv.writer(f)
    for s in students:
        writer.writerow([s["name"], s["marks"]])
    f.close()
    print("Saved!")


def load_students(filename=FILENAME):
    try:
        f = open(filename, "r")
        reader = csv.reader(f)
        loaded = []
        for row in reader:
            loaded.append({"name": row[0], "marks": int(row[1])})
        f.close()
        print("Loaded!")
        return loaded
    except FileNotFoundError:
        print("No file found")
        return []


if __name__ == "__main__":
    main()