from app.main import get_human_age


def test_should_return_zero_when_animal_age_less_than_15():
    assert get_human_age(14, 14) == [0, 0]


def test_should_return_correct_human_age():
    assert get_human_age(28, 28) == [3, 2]
