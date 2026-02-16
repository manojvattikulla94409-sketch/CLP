def average_passing_grades(grades: list[int]) -> float:

    total = 0
    count = 0

    # Iterating through grades
    for grade in grades:
        if grade >= 50:
            total += grade
            count += 1

    # If no passing grades, return 0.0
    if count == 0:
        return 0.0

    # Return average as float
    return total / count
#Team name-{CLP}
