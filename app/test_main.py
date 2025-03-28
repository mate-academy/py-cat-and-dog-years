import pytest

from app.main import get_human_age, convert_to_human


@pytest.mark.parametrize(
    "cat_age,dog_age,expected_result",
    [
        pytest.param(
            100, 100, [21, 17],
            id="result_should_be_correct"
        ),
        pytest.param(
            15, 15, [1, 1],
            id="result_should_be_correct"
        ),
        pytest.param(
            24, 24, [2, 2],
            id="result_should_be_correct"
        ),
        pytest.param(
            14, 14, [0, 0],
            id="result_should_be_correct"
        ),
        pytest.param(
            23, 23, [1, 1],
            id="result_should_be_correct"
        )
    ]
)
def test_should_check_correct_data(
        cat_age: int,
        dog_age: int,
        expected_result: list) -> None:
    assert get_human_age(cat_age, dog_age) == expected_result


@pytest.mark.parametrize(
    "animal_age,first_year,second_year,each_year_cat,expected_result",
    [
        pytest.param(
            15.3, 14.1, 9.1, 3, 1,
            id="result_should_be_int"
        ),
        pytest.param(
            25.3, 14.2, 9.4, 3, 2,
            id="result_should_be_int"
        ),
        pytest.param(
            23, 14.1, 9.2, 3, 1,
            id="result_should_be_int"
        )

    ]
)
def test_convert_to_human(
        animal_age: int,
        first_year: int,
        second_year: int,
        each_year_cat: int,
        expected_result: int) -> None:
    assert convert_to_human(
        animal_age,
        first_year,
        second_year,
        each_year_cat
    ) == expected_result
