available_subject_time_slots = {
    'Math': ['Monday 9AM', 'Wednesday 10AM'],
    'Science': ['Monday 10AM', 'Thursday 11AM'],
    'Literature': ['Tuesday 9AM', 'Friday 10AM'],
    'History': ['Wednesday 9AM', 'Friday 11AM']
}

def generate_schedule(students):
    schedules = {}
    alerts = {}

    for student in students:
        name = student['name']
        preferences = student['preferences']
        available_slots = student['available_slots']
        student_schedule = {}
        student_alerts = []

        for subject in preferences:
            assigned = False
            for slot in available_subject_time_slots.get(subject, []):
                if slot in available_slots and slot not in student_schedule.values():
                    student_schedule[subject] = slot
                    assigned = True
                    break
            if not assigned:
                student_alerts.append(subject)

        schedules[name] = student_schedule
        alerts[name] = student_alerts

    return schedules, alerts

def validate_schedules(schedules):
    for student, schedule in schedules.items():
        assigned_slots = list(schedule.values())
        if len(assigned_slots) != len(set(assigned_slots)):
            return False

        for subject, slot in schedule.items():
            if slot not in available_subject_time_slots[subject]:
                return False

    return True

def view_schedule(name, schedules, alerts):
    if name not in schedules:
        return f"Schedule not found for student: {name}"

    schedule = schedules[name]
    student_alerts = alerts[name]
    result = f"Schedule for {name}"

    for subject, slot in schedule.items():
        result += f"\n{subject}: {slot}"

    if student_alerts:
        result += "\nCould not schedule: " + ", ".join(student_alerts) + "\n"

    return result