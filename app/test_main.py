import pytest
from app.main import get_human_age


@pytest.mark.parametrize("cat_age, dog_age, expected", [
    pytest.param(0, 0, [0, 0], id="both_0"),
    pytest.param(14, 14, [0, 0], id="both_14"),
    pytest.param(15, 15, [1, 1], id="both_15"),
    pytest.param(23, 23, [1, 1], id="both_23"),
    pytest.param(24, 24, [2, 2], id="both_24"),
    pytest.param(27, 27, [2, 2], id="both_27"),
    pytest.param(28, 28, [3, 2], id="cat_28_dog_28"),
    pytest.param(100, 100, [21, 17], id="cat_100_dog_100"),
])
def test_get_human_age(cat_age: int, dog_age: int, expected: list) -> None:
    assert get_human_age(cat_age, dog_age) == expected
