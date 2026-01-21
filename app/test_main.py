import pytest
from app.main import get_human_age


class NegativeException(Exception):
    pass


class TooBigException(Exception):
    pass


@pytest.mark.parametrize(
    "cat_age,dog_age,result",
    [
        pytest.param(
            28,
            28,
            [3, 2],
            id="should calculate cat and dog years"
        ),
        pytest.param(
            14,
            14,
            [0, 0],
            id="return 0 if animal_age less than first_year"
        ),
        pytest.param(
            23,
            23,
            [1, 1],
            id="return 1 if animal_age less than sum first_year + second_year"
        ),
        pytest.param(
            0,
            -1,
            [0, 0],
            id="return 0 if ages 0 or less than 0"
        ),
        pytest.param(
            2**31,
            2**31,
            [536870908, 429496726],
            id="calculate if data is too big"
        ),
    ]
)
def test_can_calculate_cats_and_dogs_year(cat_age: int,
                                          dog_age: int,
                                          result: list) -> None:
    assert get_human_age(cat_age, dog_age) == result


@pytest.mark.parametrize(
    "cat_age,dog_age,raised_error",
    [
        pytest.param(
            "28",
            False,
            TypeError,
            id="raise exception when data type is incorrect"
        )
    ]
)
def test_raise_error_if_data_incorrect(cat_age: int,
                                       dog_age: int,
                                       raised_error: TypeError) -> None:
    with pytest.raises(raised_error):
        get_human_age(cat_age, dog_age)
