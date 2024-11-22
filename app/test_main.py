import pytest

from typing import Any

from .main import get_human_age


class TestGetHumanAge:
    @pytest.mark.parametrize(
        "input_animal_age,output_cat_age,output_dog_age",
        [
            pytest.param(
                0, 0, 0,
                id="should return list of 0 if input was 0"
            ),
            pytest.param(
                -1, 0, 0,
                id="should return list of 0 if input was < 0"
            ),
            pytest.param(
                14, 0, 0,
                id="should correctly calculate 1 year (1st test)"
            ),
            pytest.param(
                15, 1, 1,
                id="should correctly calculate 1 year (2nd test)"
            ),
            pytest.param(
                23, 1, 1,
                id="should correctly calculate 1 year (3rd test)"
            ),
            pytest.param(
                24, 2, 2,
                id="should correctly calculate 2 year (1st test)"
            ),
            pytest.param(
                27, 2, 2,
                id="should correctly calculate 2 year (2nd test)"
            ),
            pytest.param(
                28, 3, 2,
                id="should correctly calculate 1 year (3rd test)"
            ),
            pytest.param(
                29, 3, 3,
                id="should correctly calculate 2 year (4th test)"
            ),
            pytest.param(
                100, 21, 17,
                id="should correctly calculate age for different animals"
            ),
        ]
    )
    def test_calculate_age_correctly(self,
                                     input_animal_age: int,
                                     output_cat_age: Any,
                                     output_dog_age: Any) -> None:
        assert (
            [output_cat_age, output_dog_age]
            == get_human_age(input_animal_age, input_animal_age)
        )

    def test_should_return_list_of_int(self) -> None:
        cat_age_to_human, dog_age_to_human = get_human_age(45, 45)

        assert (
            isinstance(cat_age_to_human, int)
            and isinstance(dog_age_to_human, int)
        )
