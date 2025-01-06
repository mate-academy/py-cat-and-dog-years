import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "age_cat,age_dog,result",
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
def test_should_be_correct(age_cat, age_dog, result) -> None:
    assert get_human_age(age_cat, age_dog) == result