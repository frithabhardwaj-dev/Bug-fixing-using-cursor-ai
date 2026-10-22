"""Student mark utilities, corrected after the RED test stage."""

PASS_MARK = 40
DISTINCTION_MARK = 90
FIRST_MARK = 60
SECOND_MARK = 45

def calculate_average(marks):
    """Return the arithmetic average of the supplied marks."""
    return sum(marks) / len(marks)

def is_passing(mark):
    """Return whether a mark meets the passing boundary."""
    return mark >= PASS_MARK

def get_grade(average):
    """Return the grade label for an average mark."""
    if average >= DISTINCTION_MARK:
        return "Distinction"
    if average >= FIRST_MARK:
        return "First"
    if average >= SECOND_MARK:
        return "Second"
    return "Fail"
