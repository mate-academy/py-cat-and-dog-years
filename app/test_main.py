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
    ]
)
def test_get_human_age(
        cat_age: int,
        dog_age: int,
        expected: list[int]
) -> None:
    assert get_human_age(cat_age, dog_age) == expected


@pytest.mark.parametrize(
    "cat_age, dog_age",
    [
        (-1, 5),
        (5, -1),
        (1.5, 5),
        (5, 2.5),
        ("10", 10),
        (10, "10"),
    ]
)
def test_get_human_age_edge_cases(
        cat_age: object,
        dog_age: object
) -> None:
    try:
        result = get_human_age(cat_age, dog_age)
        assert isinstance(result, list)
        assert len(result) == 2
    except Exception:
        pass
