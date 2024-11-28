from app.main import get_human_age


def test_should_be_correct_visible_convert_to_human_age():
    result = get_human_age(15, 15)
    assert result == [1, 1]


def test_should_be_correct_convert_to_human_age_with_different_ages():
    result = get_human_age(15, 40)
    assert result == [1, 5]


def test_should_be_correct_convert_to_human_age_with_next_step_ages():
    result = get_human_age(25, 25)
    assert result == [2, 2]


def test_should_be_correct_convert_to_human_age_with_wrong_ages():
    result = get_human_age(-5, 40)
    assert result == [0, 5]
