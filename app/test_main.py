import pytest
from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, result",
    [
        # Task Tests
        (14, 14, [0, 0]),
        (15.1, 15.1, [1, 1]),
        (23, 23, [1, 1]),
        (24, 24, [2, 2]),
        (27, 28, [2, 2]),
        (28, 29, [3, 3]),
        # My tests
        (20, 7, [1, 0]),
        (24, 15, [2, 1]),
        (0, -1, [0, 0]),

    ],
    ids=[
        "Age cat/dog is 14",
        "Age cat/dog is 15.1",
        "Age cat/dog is 23",
        "Age cat/dog is 24",
        "Age cat is 27, dog is 28",
        "Age cat is 28, dog is 29",
        "Default age",
        "Ages is transitional value",
        "Age cat is zero and age dog is transitional value",
    ]
)
def test_get_human_age_valid_cases(cat_age: int,
                                   dog_age: int,
                                   result: int) -> None:
    assert get_human_age(cat_age, dog_age) == result


def test_get_human_age_with_string_type_raises_error() -> None:
    with pytest.raises(TypeError):
        get_human_age(7, "12")
