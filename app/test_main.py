import pytest
from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, expected",
    [
        (0, 0, [0, 0]),           # both under first threshold
        (14, 14, [0, 0]),         # just below first human year
        (15, 15, [1, 1]),         # exactly first threshold
        (23, 23, [1, 1]),         # just below second human year
        (24, 24, [2, 2]),         # exactly second threshold
        (27, 27, [2, 2]),         # just below third increment
        (28, 28, [3, 2]),         # cat gets third human year
        (100, 100, [21, 17]),     # large values
    ]
)
def test_get_human_age_typical_cases(cat_age: int,
                                     dog_age: int, expected: list) -> None:
    assert get_human_age(cat_age, dog_age) == expected


@pytest.mark.parametrize(
    "cat_age, dog_age",
    [
        (-1, 10),
        (10, -1),
        (-5, -5),
    ]
)
def test_get_human_age_negative_values(cat_age: int, dog_age: int) -> None:
    assert get_human_age(cat_age, dog_age) == [0, 0]


@pytest.mark.parametrize(
    "cat_age, dog_age",
    [
        (1e6, 1e6),          # very large floats
        ("10", "10"),       # strings
        (None, None),       # None
        ([], {}),           # wrong types
        (True, False),      # booleans
    ]
)
def test_get_human_age_invalid_types(cat_age: int, dog_age: int) -> None:
    with pytest.raises(TypeError):
        get_human_age(cat_age, dog_age)
