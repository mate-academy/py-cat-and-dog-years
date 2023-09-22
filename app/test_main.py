import pytest
from app.main import get_human_age


@pytest.mark.parametrize(
    "animal_age, human_age",
    [
        ([-1, -2], [0, 0]),
        ([0, 0], [0, 0]),
        ([14, 14], [0, 0]),
        ([12, 12], [0, 0]),
        ([24, 24], [2, 2]),
        ([27, 28], [2, 2]),
        ([28, 29], [3, 3]),
        ([28, 28], [3, 2]),
        ([100, 100], [21, 17]),
        ([121, 121], [26, 21])
    ]
)
def test_worked_human_age(
        animal_age: list,
        human_age: list) -> None:
    assert get_human_age(*animal_age) == human_age
