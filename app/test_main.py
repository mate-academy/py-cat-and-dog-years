import pytest
from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, result",
    [
        # Values for tests
        (20, 7, [1, 0]),
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (20, 20, [1, 1]),
        (24, 24, [2, 2]),
        (27, 28, [2, 2]),
        (28, 29, [3, 3]),
        (31, 33, [3, 3]),
        (32, 34, [4, 4])
    ],
    ids=[
        "Age cat/dog is 20/7",
        "Age cat/dog is 14/14",
        "Age cat/dog is 15/15",
        "Age cat/dog is 20/20",
        "Age cat/dog is 24/24",
        "Age cat/dog is 27/28",
        "Age cat/dog is 28/29",
        "Age cat/dog is 31/33",
        "Age cat/dog is 32/34"
    ]
)
def test_get_human_age_valid_cases(cat_age: int,
                                   dog_age: int,
                                   result: int) -> None:
    assert get_human_age(cat_age, dog_age) == result


def test_get_human_age_with_string_type_raises_error() -> None:
    with pytest.raises(TypeError):
        get_human_age(7, "12")
