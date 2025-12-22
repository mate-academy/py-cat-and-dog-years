import pytest
from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age,dog_age,expected",
    [
        (0, 0, [0, 0]),
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (23, 23, [1, 1]),
        (24, 24, [2, 2]),
        (27, 27, [2, 2]),
        (28, 28, [3, 2]),
        (100, 100, [21, 17]),
    ]
)
def test_examples_from_task(cat_age, dog_age, expected):
    assert get_human_age(cat_age, dog_age) == expected


def test_cat_age_grows_every_4_years_after_24():
    assert get_human_age(28, 0)[0] == get_human_age(24, 0)[0] + 1
    assert get_human_age(32, 0)[0] == get_human_age(28, 0)[0] + 1


def test_dog_age_grows_every_5_years_after_24():
    assert get_human_age(0, 28)[1] == get_human_age(0, 24)[1]
    assert get_human_age(0, 29)[1] == get_human_age(0, 24)[1] + 1
    assert get_human_age(0, 34)[1] == get_human_age(0, 29)[1] + 1


def test_cat_and_dog_are_calculated_independently():
    assert get_human_age(28, 10)[1] == get_human_age(24, 10)[1]
    assert get_human_age(10, 30)[0] == get_human_age(10, 24)[0]


def test_negative_values_raise_error():
    with pytest.raises(ValueError):
        get_human_age(-1, 0)

    with pytest.raises(ValueError):
        get_human_age(0, -5)


def test_invalid_types_raise_error():
    with pytest.raises(TypeError):
        get_human_age("10", 5)

    with pytest.raises(TypeError):
        get_human_age(10, "5")