import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "animal_years, expected_result",
    [
        pytest.param(
            0, [0, 0], id="should return zeros if input values are zeros"
        ),
        pytest.param(
            -10, [0, 0], id="should return zeros if input values are negative"
        ),
        pytest.param(14, [0, 0], id="should round result down"),
        pytest.param(15, [1, 1], id="should return correct result for 1 year"),
        pytest.param(23, [1, 1], id="should round result down to 1 year"),
        pytest.param(
            24, [2, 2], id="should return correct result for 2 years"
        ),
        pytest.param(27, [2, 2], id="should round result down to 2 years"),
        pytest.param(
            28, [3, 2], id="should return different values for cat and dog"
        ),
        pytest.param(
            100,
            [21, 17],
            id="should return correct values for big input values",
        ),
    ],
)
def test_should_return_correct_values(
    animal_years: int, expected_result: list[int]
) -> None:
    assert get_human_age(animal_years, animal_years) == expected_result
