from solution import *

import math

from solution import *

import math

from solution import *

import math

import pytest
from solution import generate_schedule, validate_schedules, view_schedule

def test_generate_schedule():
    students = [
        {'name': 'Alice', 'preferences': ['Math', 'Science', 'Literature'], 'available_slots': ['Monday 9AM', 'Monday 10AM', 'Tuesday 9AM']},
        {'name': 'Bob', 'preferences': ['Math', 'History'], 'available_slots': ['Monday 9AM', 'Friday 11AM']},
        {'name': 'Charlie', 'preferences': ['Science', 'Literature', 'History'], 'available_slots': ['Thursday 11AM', 'Tuesday 9AM', 'Friday 11AM']}
    ]
    
    schedules, alerts = generate_schedule(students)
    
    assert schedules['Alice'] == {'Math': 'Monday 9AM', 'Science': 'Monday 10AM', 'Literature': 'Tuesday 9AM'}
    assert alerts['Alice'] == []

    assert schedules['Bob'] == {'Math': 'Monday 9AM', 'History': 'Friday 11AM'}
    assert alerts['Bob'] == []

    assert schedules['Charlie'] == {'Science': 'Thursday 11AM', 'Literature': 'Tuesday 9AM', 'History': 'Friday 11AM'}
    assert alerts['Charlie'] == []
    
def test_generate_schedule_with_conflicts():
    students = [
        {'name': 'David', 'preferences': ['Math', 'Science'], 'available_slots': ['Monday 9AM', 'Monday 10AM']},
        {'name': 'Eve', 'preferences': ['Math', 'Science'], 'available_slots': ['Monday 10AM']},
        {'name': 'Frank', 'preferences': ['History', 'Literature'], 'available_slots': ['Friday 10AM', 'Friday 11AM']}
    ]
    
    schedules, alerts = generate_schedule(students)
    
    assert schedules['David'] == {'Math': 'Monday 9AM', 'Science': 'Monday 10AM'}
    assert alerts['David'] == []

    assert schedules['Eve'] == {'Science': 'Monday 10AM'}
    assert alerts['Eve'] == ['Math']
    
    assert schedules['Frank'] == {'Literature': 'Friday 10AM', 'History': 'Friday 11AM'}
    assert alerts['Frank'] == []

def test_validate_schedules():
    schedules = {
        'Alice': {'Math': 'Monday 9AM', 'Science': 'Monday 10AM', 'Literature': 'Tuesday 9AM'},
        'Bob': {'Math': 'Monday 9AM', 'History': 'Friday 11AM'},
        'Charlie': {'Science': 'Thursday 11AM', 'Literature': 'Tuesday 9AM', 'History': 'Friday 11AM'}
    }
    
    assert validate_schedules(schedules) == True

def test_view_schedule():
    students = [
        {'name': 'Alice', 'preferences': ['Math', 'Science', 'Literature'], 'available_slots': ['Monday 9AM', 'Monday 10AM', 'Tuesday 9AM']},
        {'name': 'Bob', 'preferences': ['Math', 'History'], 'available_slots': ['Monday 9AM', 'Friday 11AM']},
        {'name': 'Charlie', 'preferences': ['Science', 'Literature', 'History'], 'available_slots': ['Thursday 11AM', 'Tuesday 9AM', 'Friday 11AM']}
    ]
    
    schedules, alerts = generate_schedule(students)
    
    expected_output = "Schedule for Alice:\nMath: Monday 9AM\nScience: Monday 10AM\nLiterature: Tuesday 9AM\n"
    assert view_schedule('Alice', schedules, alerts) == expected_output
    
    expected_output = "Schedule for Bob:\nMath: Monday 9AM\nHistory: Friday 11AM\n"
    assert view_schedule('Bob', schedules, alerts) == expected_output
    
    expected_output = "Schedule for Charlie:\nScience: Thursday 11AM\nLiterature: Tuesday 9AM\nHistory: Friday 11AM\n"
    assert view_schedule('Charlie', schedules, alerts) == expected_output
    
    expected_output = "Schedule not found for student: Zach"
    assert view_schedule('Zach', schedules, alerts) == expected_output