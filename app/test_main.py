from app.main import get_human_age
import pytest


@pytest.mark.parametrize(
    "cat_age, dog_age, result",
    [
        (0, 0, [0, 0]),
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (23, 23, [1, 1]),
        (24, 24, [2, 2]),
        (28, 28, [3, 2]),
        (28, 29, [3, 3]),
        (32, 32, [4, 3]),
        (100, 104, [21, 18])
    ]
)
def test_get_human_ages_for_cat_and_dog(cat_age, dog_age, result):
    assert get_human_age(cat_age, dog_age) == result


@pytest.mark.parametrize(
    "cat_age, dog_age, result",
    [
        (-7, -4, [0, 0]),
        (-10, 17, [0, 1]),
        (15, -15, [1, 0]),
        (-23, -23, [0, 0]),
    ]
)
def test_negative_cat_or_dog_ages(cat_age, dog_age, result):
    assert get_human_age(cat_age, dog_age) == result


@pytest.mark.parametrize(
    "cat_age, dog_age, exception",
    [
        ({0: None}, (15,), TypeError),
        ("14", [14], TypeError),
    ]
)
def test_expected_raises_if_ages_not_integers(cat_age, dog_age, exception):
    with pytest.raises(exception):
        get_human_age(cat_age, dog_age)
