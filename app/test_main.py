import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, expected",
    [
        pytest.param(-15, -20, [0, 0], id="both ages are negative"),
        pytest.param(0, 0, [0, 0], id="both ages are 0"),
        pytest.param(14, 14, [0, 0], id="both ages are 0"),
        pytest.param(15, 15, [1, 1], id="both ages are 1"),
        pytest.param(23, 23, [1, 1], id="both ages are 1"),
        pytest.param(24, 24, [2, 2], id="both ages are 2"),
        pytest.param(27, 28, [2, 2], id="both ages are 2"),
        pytest.param(28, 29, [3, 3], id="both ages are 3"),
        pytest.param(100, 100, [21, 17], id="both ages are different")
    ]
)
def test_get_human_age_should_be_equal_to_zero_or_negative(
        cat_age: int,
        dog_age: int,
        expected: list
) -> None:
    result = get_human_age(cat_age, dog_age)
    assert result == expected
