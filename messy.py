"""Readable version of the Lecture 6 student report program."""

SUBJECT_COUNT = 3
students = [
    ["Rahul", 78, 88, 92],
    ["Priya", 65, 71, 69],
    ["Amit", 90, 94, 85],
    ["Sneha", 55, 60, 58],
    ["Vikram", 82, 79, 88],
]


def calculate_total(student):
    """Return the total of one student's subject marks."""
    return sum(student[1:])


def calculate_average(total):
    """Return a student's average from their total marks."""
    return total / SUBJECT_COUNT


def grade_for(average):
    """Return the letter grade for an average mark."""
    if average >= 90:
        return "A"
    if average >= 80:
        return "B"
    if average >= 70:
        return "C"
    if average >= 60:
        return "D"
    return "F"


def count_above_class_average(records):
    """Return how many students score above the class average."""
    averages = [calculate_average(calculate_total(student)) for student in records]
    class_average = sum(averages) / len(averages)
    return sum(average > class_average for average in averages)


print("REPORT")
averages = []
for student in students:
    total = calculate_total(student)
    average = calculate_average(total)
    averages.append(average)
    print(f"{student[0]}{total}{average}{grade_for(average)}")

class_average = sum(averages) / len(averages)
print(f"Class average:{class_average}")

topper_index = max(range(len(students)), key=averages.__getitem__)
print(f"Topper:{students[topper_index][0]}{averages[topper_index]}")
