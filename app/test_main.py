import pytest
from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_years, dog_years, human_years",
    [
        pytest.param(
            0,
            0,
            [0, 0],
            id="should return [0,0] when inputs are zero"
        ),
        pytest.param(
            14,
            14,
            [0, 0],
            id="should return [0, 0] when animal years less than 15"
        ),
        pytest.param(
            15,
            15,
            [1, 1],
            id="should return [1,1] when animal years equal 15"
        ),
        pytest.param(
            23,
            23,
            [1, 1],
            id="should return [1,1] when animal years doesn't reach 2 human"
        ),
        pytest.param(
            24,
            24,
            [2, 2],
            id="should return [2,2] when animal years reach 2 human"
        ),
        pytest.param(
            27,
            27,
            [2, 2],
            id="should return [2,2] when animal years doesn't reach 3 human"
        ),
        pytest.param(
            28,
            28,
            [3, 2],
            id="should return [3,2] when cat reach 3 human year and dog not"
        ),
        pytest.param(
            100,
            100,
            [21, 17],
            id="should return [21,17] when cat and dog age is 100"
        ),
    ]
)
def test_convert_animal_to_human_years_correctly(cat_years: int,
                                                 dog_years: int,
                                                 human_years: list) -> None:
    assert get_human_age(cat_years, dog_years) == human_years
