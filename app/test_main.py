import pytest
from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, human_age",
    [
        pytest.param(
            14,
            15,
            [0, 1],
            id="first 15 both animal years give 1 human year"
        ),
        pytest.param(
            23,
            24,
            [1, 2],
            id="second human year is given by 9 animal's years"
        ),
        pytest.param(
            28,
            28,
            [3, 2],
            id="the third year has different value for cats and dogs"
        ),
        pytest.param(
            -1,
            0,
            [0, 0],
            id="negative number and zero give zero human years"
        ),
        pytest.param(
            14.5,
            24.5,
            [0, 2],
            id="an integer year is considered to be passed "
        ),
        pytest.param(
            100,
            100,
            [21, 17],
            id="this old pets are lucky to have good owners!"

        )
    ]
)
def test_get_human_age(
        cat_age: int,
        dog_age: int,
        human_age: int
) -> None:
    assert get_human_age(cat_age, dog_age) == human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, error",
    [
        pytest.param(
            [],
            {},
            TypeError,
            id="lists and sets can't be arguments"
        ),
        pytest.param(
            (16,),
            {"age": 24},
            TypeError,
            id="tuples and dictionaries can't be arguments"
        ),
        pytest.param(
            "15",
            "25",
            TypeError,
            id="strings can't be arguments"
        )
    ]
)
def test_get_human_age_arguments_type(
        cat_age: int,
        dog_age: int,
        error: Exception
) -> None:
    with pytest.raises(error):
        get_human_age(cat_age, dog_age)
