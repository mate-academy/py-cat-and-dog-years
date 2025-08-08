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
        (27, 27, [2, 2]),
        (28, 28, [3, 2]),
        (100, 100, [21, 17])
    ]
)
def test_get_human_ages_for_cat_and_dog(cat_age, dog_age, result):
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
