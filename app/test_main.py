import pytest
from app.main import get_human_age


@pytest.mark.parametrize("cat_age, dog_age, expected_output", [
    (0, 0, [0, 0]),
    (14, 14, [0, 0]),
    (15, 15, [1, 1]),
    (23, 23, [1, 1]),
    (24, 24, [2, 2]),
    (27, 27, [2, 2]),
    (28, 28, [3, 2]),
    (100, 100, [21, 17]),
])
def test_get_human_age(cat_age, dog_age, expected_output):
    actual_output = get_human_age(cat_age, dog_age)
    assert actual_output == expected_output


def test_get_human_age_with_negative_cat_age():
    actual_output = get_human_age(-1, 0)
    assert actual_output == [0, 0]


def test_get_human_age_with_zero_cat_age():
    actual_output = get_human_age(0, 0)
    assert actual_output == [0, 0]


def test_get_human_age_with_string_cat_age():
    with pytest.raises(TypeError):
        get_human_age("15", 0)
