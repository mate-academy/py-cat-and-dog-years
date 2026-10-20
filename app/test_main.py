import pytest
from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, expected",
    [
        (0, 0, [0, 0]),
        (13, 23, [0, 1]),
        (14, 24, [0, 2]),
        (15, 25, [1, 2]),
        (23, 23, [1, 1]),
        (24, 24, [2, 2]),
        (27, 27, [2, 2]),
        (28, 28, [3, 2]),
        (100, 100, [21, 17]),
    ],
    ids=[
        "zero_years",
        "below_thresholds",
        "boundary_transition_1",
        "boundary_transition_2",
        "under_second_threshold",
        "exact_second_threshold",
        "cat_next_interval",
        "dog_next_interval",
        "large_ages",
    ],
)
def test_get_human_age(
    cat_age: int, dog_age: int, expected: list
) -> None:
    assert get_human_age(cat_age, dog_age) == expected


@pytest.mark.parametrize(
    "cat_age, dog_age",
    [
        (-1, 10),
        (10, -5),
        (-15, -15),
    ],
)
def test_get_human_age_negative_raises_value_error(
    cat_age: int, dog_age: int
) -> None:
    with pytest.raises(ValueError):
        get_human_age(cat_age, dog_age)


@pytest.mark.parametrize(
    "cat_age, dog_age",
    [
        ("15", 15),
        (15, "15"),
        (None, 15),
        (15, None),
        ([15], 15),
    ],
)
def test_get_human_age_invalid_type_raises_type_error(
    cat_age: object, dog_age: object
) -> None:
    with pytest.raises(TypeError):
        get_human_age(cat_age, dog_age)  # type: ignore[arg-type]


def test_get_human_age_returns_list() -> None:
    result = get_human_age(15, 15)
    assert isinstance(result, list)
    assert len(result) == 2
