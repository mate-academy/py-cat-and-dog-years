import pytest
from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, result",
    [
        pytest.param(0, 0, [0, 0]),
        pytest.param(14, 14, [0, 0]),
        pytest.param(15, 15, [1, 1]),
        pytest.param(23, 23, [1, 1]),
        pytest.param(24, 24, [2, 2]),
        pytest.param(27, 27, [2, 2]),
        pytest.param(28, 28, [3, 2]),
        pytest.param(100, 100, [21, 17]),
        pytest.param(-5, -5, [0, 0]),
    ],
)
def test_get_human_age(cat_age: int, dog_age: int, result: list) -> list:
    assert get_human_age(cat_age, dog_age) == result


@pytest.mark.parametrize(
    "cat_age, dog_age, expected_error",
    [
        pytest.param("100", 100, TypeError),
        pytest.param(100, "100", TypeError),
        pytest.param("100", "100", TypeError),
    ],
)
def test_should_raising_error(
    cat_age: int, dog_age: int, expected_error: Exception
) -> Exception:
    with pytest.raises(expected_error):
        get_human_age(cat_age, dog_age)
