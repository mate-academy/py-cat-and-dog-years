import pytest

from app.main import get_human_age, convert_to_human


class TestGetHumanAge:

    @pytest.mark.parametrize(
        "cat_age, dog_age, expected_result",
        [
            pytest.param(
                0,
                0,
                [0, 0],
                id="should return [0, 0] when zeroes were given"
            ),
            pytest.param(
                -1,
                -1,
                [0, 0],
                id="should return [0, 0] when negative age were given"
            ),
            pytest.param(
                4,
                4,
                [0, 0],
                id="check first year of a cat's/dog's life"
            ),
            pytest.param(
                14,
                14,
                [0, 0],
                id="check first year of a cat's/dog's life"
            ),
            pytest.param(
                15,
                15,
                [1, 1],
                id="check second year of a cat's/dog's life"
            ),
            pytest.param(
                23,
                23,
                [1, 1],
                id="check second year of a cat's/dog's life"
            ),
            pytest.param(
                24,
                24,
                [2, 2],
                id="check third year of a cat's/dog's life"
            ),
            pytest.param(
                27,
                27,
                [2, 2],
                id="check third year of a cat's/dog's life"
            ),
            pytest.param(
                28,
                28,
                [3, 2],
                id="check cat's fourth and dog's third year of life"
            ),
            pytest.param(
                28,
                29,
                [3, 3],
                id="check fourth year of a cat's/dog's life"
            ),
            pytest.param(
                100,
                100,
                [21, 17],
                id="check cat's 22-th and dog's 18-th year of life"
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

@pytest.mark.parametrize(
    "cat_age, dog_age, expected_error",
    [
        pytest.param(
            "23", 12, TypeError, id="Age can't be string"
        ),
        pytest.param(
            23, None, TypeError, id="Age can't be bool type"
        )
    ]
)
def test_with_incorrect_type(
        cat_age: int,
        dog_age: int,
        expected_error: type[TypeError]
) -> None:
    with pytest.raises(expected_error):
        get_human_age(cat_age, dog_age)
