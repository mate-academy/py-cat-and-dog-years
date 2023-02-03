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

    @pytest.mark.parametrize(
        "initial_cat_age,"
        "initial_dog_age,",
        [
            ("0", 0),
            (14, "14"),
            ([15, 6], 15),
            (23, (23, 4, 5)),
            ({}, 24)
        ],
    )
    def test_should_raise_error_if_incorrect_data_type(
            self,
            initial_cat_age: int,
            initial_dog_age: int

    ) -> None:

        with pytest.raises(TypeError):
            get_human_age(
                initial_cat_age,
                initial_dog_age
            )

    @pytest.mark.parametrize(
        "initial_cat_age,"
        "initial_dog_age,",
        [
            (130, 10),
            (0, 10),
            (-50, 10),
            (30, 120),
            (30, 0),
            (30, -24)
        ],
    )
    def test_should_receive_correct_animal_age(
            self,
            initial_cat_age: int,
            initial_dog_age: int

    ) -> None:
        get_human_age(
            initial_cat_age,
            initial_dog_age
        )
        with pytest.raises(AssertionError):
            assert 0 < initial_cat_age < 100
            assert 0 < initial_dog_age < 100

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
            (2000, 15, 9, 100),
            (300, 0, 0, 15),
            (30, 1, 1, 2),
        ],
    )
    def test_should_return_human_age_not_more_30(
            self,
            initial_animal_age: int,
            first_year: int,
            second_year: int,
            each_year: int
    ) -> None:
        assert convert_to_human(
            initial_animal_age,
            first_year,
            second_year,
            each_year
        ) < 30

    @pytest.mark.parametrize(
        "initial_animal_age,first_year,"
        "second_year,each_year",
        [
            (100, 15, 9, 8),
            (-99, 20, 5, 4),
            (99, 1, -2, 1),
            (50, 20, 10, -5),
            (99, 1, 2, 3),
            (99, -1, 2, 1)
        ],
    )
    def test_should_receive_correct_age(
            self,
            initial_animal_age: int,
            first_year: int,
            second_year: int,
            each_year: int
    ) -> None:

        convert_to_human(
            initial_animal_age,
            first_year,
            second_year,
            each_year
        )

        with pytest.raises(AssertionError):
            assert 0 < initial_animal_age < 100
            assert 0 < each_year < second_year
            assert first_year > 0 and second_year > 0

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

    @pytest.mark.parametrize(
        "initial_animal_age,first_year,"
        "second_year,each_year",
        [
            ("30", 11, 9, 3),
            (28, "10.9", 5, 3),
            (10, 5, [1, 4], 3),
            ("1", ("1", "3 ", 3), "1", 5)
        ],
    )
    def test_should_raise_error_if_incorrect_data_type(
            self,
            initial_animal_age: int,
            first_year: int,
            second_year: int,
            each_year: int,
    ) -> None:

        with pytest.raises(TypeError):
            convert_to_human(
                initial_animal_age,
                first_year,
                second_year,
                each_year
            )
