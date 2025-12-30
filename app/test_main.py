import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, expected",
    [
        (0, 0, [0, 0], id="zero_years"),
        (14, 14, [0, 0], id="less_than_15_years"),
        (15, 15, [1, 1], id="one_human_age"),
        (23, 23, [1, 1], id="one_human_age"),
        (24, 24, [2, 2], id="twp_human_age"),
        (27, 27, [2, 2], id="twp_human_age"),
        (28, 28, [3, 2], id="two_human_age"),
        (100, 100, [21, 17], id="big_human_age")
    ]
)
def test_get_human_age(cat_age, dog_age, expected):
    assert get_human_age(cat_age, dog_age) == expected
