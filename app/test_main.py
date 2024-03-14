import pytest
from app.main import get_human_age


@pytest.mark.parametrize("cat_age, dog_age, expected_result", [
    (0, 0, [0, 0]),
    (14, 14, [0, 0]),
    (15, 15, [1, 1]),
    (23, 23, [1, 1]),
    (24, 24, [2, 2]),
    (27, 27, [2, 2]),
    (28, 28, [3, 2]),
    (100, 100, [21, 17]),
    (-5, 10, [0, 0]),
    (5, -10, [0, 0]),
    (-5, -10, [0, 0]),

])
def test_get_human_age(cat_age: int,
                       dog_age: int,
                       expected_result: list) -> None:
    assert get_human_age(cat_age, dog_age) == expected_result


@pytest.mark.parametrize("age_in_human_years, age_in_dog_years", [
    ("5", 10),
    (5, "10"),
    ("5", "10")
])
def test_get_human_age_raises_type_error(
        age_in_human_years: int,
        age_in_dog_years: int
) -> None:
    with pytest.raises(TypeError):
        get_human_age("5", "10")
