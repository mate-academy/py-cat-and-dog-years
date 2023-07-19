import pytest
from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_years, dog_years, human_years",
    [
        pytest.param(0, 0, [0, 0]),
        pytest.param(14, 14, [0, 0]),
        pytest.param(14.1, 14, [0, 0]),
        pytest.param(15, 15, [1, 1]),
        pytest.param(23, 23, [1, 1]),
        pytest.param(24, 24, [2, 2]),
        pytest.param(27, 27, [2, 2]),
        pytest.param(28, 28, [3, 2]),
        pytest.param(100, 100, [21, 17])
    ]
)
def test_human_years_values(
        cat_years: int,
        dog_years: int,
        human_years: list[int]
) -> None:
    assert get_human_age(cat_years, dog_years) == human_years, (
        f"Sum of {cat_years} and {dog_years} "
        f"should be equal to {human_years}")
