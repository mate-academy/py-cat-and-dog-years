import pytest
from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, result",
    [pytest.param(0, 0, [0, 0], id="zero animal years"),
     pytest.param(14, 14, [0, 0], id="14 animal years"),
     pytest.param(15, 15, [1, 1], id="15 animal years"),
     pytest.param(27, 27, [2, 2], id="27 animal years"),
     pytest.param(28, 28, [3, 2], id="28 animal years"),
     pytest.param(-5, -3, [0, 0], id="negative value"),
     pytest.param(100, 100, [21, 17], id="100 animal years")]
)
def test_get_human_age(cat_age: int, dog_age: int, result: list) -> None:
    assert get_human_age(cat_age, dog_age) == result, \
        (f"When cat is {cat_age} cat years, and dog is {dog_age} "
         f"you should get this {result} list")
