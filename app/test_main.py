import pytest
from app.main import get_human_age


@pytest.mark.parametrize(
    "input_cat_years,input_dog_years,expected_human_years",
    [
        pytest.param(
            -2, -2,
            [0, 0],
            id="negative value of cat/dog years should be equal "
               "to 0 human years"
        ),
        pytest.param(
            0, 0,
            [0, 0],
            id="0 cat/dog years should be equal to 0 human years"
        ),
        pytest.param(
            14, 14,
            [0, 0],
            id="14 cat/dog years should be equal to 0 human years"
        ),
        pytest.param(
            15, 15,
            [1, 1],
            id="15 cat/dog years should be equal to 1 human year"
        ),
        pytest.param(
            24, 24,
            [2, 2],
            id="24 cat/dog years should be equal to 2 human years"
        ),
        pytest.param(
            27, 28,
            [2, 2],
            id="27/28 cat/dog years should be equal to 2 human years"
        ),
        pytest.param(
            28, 28,
            [3, 2],
            id="28 cat/dog years should be equal "
               "to 3/2 human years accordingly"
        ),
        pytest.param(
            28, 29,
            [3, 3],
            id="28/29 cat/dog years should be equal to 3 human years"
        ),
        pytest.param(
            100, 100,
            [21, 17],
            id="100 cat/dog years should be equal to "
               "21/17 human years accordingly"
        ),
        pytest.param(
            1000, 1000,
            [246, 197],
            id="1000 cat/dog years should be equal to "
               "246/197 human years accordingly"
        )
    ]
)
def test_return_correct_values(
        input_cat_years: int,
        input_dog_years: int,
        expected_human_years: list
) -> None:
    assert get_human_age(
        input_cat_years,
        input_dog_years
    ) == expected_human_years


@pytest.mark.parametrize(
    "input_cat_years,input_dog_years",
    [
        ("1", "1")
    ]
)
def test_receive_correct_value_type(
        input_cat_years: int,
        input_dog_years: int
) -> None:
    with pytest.raises(TypeError):
        get_human_age(input_cat_years, input_dog_years)
