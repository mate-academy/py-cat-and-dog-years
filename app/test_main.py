import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, expected_list",
    [
        (-13, -10, [0, 0]),
        (0, 0, [0, 0]),
        (14, 14, [0, 0]),
        (23, 23, [1, 1]),
        (27, 27, [2, 2]),
        (100, 100, [21, 17]),
        (1024, 536, [252, 104])
    ]
)
def test_get_human_age(cat_age, dog_age, expected_list):
    assert get_human_age(cat_age, dog_age) == expected_list
