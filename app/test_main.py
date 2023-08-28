import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age,dog_age,expected_years",
    [
        pytest.param(
            0,
            0,
            [0, 0],
            id="should return zeros when ages are zeros"
        ),
        pytest.param(
            14,
            14,
            [0, 0],
            id="should return zeros when cat/dog ages are less than 15 years"
        ),
        pytest.param(
            15,
            15,
            [1, 1],
            id="should return [1, 1] when cat/dog ages are 15"
        ),
        pytest.param(
            23,
            23,
            [1, 1],
            id="should return [1, 1] when cat/dog ages are 23"
        ),
        pytest.param(
            24,
            24,
            [2, 2],
            id="should return [2, 2] when cat/dog ages are 24"
        ),
        pytest.param(
            27,
            27,
            [2, 2],
            id="should return [2, 2] when cat/dog ages are 27"
        ),
        pytest.param(
            28,
            28,
            [3, 2],
            id="should return [3, 2] when cat/dog ages are 28"
        ),
        pytest.param(
            29,
            29,
            [3, 3],
            id="should return [3, 3] when cat/dog ages are 29"
        ),
        pytest.param(
            777,
            777,
            [190, 152],
            id="should return correct values when cat/dog are immortal"
        ),
        pytest.param(
            -10,
            -10,
            [0, 0],
            id="should return zeros when cat/dog ages are zeros"
        )
    ]
)
def test_calculate_years_correctly(
    cat_age: int,
    dog_age: int,
    expected_years: list[int]
) -> None:
    assert get_human_age(cat_age, dog_age) == expected_years
