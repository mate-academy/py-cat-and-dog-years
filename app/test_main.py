import pytest
from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_years, dog_years, expected",
    [
        (0, 0, [0, 0]),
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (23, 23, [1, 1]),
        (24, 24, [2, 2]),
        (27, 27, [2, 2]),
        (28, 28, [3, 2]),
        (29, 29, [3, 3]),
        (100, 100, [21, 17]),
    ],
)
def test_valid_cases(cat_years: int,
                     dog_years: int,
                     expected: list[int]
                     ) -> None:
    assert get_human_age(cat_years, dog_years) == expected


@pytest.mark.parametrize("cat_years, dog_years", [
    (-1, 10),
    (10, -1),
    (-5, -5),
])
def test_negative_values_raise_error(cat_years: int, dog_years: int) -> None:
    with pytest.raises(ValueError):
        get_human_age(cat_years, dog_years)


@pytest.mark.parametrize("cat_years, dog_years", [
    ("10", 10),
    (10, "10"),
    ("a", "b"),
    (None, 5),
    (5, None),
])
def test_invalid_type_inputs_raise_error(cat_years: object,
                                         dog_years: object
                                         ) -> None:
    with pytest.raises(TypeError):
        get_human_age(cat_years, dog_years)
