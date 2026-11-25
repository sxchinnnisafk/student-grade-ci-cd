# grade_calculator.py

def _validate_marks(marks):
    """Validate that marks is a non-empty list/tuple of numbers between 0 and 100."""
    if not marks or not isinstance(marks, (list, tuple)):
        raise ValueError("Marks must be a non-empty list of numeric scores.")
    for m in marks:
        if isinstance(m, bool) or not isinstance(m, (int, float)) or m < 0 or m > 100:
            raise ValueError(f"Invalid mark: {m}. Each mark must be between 0 and 100.")


def average(marks):
    """Return the arithmetic average of a list of subject marks rounded to 2 decimals."""
    _validate_marks(marks)
    return round(sum(marks) / len(marks), 2)


def grade(avg):
    """Return the letter grade corresponding to an average score (0-100)."""
    if isinstance(avg, bool) or not isinstance(avg, (int, float)) or avg < 0 or avg > 100:
        raise ValueError(f"Invalid average: {avg}. Must be between 0 and 100.")
    if avg >= 90:
        return "A+"
    elif avg >= 80:
        return "A"
    elif avg >= 70:
        return "B"
    elif avg >= 60:
        return "C"
    elif avg >= 50:
        return "D"
    else:
        return "F"


def is_pass(marks, pass_mark=40):
    """Return True if all subject marks meet or exceed pass_mark, False otherwise."""
    _validate_marks(marks)
    return all(m >= pass_mark for m in marks)


if __name__ == "__main__":
    student_a = [88, 92, 85, 90, 95]
    student_b = [72, 65, 38, 80, 74]

    avg_a = average(student_a)
    print(f"Student A Marks: {student_a}")
    print(f"  Average: {avg_a} | Grade: {grade(avg_a)} | Passed: {is_pass(student_a)}")
def highest_mark(marks):
    """Return the highest individual mark from a non-empty list of marks."""
    _validate_marks(marks)
    return max(marks)
