import pytest

from app.main import get_human_age


@pytest.mark.parametrize("cat_age, dog_age, result", [
    pytest.param(0, 0, [0, 0]),
    pytest.param(14, 14, [0, 0]),
    pytest.param(15, 15, [1, 1]),
    pytest.param(23, 23, [1, 1]),
    pytest.param(24, 24, [2, 2]),
    pytest.param(27, 27, [2, 2]),
    pytest.param(28, 28, [3, 2]),
    pytest.param(100, 100, [21, 17]),

])
def test_function_calculations(cat_age: int, dog_age: int, result: list[int]) -> None:
    assert get_human_age(cat_age, dog_age) == result


def test_type_error() -> None:
    with pytest.raises(TypeError):
        get_human_age("Nan", False)
