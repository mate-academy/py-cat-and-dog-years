import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, doge_age, result",
    [
        (0, 0, [0, 0]),
        (-3, 17, [0, 1])
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (28, 28, [3, 2]),
        (100, 100, [21, 17]),
        (3224, 20, [802, 1])

    ]
)
def test_get_human_age(
        cat_age: int,
        doge_age: int,
        result: list) -> None:
    assert (
        get_human_age(cat_age, doge_age) == result
    ), (f"Function get_human_age should return {result}, "
        f"got {get_human_age(cat_age, doge_age)} instead")
