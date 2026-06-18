import pytest
from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, expected_human_age",
    [
        (0, 0, [0, 0]),
        (14, 9, [0, 0]),
        (15, 15, [1, 1]),
        (20, 15, [1, 1]),
        (25, 24, [2, 2]),
        (29, 30, [3, 3]),
        (30, 50, [3, 7]),
        (35, 80, [4, 13]),
        (40, 100, [6, 17]),
        (1000, 1000, [246, 197])
    ]
)
def test_get_human_age(cat_age: int,
                       dog_age: int,
                       expected_human_age: list
                       ) -> None:
    assert get_human_age(cat_age, dog_age) == expected_human_age


def test_negative_age_raises_error() -> None:
    with pytest.raises(ValueError):
        get_human_age(-1, 10)

    with pytest.raises(ValueError):
        get_human_age(10, -1)


@pytest.mark.parametrize("age", [14, 15])
def test_boundary_values(age: int) -> None:
    assert get_human_age(age, 0)[0] == 0 if age < 15 else 1
