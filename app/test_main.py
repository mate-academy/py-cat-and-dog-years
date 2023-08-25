import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age,dog_age,expected_ages",
    [
        pytest.param(0, 0, [0, 0]),
        pytest.param(14, 14, [0, 0]),
        pytest.param(15, 15, [1, 1]),
        pytest.param(23, 23, [1, 1]),
        pytest.param(24, 24, [2, 2]),
        pytest.param(27, 24, [2, 2]),
        pytest.param(28, 24, [3, 2]),
        pytest.param(28, 28, [3, 2]),
        pytest.param(28, 29, [3, 3]),
        pytest.param(60, 60, [11, 9]),
        pytest.param(1000, 1000, [246, 197]),
        pytest.param(-10, -10, [0, 0]),
    ],
)
def test_converting_ages_correctly(
    cat_age: int, dog_age: int, expected_ages: list[int]
) -> None:
    assert get_human_age(cat_age, dog_age) == expected_ages


@pytest.mark.parametrize("cat_age,dog_age", [pytest.param("15", [15, 12])])
def test_raising_errors_correctly(cat_age: int, dog_age: int) -> None:
    with pytest.raises(TypeError):
        get_human_age(cat_age, dog_age)
