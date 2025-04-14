from app.main import get_human_age
import pytest


@pytest.mark.parametrize("age_cat, age_dog, expected", [
    (14, 14, [0, 0]),
    (24, 24, [2, 2]),
    (28, 28, [3, 2])
])
def test_get_human_age(age_cat: int, age_dog: int, expected: list) -> None:
    assert get_human_age(age_cat, age_dog) == expected
