import pytest
from app.main import get_human_age


class TestCatDogConvertAge:
    @pytest.mark.parametrize(
        "cat_age, dog_age, expected_array",
        [
            pytest.param(
                0,
                0,
                [0, 0],
                id="should return [0, 0] if ages are less than 15"
            ),
            pytest.param(
                15,
                15,
                [1, 1],
                id="should return [1, 1] if both ages equal 15"
            ),
            pytest.param(
                27,
                27,
                [2, 2],
                id="should return [2, 2] if both ages equal 27"
            ),
            pytest.param(
                28,
                28,
                [3, 2],
                id="should return [3, 2] if both ages are equal 28"
            ),
            pytest.param(
                23,
                23,
                [1, 1],
                id="should return [2, 2] if both ages are equal 23"
            ),
            pytest.param(
                100,
                100,
                [21, 17],
                id="should return [21, 17] if both ages are equal 100"
            )
        ]
    )
    def test_correctly_convert_animal_age(
            self,
            cat_age: int,
            dog_age: int,
            expected_array: list
    ) -> None:
        result = get_human_age(cat_age, dog_age)
        assert result == expected_array
