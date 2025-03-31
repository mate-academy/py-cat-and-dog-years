import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat,dog,result",
    [
        pytest.param(14, 14, [0, 0], id="0 years if less than 15"),
        pytest.param(15, 15, [1, 1], id="1 year if more than 15"),
        pytest.param(23, 23, [1, 1], id="1 year if less than 24"),
        pytest.param(24, 24, [2, 2], id="2 years if more than 24"),
        pytest.param(27, 28, [2, 2], id="2 years if 27 cat 28 dog"),
        pytest.param(28, 29, [3, 3], id="3 years if 28 cat 29 dog"),
    ]
)
def test_cat_dog_age(cat: int, dog: int, result: list) -> None:
    assert (get_human_age(cat, dog) == result)
