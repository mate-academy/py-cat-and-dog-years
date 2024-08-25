import pytest
from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_years, dog_years, expected_result",
    [
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (23, 23, [1, 1]),
        (24, 24, [2, 2]),
        (27, 28, [2, 2]),
        (28, 29, [3, 3]),
    ],
)
def test_ages(cat_years: int, dog_years: int, expected_result: list) -> None:
    assert get_human_age(cat_years, dog_years) == expected_result


@pytest.mark.parametrize(
    "cat_years, dog_years",
    [
        ("14", 14),
        (15, "15"),
        ("15", "15")
    ],
)
def test_errors(cat_years: int, dog_years: int) -> None:
    with pytest.raises(TypeError):
        get_human_age(cat_years, dog_years)
