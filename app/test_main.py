import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age,dog_age,expected_list",
    [
        pytest.param(0, 0, [0, 0]),
        pytest.param(14, 14, [0, 0]),
        pytest.param(15, 15, [1, 1]),
        pytest.param(23, 23, [1, 1]),
        pytest.param(24, 24, [2, 2]),
        pytest.param(27, 27, [2, 2]),
        pytest.param(28, 28, [3, 2]),
        pytest.param(100, 100, [21, 17])
    ]
)
def test_get_human_age(
        cat_age: int,
        dog_age: int,
        expected_list: list
) -> None:
    if not isinstance(cat_age, int) or not isinstance(dog_age, int):
        pytest.raises(TypeError)
    if cat_age < 0 or dog_age < 0:
        pytest.raises(ValueError)
    assert get_human_age(cat_age, dog_age) == expected_list
