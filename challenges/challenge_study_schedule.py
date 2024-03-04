def study_schedule(permanence_period, target_time):
    if not target_time:
        return None

    if not all(
        isinstance(period[0], int) and isinstance(period[1], int)
        for period in permanence_period
    ):
        return None

    number_students = 0
    for time_period in permanence_period:
        if time_period[0] <= target_time <= time_period[1]:
            number_students += 1
    return number_students
