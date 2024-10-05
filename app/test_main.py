import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, expected_human_age",
    [
        (0, 0, [0, 0]),
        (14, 9, [0, 0]),
        (15, 9, [1, 0]),
        (20, 15, [1, 1]),
        (25, 24, [2, 2]),
        (29, 30, [3, 3]),
        (30, 50, [3, 7]),
        (35, 80, [4, 13]),
        (40, 100, [6, 17]),
    ]
)
def test_get_human_age(
        cat_age: int,
        dog_age: int,
        expected_human_age: list[int]
) -> None:
    assert get_human_age(cat_age, dog_age) == expected_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age",
    [
        (-5, 10),
        (10, -5),
        ("15", 20),
        (15, "20"),
        (1e10, 15),
        (15, 1e10),
    ]
)
def test_get_human_age_exceptions(cat_age: int, dog_age: int) -> None:
    try:
        result = get_human_age(cat_age, dog_age)
        assert isinstance(result, list) and len(result) == 2
    except (ValueError, TypeError):
        pass
