from app.main import get_human_age, convert_to_human

import pytest


@pytest.mark.parametrize(
    "animal_age, first_year, second_year, each_year, expected",
    [
        pytest.param(10, 15, 9, 4, 0, id="Below_First_Year_Second_Year"),
        pytest.param(16, 15, 9, 4, 1, id="First_Year"),
        pytest.param(24, 15, 9, 4, 2, id="Second_Year"),
        pytest.param(100, 15, 9, 4, 21, id="Multiple_Each_Year_Conversions"),
    ],
)
def test_convert_to_human(
    animal_age: int,
    first_year: int,
    second_year: int,
    each_year: int,
    expected: int,
) -> None:
    assert (
        convert_to_human(animal_age, first_year, second_year, each_year)
        == expected
    )


@pytest.mark.parametrize(
    "cat_age, dog_age, expected",
    [
        pytest.param(1, 1, [0, 0], id="Cat_Dog_Below_First_Year"),
        pytest.param(23, 23, [1, 1], id="Cat_Dog_First_Year"),
        pytest.param(24, 24, [2, 2], id="Cat_Dog_Second_Year"),
        pytest.param(30, 30, [3, 3], id="Cat_Dog_Third_Year"),
        pytest.param(100, 100, [21, 17], id="Cat_Dog_Multiple_Years"),
    ],
)
def test_get_human_age(cat_age: int, dog_age: int, expected: list) -> None:
    assert get_human_age(cat_age, dog_age) == expected


if __name__ == "__main__":
    pytest.main()
