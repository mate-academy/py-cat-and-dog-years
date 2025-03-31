import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_years, dog_years, human_age_list",
    [
        pytest.param(
            0,
            0,
            [0, 0],
            id="test should work correctly with zeros"
        ),
        pytest.param(
            28,
            28,
            [3, 2],
            id="test should return different years with the same arguments"
        ),
        pytest.param(
            560,
            807,
            [136, 158],
            id="test should work correctly with big arguments"
        ),
        pytest.param(
            1,
            4,
            [0, 0],
            id="test should work correctly with small arguments"
        ),
        pytest.param(
            -5,
            -3,
            [0, 0],
            id="test should return zeros if arguments are negative"
        )
    ]
)
def test_should_calculate_human_age(
        cat_years: int,
        dog_years: int,
        human_age_list: list
) -> None:
    assert get_human_age(cat_years, dog_years) == human_age_list
