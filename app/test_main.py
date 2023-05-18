import pytest

from app.main import get_human_age


@pytest.mark.parametrize("cat_age, dog_age, expected", [
    pytest.param(14, 14, [0, 0], id="should return zeroes if animal age < 15"),
    pytest.param(14, 15, [0, 1]),
    pytest.param(15, 10, [1, 0]),
    pytest.param(0, 0, [0, 0], id="should return zeroes if animal age = 0"),
    pytest.param(23, 23, [1, 1], id="should return list with 2 elements"),
    pytest.param(-20, 20.1, [0, 1], id="all attributes should be positive"),
    pytest.param(27, 28, [2, 2]),
    pytest.param(24, 24, [2, 2]),
    pytest.param(28, 29, [3, 3])
])
def test_return_human_age_correctly(cat_age, dog_age, expected):
    assert get_human_age(cat_age, dog_age) == expected


@pytest.mark.parametrize("cat_age, dog_age, expected_error", [
    pytest.param("20", 20.1, TypeError, id="all attributes should be integer")
])
def test_raise_correctly_errors(cat_age, dog_age, expected_error):
    with pytest.raises(expected_error):
        get_human_age(cat_age, dog_age)
