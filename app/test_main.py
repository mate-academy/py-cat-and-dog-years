import pytest
from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, human_years",
    [
        pytest.param(
            -10,
            -20,
            [0, 0],
            id="checking for negative years"
        ),
        pytest.param(
            0,
            0,
            [0, 0],
            id="checking for zero years"
        ),
        pytest.param(
            14,
            14,
            [0, 0],
            id="14 cat/dog years should convert into 0 human age"
        ),
        pytest.param(
            15,
            15,
            [1, 1],
            id="15 cat/dog years should convert into 1 human age"
        ),
        pytest.param(
            23,
            23,
            [1, 1],
            id="23 cat/dog years should convert into 1 human age"
        ),
        pytest.param(
            24,
            24,
            [2, 2],
            id="24 cat/dog years should convert into 2 human age"
        ),
        pytest.param(
            27,
            28,
            [2, 2],
            id="27/28 cat/dog years should convert into 2 human age"
        ),
        pytest.param(
            28,
            29,
            [3, 3],
            id="28/29 cat/dog years should convert into 3 human age"
        ),
        pytest.param(
            100,
            100,
            [21, 17],
            id="check for big years"
        )
    ]
)
def test_checking_edge_cases(
    cat_age: int,
    dog_age: int,
    human_years: list[int]
) -> None:
    assert get_human_age(cat_age, dog_age) == human_years


@pytest.mark.parametrize(
    "cat_age, dog_age, expected_error",
    [
        pytest.param("12", "5", TypeError, id="data type check")
    ]
)
def test_data_type_check(
    cat_age: int,
    dog_age: int,
    expected_error: Exception
) -> None:
    with pytest.raises(expected_error):
        get_human_age(cat_age, dog_age)
