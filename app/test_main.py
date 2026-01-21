import traceback

import pytest
from app.main import get_human_age


class TestCatAndDogParam:
    @pytest.mark.parametrize(
        "cat_age,dog_age,expected_list",
        [
            pytest.param(
                15,
                15,
                [1, 1],
                id="test if animal age 15"
            ),
            pytest.param(
                14,
                14,
                [0, 0],
                id="test_if_animal_age_less_15"
            ),
            pytest.param(
                24,
                24,
                [2, 2],
                id="test_animal_age_24"
            ),
            pytest.param(
                23,
                23,
                [1, 1],
                id="test_animal_age_less_24"
            ),
            pytest.param(
                27,
                28,
                [2, 2],
                id="test_animal_age_have_second_human_age"
            ),
            pytest.param(
                28,
                29,
                [3, 3],
                id="test_animal_age_have_third_age"
            ),
            pytest.param(
                250,
                312,
                [58, 59],
                id="test_big_value"
            )
        ]
    )
    def test_correct_return(self,
                            cat_age: int,
                            dog_age: int,
                            expected_list: list
                            ) -> None:
        assert get_human_age(cat_age, dog_age) == expected_list

    @pytest.mark.parametrize(
        "cat_age,dog_age,expected_error",
        [
            pytest.param(
                "cat",
                "dog",
                TypeError,
                id="String_type_error"
            ),
            pytest.param(
                None,
                None,
                TypeError,
                id="None_type_error"
            )
        ]
    )
    def test_correct_value(self,
                           cat_age: int,
                           dog_age: int,
                           expected_error: traceback) -> None:
        with pytest.raises(expected_error):
            get_human_age(cat_age, dog_age)
