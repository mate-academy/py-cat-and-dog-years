import pytest

from app.main import get_human_age, convert_to_human


class TestGetHumanAge:
    @pytest.mark.parametrize(
        "cat_age, dog_age, expected_result",
        [
            pytest.param(
                14, 14, [0, 0], id="check cat_dog less than first year"
            ),
            pytest.param(15, 15, [1, 1], id="check cat_dog first year"),
            pytest.param(
                23, 24, [1, 2], id="check cat first and dog second year"
            ),
            pytest.param(28, 29, [3, 3], id="check cat_dog third year"),
            pytest.param(50, 50, [8, 7], id="check cat_dog extra years"),
        ],
    )
    def test_get_human_age(
        self, cat_age: int, dog_age: int, expected_result: list
    ) -> None:
        result = get_human_age(cat_age, dog_age)

        assert result == expected_result


class TestConvertToHuman:
    @pytest.mark.parametrize(
        "animal_age, first_year, second_year, each_year, expected_result",
        [
            pytest.param(14, 15, 9, 4, 0, id="check age less than first year"),
            pytest.param(15, 15, 9, 4, 1, id="check first year"),
            pytest.param(24, 15, 9, 4, 2, id="check second year"),
            pytest.param(50, 15, 9, 4, 8, id="check extra years"),
        ],
    )
    def test_check_convert_correctly(
        self,
        animal_age: int,
        first_year: int,
        second_year: int,
        each_year: int,
        expected_result: int,
    ) -> None:
        result = convert_to_human(
            animal_age, first_year, second_year, each_year
        )

        assert expected_result == result
