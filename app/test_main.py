from app.main import get_human_age
import pytest
from typing import Type


class TestConvertFunction:
    @pytest.mark.parametrize(
        "cat_age, dog_age,expected_values",
        [
            pytest.param(
                0,
                0,
                [0, 0],
                id="should_return_list_with_2_integers"
            ),
            pytest.param(
                14,
                14,
                [0, 0],
                id="test_should_convert_animals_14_years_to_one_human"
            ),
            pytest.param(
                23,
                23,
                [1, 1],
                id="test_should_convert_animals_23_years_to_1_human"
            ),
            pytest.param(
                24,
                24,
                [2, 2],
                id="test_should_convert_animals_24_years_to_2_human"
            ),
            pytest.param(
                27,
                28,
                [2, 2],
                id="test_should_convert_cats_27_and_dogs_28_years_to_3_human"
            ),
            pytest.param(
                27,
                28,
                [3, 3],
                id="test_should_convert_cats_28_and_dogs_29_years_to_3_human"
            ),
        ]
    )
    def test_convert_age(
            self,
            cat_age: int,
            dog_age: int,
            expected_values: Exception
    ) -> None:
        assert get_human_age(cat_age, dog_age) == expected_values

    @pytest.mark.parametrize(
        "dog_age, cat_age, expected_error",
        [
            pytest.param(
                "5",
                0,
                TypeError,
                id="should raise error if values ages is not int"
            )
        ]
    )
    def test_raising_correctly(
            self,
            cat_age: int,
            dog_age: int,
            expected_error: Type[Exception]
    ) -> None:
        with pytest.raises(expected_error):
            get_human_age(cat_age, dog_age)
