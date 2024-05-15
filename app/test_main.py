from app.main import get_human_age
import pytest


@pytest.mark.parametrize("cat_age, dog_age, expected", [
    (14, 12, [0, 0]),  # Testing when both animals are less than the first year
    (15, 23, [1, 1]),  # Testing when both animals are one year old
    (28, 28, [3, 2]),  # Testing when both animals are two years old
])
def test_get_human_age(cat_age: int, dog_age: int, expected: int) -> None:
    assert get_human_age(cat_age, dog_age) == expected


@pytest.mark.parametrize("cat_age, dog_age, expected_error", [
    ("5", 5, TypeError),  # Testing cat_age as string
    (5, "5", TypeError),  # Testing dog_age as string
])
def test_error_key_value(cat_age: int, dog_age: int, expected_error) -> None:
    with pytest.raises(expected_error):
        get_human_age(cat_age, dog_age)
