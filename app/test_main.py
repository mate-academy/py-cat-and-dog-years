import pytest

from app.main import get_human_age, convert_to_human


class TestGetHumanAge:
    @pytest.mark.parametrize(
        "initial_cat_age,"
        "initial_dog_age,"
        "expected_convert_list",
        [
            (0, 0, [0, 0]),
            (14, 14, [0, 0]),
            (15, 15, [1, 1]),
            (23, 23, [1, 1]),
            (24, 24, [2, 2]),
            (27, 27, [2, 2]),
            (28, 28, [3, 2]),
            (100, 100, [21, 17])
        ],
    )
    def test_should_get_human_age_correctly(
            self,
            initial_cat_age: int,
            initial_dog_age: int,
            expected_convert_list: list
    ) -> None:
        assert get_human_age(
            initial_cat_age,
            initial_dog_age
        ) == expected_convert_list


class TestConvertToHuman:
    @pytest.mark.parametrize(
        "initial_animal_age,first_year,"
        "second_year,each_year,expected_human_age",
        [
            (0, 15, 9, 4, 0),
            (0, 0, 0, 4, 2),
            (14, 15, 9, 4, 0),
            (15, 15, 9, 4, 1),
            (23, 15, 9, 4, 1),
            (24, 15, 9, 4, 2),
            (27, 15, 9, 4, 2),
            (28, 15, 9, 4, 3),
            (100, 15, 9, 4, 21)
        ],
    )
    def test_should_return_correct_human_age(
            self,
            initial_animal_age: int,
            first_year: int,
            second_year: int,
            each_year: int,
            expected_human_age: int
    ) -> None:
        assert convert_to_human(
            initial_animal_age,
            first_year,
            second_year,
            each_year
        ) == expected_human_age

    @pytest.mark.parametrize(
        "initial_animal_age,first_year,"
        "second_year,each_year",
        [
            (30, 11, 9, 0),
            (28, 10, 5, 0),
            (10, 5, 3, 0)
        ],
    )
    def test_should_raise_error_if_each_year_is_0(
            self,
            initial_animal_age: int,
            first_year: int,
            second_year: int,
            each_year: int,
    ) -> None:

        with pytest.raises(ZeroDivisionError):
            convert_to_human(
                initial_animal_age,
                first_year,
                second_year,
                each_year
            )
