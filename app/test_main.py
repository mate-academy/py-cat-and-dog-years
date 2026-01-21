import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, result",
    [
        pytest.param(14, 14, [0, 0], id="zero for both"),
        pytest.param(15, 15, [1, 1], id="one for both"),
        pytest.param(23, 23, [1, 1], id="end of first year"),
        pytest.param(24, 24, [2, 2], id="two for both"),
        pytest.param(27, 28, [2, 2], id="end of second year"),
        pytest.param(28, 29, [3, 3], id="three for both"),
        pytest.param(-2, 29, [0, 3], id="zero for first"),
        pytest.param(100, 29, [21, 3], id="many years")

    ]
)
def test_get_human_age(cat_age: int, dog_age: int, result: list) -> None:
    assert get_human_age(cat_age, dog_age) == result
