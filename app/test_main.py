import pytest
from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, expected_human_age",
    [
        (0, 0, [0, 0]),     # 0 cat years -> 0 human, 0 dog years -> 0 human
        (14, 9, [0, 0]),    # 14 cat years -> 0 human, 9 dog years -> 0 human
        (15, 9, [1, 0]),    # 15 cat years -> 1 human, 9 dog years -> 0 human
        (20, 15, [1, 1]),   # 20 cat years -> 1 human, 15 dog years -> 1 human
        (25, 24, [2, 2]),   # 25 cat years -> 2 human, 24 dog years -> 2 human
        (29, 30, [3, 3]),   # 29 cat years -> 3 human, 30 dog years -> 3 human
        (30, 50, [3, 7]),   # 30 cat years -> 3 human, 50 dog years -> 9 human
        (35, 80, [4, 13]),  # 35 cat years -> 4 human, 80 dog years -> 13 human
        (40, 100, [6, 17]), # 40 cat years -> 6 human, 100 dog years -> 17 human
    ]
)
def test_get_human_age(
        cat_age: int,
        dog_age: int,
        expected_human_age: int
) -> None:
    assert get_human_age(cat_age, dog_age) == expected_human_age
