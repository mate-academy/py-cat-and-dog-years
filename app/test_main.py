import pytest
from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, result",
    [
        # Values for tests
        (20, 7, [1, 0]),
        (15.1, 15.1, [1, 1]),
        (24, 24, [2, 2]),
        (27, 28, [2, 2]),
        (28, 29, [3, 3]),
        (31, 33, [3, 3]),
        (32, 34, [4, 4]),
        (0, -1, [0, 0])
    ],
    ids=[
        "Age cat/dog is 20/7",
        "Age cat/dog is 15.1(float type)",
        "Age cat/dog is 24",
        "Age cat/dog is 27/28",
        "Age cat/dog is 28/29",
        "Age cat/dog is 31/33",
        "Age cat/dog is 32/34",
        "Age cat is Zero, age dog is negative value"
    ]
)
def test_get_human_age_valid_cases(cat_age: int,
                                   dog_age: int,
                                   result: int) -> None:
    assert get_human_age(cat_age, dog_age) == result


def test_get_human_age_with_string_type_raises_error() -> None:
    with pytest.raises(TypeError):
        get_human_age(7, "12")
