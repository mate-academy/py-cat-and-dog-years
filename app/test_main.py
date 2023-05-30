# from typing import Union, List
#
# import pytest
#
# from app.main import get_human_age


def test_get_human_age_return_list() -> None:
    assert isinstance(get_human_age(15, 15), list)


def test_incorrect_input_data_type_() -> None:
    with pytest.raises(TypeError):
        get_human_age("15", [15])


def test_numeric_values_in_returned_list() -> None:
    for age in get_human_age(15, 15.0):
        assert isinstance(age, (int, float))


def test_returned_list_length() -> None:
    assert len(get_human_age(15, 15)) == 2


def test_list_contains_zeros() -> None:
    assert get_human_age(-1, 0) == [0, 0]


@pytest.mark.parametrize(
    "cat_age, dog_age, expected_result",
    [
        (35.9999, 0, [4.0, 0]),
        (36.1, 0, [5.0, 0]),
        (0, 38.9999, [0, 4.0]),
        (0, 39.1, [0, 5.0]),

    ], ids=[
        "prevent_age_auto_ceiling_for_float_cat",
        "prevent_age_auto_flooring_for_float_cat",

        "prevent_age_auto_ceiling_for_float_dog",
        "prevent_age_auto_flooring_for_float_dog",

    ]
)
def test_float_argument_processed(cat_age: Union[int, float],
                                  dog_age: Union[int, float],
                                  expected_result: List[Union[int, float]]
                                  ) -> None:
    assert get_human_age(cat_age, dog_age) == expected_result


@pytest.mark.parametrize(
    "cat_age, dog_age, expected_result",
    [
        (15, 0, [1, 0]),
        (24, 0, [2, 0]),
        (28, 0, [3, 0]),

        (0, 15, [0, 1]),
        (0, 24, [0, 2]),
        (0, 29, [0, 3]),

    ], ids=[
        "first 15 cat years give 1 human year",
        "the next 9 cat years give 1 more human year",
        "every 4 next cat years give 1 extra human year",

        "first 15 dog years give 1 human year",
        "the next 9 dog years give 1 more human year",
        "every 5 next dog years give 1 extra human year"
    ]
)
def test_common_functional(cat_age: Union[int, float],
                           dog_age: Union[int, float],
                           expected_result: List[Union[int, float]]
                           ) -> None:
    assert get_human_age(cat_age, dog_age) == expected_result


@pytest.mark.parametrize(
    "cat_age, dog_age, expected_result",
    [
        (0, 0, [0, 0]),
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (23, 23, [1, 1]),
        (24, 24, [2, 2]),
        (27, 27, [2, 2]),
        (28, 28, [3, 2]),
        (100, 100, [21, 17]),

    ], ids=["zeroes should return zeroes",
            "minimum requirement for 1 human year not met",
            "minimum requirement for 1 human year met",
            "minimum requirement for 2 human years not met",
            "minimum requirement for 2 human years met",
            "minimum requirement for 3 human years not met",
            "minimum requirement for 3 human years met for cat only",
            "general test scale test",
            ]
)
def test_functional_from_requirements(cat_age: Union[int, float],
                                      dog_age: Union[int, float],
                                      expected_result: List[Union[int, float]]
                                      ) -> None:
    assert get_human_age(cat_age, dog_age) == expected_result
