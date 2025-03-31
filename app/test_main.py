import pytest

from app.main import get_human_age, convert_to_human


class TestGetHumanAge:
    @pytest.mark.parametrize(
        "cat_age,dog_age,expected",
        [
            pytest.param(
                30,
                30,
                [3, 3],
                id="check normal values",
            ),
            pytest.param(
                14,
                14,
                [0, 0],
                id="should return 0 for animal age less than 15",
            ),
            pytest.param(
                -1,
                -1,
                [0, 0],
                id="for negative values should return 0",
            ),
            pytest.param(
                10 ** 1000,
                10 ** 1000,
                [
                    2499999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999996,  # noqa: E501 Need loog number for check
                    1999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999997  # noqa: E501 Need loog number for check
                ],
                id="Should work properly with large numbers",
            )
        ],
    )
    def test_get_human_age(
            self,
            cat_age: int,
            dog_age: int,
            expected: int | None
    ) -> None:
        assert (
            get_human_age(cat_age, dog_age) == expected
        )

    @pytest.mark.parametrize(
        "cat_age,dog_age,expected_error",
        [
            pytest.param(
                "",
                "",
                TypeError,
                id="should raise TypeError if params are not int",
            ),
        ]
    )
    def test_cannot_add_int_and_str(
            self,
            cat_age: int,
            dog_age: int,
            expected_error: Exception
    ) -> None:
        with pytest.raises(expected_error):
            get_human_age(cat_age, dog_age)


class TestConvertToHuman:
    @pytest.mark.parametrize(
        "animal_age,first_year,second_year,each_year,expected",
        [
            pytest.param(
                14, 9, 4, 5, 0,
                id="lesser 15 animal years return 0 human",
            ),
            pytest.param(
                30,
                15,
                9,
                4,
                3,
                id="check normal values",
            ),
            pytest.param(
                14,
                15,
                9,
                4,
                0,
                id="should return 0 for animal age less than 15",
            ),
            pytest.param(
                -1,
                -15,
                -9,
                -4,
                -4,
                id="for negative values should return negative",
            ),
            pytest.param(
                10 ** 1000,
                15 ** 1000,
                9 ** 1000,
                4 ** 1000,
                (
                    0
                ),
                id="Should work properly with large numbers",
            )
        ],
    )
    def test_convert_to_human(
            self,
            animal_age: int,
            first_year: int,
            second_year: int,
            each_year: int,
            expected: int | None
    ) -> None:
        assert (
            convert_to_human(
                animal_age,
                first_year,
                second_year,
                each_year
            ) == expected
        )

    @pytest.mark.parametrize(
        "animal_age,first_year,second_year,each_year,expected_error",
        [
            pytest.param(
                0,
                0,
                0,
                0,
                ZeroDivisionError,
                id="should raise ZeroDivisionError if each_year is 0",
            ),
            pytest.param(
                "",
                "",
                "",
                "",
                TypeError,
                id="should raise TypeError if params are not int",
            ),
        ]
    )
    def test_cannot_add_int_and_str(
            self,
            animal_age: int,
            first_year: int,
            second_year: int,
            each_year: int,
            expected_error: Exception
    ) -> None:
        with pytest.raises(expected_error):
            convert_to_human(
                animal_age,
                first_year,
                second_year,
                each_year
            )
