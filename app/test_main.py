import pytest
from typing import Union

from app.main import get_human_age, convert_to_human


@pytest.mark.parametrize(
    "test_cat_age, test_dog_age, expected_result",
    [
        pytest.param(
            0, 0, [0, 0],
            id="result_have_to_be_correct"
        ),
        pytest.param(
            14, 14, [0, 0],
            id="result_have_to_be_correct"
        ),
        pytest.param(
            23, 23, [1, 1],
            id="result_have_to_be_correct"
        ),
        pytest.param(
            27, 27, [2, 2],
            id="result_have_to_be_correct"
        ),
        pytest.param(
            100, 100, [21, 17],
            id="result_have_to_be_correct"
        )
    ]
)
def test_have_to_return_correct_result(test_cat_age: Union[int, float],
                                       test_dog_age: Union[int, float],
                                       expected_result: int) -> None:
    assert get_human_age(test_cat_age, test_dog_age) == expected_result


@pytest.mark.parametrize(
    "test_animal_age, "
    "test_first_year, "
    "test_second_year, "
    "test_each_year_cat, "
    "expected_result",
    [
        pytest.param(
            15.3, 14.1, 9.1, 3, 1,
            id="type_result_have_to_be_equal_to_int"
        ),
        pytest.param(
            30.2, 14.2, 9.1, 4, 3,
            id="type_result_have_to_be_equal_to_int"
        ),
        pytest.param(
            25.1, 14, 9.1, 4, 2,
            id="type_result_have_to_be_equal_to_int"
        )
    ]
)
def test_have_to_be_equal_int(test_animal_age: Union[int, float],
                              test_first_year: Union[int, float],
                              test_second_year: Union[int, float],
                              test_each_year_cat: Union[int, float],
                              expected_result: int) -> None:
    assert convert_to_human(test_animal_age,
                            test_first_year,
                            test_second_year,
                            test_each_year_cat) == expected_result
