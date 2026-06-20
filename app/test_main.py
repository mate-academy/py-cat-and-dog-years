import pytest
from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age,dog_age,expected",
    [
        (0, 0, [0, 0]),
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (23, 23, [1, 1]),
        (24, 24, [2, 2]),
        (27, 27, [2, 2]),
        (28, 28, [3, 2]),
        (29, 29, [3, 3]),
        (100, 100, [21, 17]),
        (-5, -10, [0, 0]),  # negative values
    ],
)
def test_examples(
    cat_age: int,
    dog_age: int,
    expected: list[int],
) -> None:
    assert get_human_age(cat_age, dog_age) == expected


def test_monotonic_increase() -> None:
    """Ensure human age never decreases as pet age increases."""
    for cat_age in range(1, 50):
        prev = get_human_age(cat_age - 1, 0)[0]
        curr = get_human_age(cat_age, 0)[0]
        assert curr >= prev

    for dog_age in range(1, 50):
        prev = get_human_age(0, dog_age - 1)[1]
        curr = get_human_age(0, dog_age)[1]
        assert curr >= prev
