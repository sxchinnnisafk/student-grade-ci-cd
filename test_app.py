def calculate_average(marks):
    if len(marks) != 3 or any(m < 0 or m > 100 for m in marks):
        raise ValueError("Enter exactly three marks from 0 to 100")
    return sum(marks) / 3


def calculate_grade(average):
    if average < 0 or average > 100:
        raise ValueError("Average must be between 0 and 100")
    if average >= 90:
        return "S"
    if average >= 80:
        return "A"
    if average >= 65:
        return "B"
    if average >= 50:
        return "C"
    if average >= 40:
        return "D"
    return "F"