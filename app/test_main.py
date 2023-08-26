import pytest

from app.main import get_human_age, convert_to_human


class TestGetHumanAge:

    @pytest.mark.parametrize(
        "cat_age,dog_age,expected_result",
        [
            pytest.param(
                14,
                14,
                [0, 0],
                id="the first year of a cat's/dog's life"
            ),
            pytest.param(
                23,
                23,
                [1, 1],
                id="the second year of a cat's/dog's life"
            ),
            pytest.param(
                27,
                27,
                [2, 2],
                id="the third year of a cat's/dog's life"
            ),
            pytest.param(
                28,
                28,
                [3, 2],
                id="the cat's fourth and dog's second year of life"
            ),
            pytest.param(
                100,
                100,
                [21, 17],
                id="the cat's 22-th and dog's 18-th year of life"
            ),
        ]
    )
    def test_get_human_age(
        self,
        cat_age: int,
        dog_age: int,
        expected_result: list
    ) -> None:
        assert get_human_age(cat_age, dog_age) == expected_result


class TestConvertToHuman:
    @pytest.mark.parametrize(
        "animal_age,first_year,second_year,each_year,expected_result",
        [
            pytest.param(
                13, 15, 9, 4, 0, id="case when age less than first year"
            ),
            pytest.param(
                16, 15, 9, 4, 1, id="case when animal age less "
                                    "than first year + second year"
            ),
            pytest.param(
                40, 15, 9, 4, 6, id="case when animals have 40 years"
            )
        ]
    )
    def test_convert_to_human(
        self,
        animal_age: int,
        first_year: int,
        second_year: int,
        each_year: int,
        expected_result: int
    ) -> None:
        result = convert_to_human(
            animal_age, first_year, second_year, each_year
        )

        assert result == expected_result
