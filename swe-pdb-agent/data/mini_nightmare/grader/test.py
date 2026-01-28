import pytest

from grader_code import GradeProcessor


@pytest.fixture
def test_data():
    # Test data with multiple classes, sections, and students
    return {
        'Math': {
            'Section1': [
                ('student1', 95.0),
                ('student2', 88.0),
                ('student3', 92.0)
            ],
            'Section2': [
                ('student4', 91.0),
                ('student5', 89.0)
            ]
        },
        'Physics': {
            'Section1': [
                ('student1', 89.0),  # Note: same student1 in different class
                ('student3', 94.0),
                ('student5', 93.0)
            ]
        }
    }


@pytest.fixture
def processor(test_data):
    return GradeProcessor(test_data)


def test_top_performers(processor):
    """
    When a student's score is incomplete, they should not be considered
    """
    # With threshold 90, we expect student3 only
    # (only student with all grades >= 90)
    top_students = processor.get_top_performers(threshold=90.0)
    
    # This is what we actually want
    assert set(top_students) == {'student3'}, "Should only return students with ALL grades above threshold"


def test_student_averages(processor):
    """
    Test the working get_student_averages() method for comparison
    """
    averages = processor.get_student_averages()
    
    # Test specific average calculations
    assert abs(averages['student1'] - 92.0) < 1e-9  # (95 + 89) / 2
    assert averages['student2'] == 88.0  # Single grade
    assert abs(averages['student3'] - 93.0) < 1e-9  # (92 + 94) / 2


def test_edge_cases():
    # Empty data
    empty_processor = GradeProcessor({})
    assert empty_processor.get_top_performers() == []
    
    # Single grade at exactly threshold
    threshold_data = {
        'Math': {
            'Section1': [('student1', 90.0)]
        }
    }
    threshold_processor = GradeProcessor(threshold_data)
    assert threshold_processor.get_top_performers(threshold=90.0) == ['student1']