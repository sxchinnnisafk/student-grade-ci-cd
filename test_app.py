# test_grade_calculator.py
import pytest
from StudentCalculator import average, grade, is_pass, highest_mark

def test_average_standard():
    assert average([80, 90, 100]) == 90.0
    assert average([75, 82, 91]) == 82.67


def test_average_single_subject():
    assert average([64]) == 64.0


def test_grade_top_tiers():
    assert grade(95) == "A+"
    assert grade(90) == "A+"
    assert grade(84) == "A"
    assert grade(80) == "A"


def test_grade_mid_and_fail_tiers():
    assert grade(75) == "B"
    assert grade(62) == "C"
    assert grade(50) == "D"
    assert grade(49.9) == "F"


def test_is_pass_all_subjects_above_threshold():
    assert is_pass([40, 55, 78, 90]) is True


def test_is_pass_fails_if_one_subject_below_threshold():
    # Average is 76.25, but one subject is below 40 -> must return False
    assert is_pass([90, 88, 88, 39]) is False


def test_highest_mark():
    assert highest_mark([67, 94, 81, 73]) == 94


def test_invalid_inputs_raise_value_error():
    with pytest.raises(ValueError):
        average([])
    with pytest.raises(ValueError):
        is_pass([85, 105])
    with pytest.raises(ValueError):
        grade(-5)
