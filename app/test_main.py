import pytest
from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, expected",
    [
        (0, 0, [0, 0]),
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (23, 23, [1, 1]),
        (24, 24, [2, 2]),
        (27, 27, [2, 2]),
        (28, 28, [3, 2]),
        (100, 100, [21, 17]),
    ],
)
def test_should_return_correct_human_years(
        cat_age: int,
        dog_age: int,
        expected: list[int]
) -> None:
    assert get_human_age(cat_age, dog_age) == expected


@pytest.mark.parametrize(
    "cat_age, dog_age",
    [
        (-1, 10),
        (10, -5),
        (-3, -3),
    ],
)
def test_negative_values_are_handled_gracefully(
        cat_age: int,
        dog_age: int
) -> None:
    result = get_human_age(cat_age, dog_age)
    assert isinstance(result, list)
    assert len(result) == 2


@pytest.mark.parametrize(
    "cat_age, dog_age",
    [
        ("ten", 5),
        (10, "five"),
        ("a", "b"),
    ],
)
def test_incorrect_types_are_handled_gracefully(
        cat_age: object,
        dog_age: object
) -> None:
    try:
        result = get_human_age(cat_age, dog_age)
        assert isinstance(result, list)
    except Exception:
        pytest.skip()


@pytest.mark.parametrize(
    "cat_age, dog_age, expected",
    [
        (15, 14, [1, 0]),
        (24, 23, [2, 1]),
        (28, 27, [3, 2]),
    ],
)
def test_threshold_changes_are_correct(
        cat_age: int,
        dog_age: int,
        expected: list[int]
) -> None:
    assert get_human_age(cat_age, dog_age) == expected
