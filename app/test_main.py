from app.main import get_human_age


def test_should_return_correct_age():
    age = get_human_age(28, 28)
    assert age == [3, 2]


def test_should_return_0_when_age_is_0():
    age = get_human_age(0, 17)
    assert age == [0, 1]


def test_should_return_correct_age_when_input_is_float():
    age = get_human_age(15.9, 0.7)
    assert age == [1, 0]
