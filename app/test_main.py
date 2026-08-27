from app.main import get_human_age
import pytest

@pytest.mark.parametrize(
    "cat_age,dog_age,expected_in_human_age",
    [(0,0, [0, 0]),
     (14, 14, [0, 0]),
     (15, 15, [1, 1]),
     (23, 23, [1, 1]),
     (24, 24, [2, 2]),
     (27, 27, [2, 2]),
     (28, 28, [3, 2]),
     (100, 100, [21, 17]),
     (-1,-1, [0, 0]),
     (10_000, 10_000, [2496, 1997]),
    ],
    ids=[
        "zero_ages",
        "before first human year",
        "first human year",
        "before second human year",
        "second human year",
        "before cat third human year",
        "cat third human year dog second",
        "large ages from readme",
        "negative ages",
        "very large ages",
    ]
)
def test_get_human_age(cat_age: int, dog_age: int, expected_in_human_age: list) -> None:
    assert (
        get_human_age(cat_age, dog_age) == expected_in_human_age
    ), f"Expected result for {cat_age} and {dog_age} is {expected_in_human_age}"


@pytest.mark.parametrize(
    "cat_age,dog_age",
    [
        ("15", 15),
        (15, "15"),
        (15.5, 15),
        (15, 15.5),
    ],
    ids=[
        "cat_age_as_string",
        "dog_age_as_string",
        "cat_age_as_float",
        "dog_age_as_float",
    ],
)
def test_get_human_age_with_invalid_types(cat_age: int, dog_age: int):
    with pytest.raises(TypeError):
        get_human_age(cat_age, dog_age)
