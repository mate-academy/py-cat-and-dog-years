import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age,dog_age,result",
    [
        (0, 0, [0, 0]),
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (28, 28, [3, 2]),
        (-1, -11, [0, 0])

    ],
    ids=[
        "If cat and dog age = 0 should return [0, 0]",
        "Should return [0, 0]",
        "Should return [1, 1]",
        "Should return [3, 2]",
        "If age is negative, should return [0, 0]"
    ]
)
def test_get_human_age(cat_age, dog_age, result):
    assert get_human_age(cat_age, dog_age) == result
