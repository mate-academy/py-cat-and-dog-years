import pytest
from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, expected",
    [
        (0, 0, [0, 0]),
        (14, 14, [0, 0]),
        (23, 23, [2, 2]),
        (29, 29, [3, 2]),
        (1111, 1111, [246, 197]),
        (-1, -1, [0, 0]),
    ],
    ids=["Both ages are zero",
         "Both ages are less than the first_year",
         "Both ages are greater than the second_year",
         "Different ages between dogs and cats"
         "Dog age greater than cat age",
         "Large numbers", "Negative ages"]
)
def test_get_human_age(cat_age: int,
                       dog_age: int,
                       expected: list) -> None:
    assert get_human_age(cat_age, dog_age) == expected


def test_get_human_age_type_error() -> None:
    with pytest.raises(TypeError):
        get_human_age("cat", "dog")
