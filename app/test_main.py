import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, expected",
    [
        (1, 1, (0, 0)),
        (14, 14, (0, 0)),
        (15, 15, (1, 1)),
        (23, 24, (2, 2)),
        (28, 29, (3, 3)),
    ],
)
def test_get_human_age(
    cat_age: float,
    dog_age: float,
    expected: tuple[int, int],
) -> None:
    result = get_human_age(cat_age, dog_age)
    assert result == expected


def test_additional_boundary_cases() -> None:
    assert get_human_age(16, 16) == (1, 1)
    assert get_human_age(24, 24) == (2, 2)
    assert get_human_age(32, 34) == (4, 4)
    assert get_human_age(34, 29) == (3, 3)
