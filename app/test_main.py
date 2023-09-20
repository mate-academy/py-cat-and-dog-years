import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, expected_result",
    [
        pytest.param(
            1,
            1,
            [0, 0],
            id=("should add zero to list if"
                " cat_age or dog_age less than first_year")
        ),
        pytest.param(
            23,
            23,
            [1, 1],
            id=("should add 1 to list if"
                " we use only first_year rule")
        ),
        pytest.param(
            24,
            24,
            [2, 2],
            id=("should add 2 to list if"
                " we use first_year and second_year rule")
        ),
        pytest.param(
            30,
            30,
            [3, 3],
            id=("should add 3 to list if we use"
                " first_year, second_year and each year rule")),
        pytest.param(
            100,
            100,
            [21, 17],
            id=("should return correct values if we use"
                " first_year, second_year and each_year rules")),
        pytest.param(
            14,
            15,
            [0, 1],
            id="should return correct values",
        ),
        pytest.param(
            15,
            14,
            [1, 0],
            id="should return correct values",
        ),
        pytest.param(
            70,
            35,
            [13, 4],
            id="should return correct values",
        ),
        pytest.param(
            -1,
            5,
            [0, 0],
            id=("should add zero to list if"
                " cat_age or dog_age less than first_year")
        ),
        pytest.param(
            1,
            -5,
            [0, 0],
            id=("should add zero to list if"
                " cat_age or dog_age less than first_year")
        ),
    ],
)
def test_check_correct_result(
        cat_age: int,
        dog_age: int,
        expected_result: list
) -> None:
    assert get_human_age(cat_age, dog_age) == expected_result


def test_invalid_data_type() -> None:
    cat_age = "fdf"
    dog_age = True
    expected_error = TypeError

    with pytest.raises(expected_error):
        get_human_age(cat_age, dog_age)
