import pytest
from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, expected",
    [
        (0, 0, [0, 0]),
        (14, 14, [0, 0]),
        (15, 0, [1, 0]),
        (16, 0, [1, 0]),
        (24, 0, [2, 0]),
        (28, 0, [3, 0]),
        (15, 15, [1, 1]),
        (24, 24, [2, 2]),
        (29, 29, [3, 3]),
        (100, 100, [21, 17]),
    ]
)
def test_valid_inputs(cat_age: int, dog_age: int, expected: list) -> None:
    assert get_human_age(cat_age, dog_age) == expected


@pytest.mark.parametrize(
    "cat_age, dog_age",
    [
        (-1, 0),
        (0, -5),
        (-10, -10),
    ]
)
def test_invalid_inputs(cat_age: int, dog_age: int) -> None:
    assert get_human_age(cat_age, dog_age) == [0, 0]


@pytest.mark.parametrize(
    "cat_age, dog_age",
    [
        ("15", 10),
        (None, 10),
        ([15], 10),
        ({"age": 15}, 10)
    ]
)
def test_invalid_type(cat_age: int, dog_age: int) -> None:
    with pytest.raises(TypeError):
        get_human_age(cat_age, dog_age)


@pytest.mark.parametrize(
    "cat_age_before, cat_age_after, dog_age_before, dog_age_after",
    [
        (14, 15, 0, 0),
        (23, 24, 0, 0),
        (27, 28, 0, 0),
        (14, 15, 14, 15),
        (23, 24, 23, 24),
        (28, 29, 28, 29),
    ]
)
def test_threshold_changes(cat_age_before: int, cat_age_after: int,
                           dog_age_before: int, dog_age_after: int) -> None:
    before = get_human_age(cat_age_before, dog_age_before)
    after = get_human_age(cat_age_after, dog_age_after)
    assert before != after
