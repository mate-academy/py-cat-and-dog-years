from app.main import get_human_age

import pytest


class TestGetHumanAge:

    @pytest.mark.parametrize(
        "cat_age,dog_age,expected_result",
        [
            pytest.param(
                0,
                0,
                [0, 0],
                id="should return [0, 0] if pets' age is 0"
            ),
            pytest.param(
                14,
                5,
                [0, 0],
                id="should return [0, 0] if pets' age is less than 15"
            ),
            pytest.param(
                15,
                15,
                [1, 1],
                id="should return [1, 1] if pets' age is 15"
            ),
            pytest.param(
                16,
                23,
                [1, 1],
                id="should return [1, 1] if 15 < pets' age < 24"
            ),
            pytest.param(
                24,
                24,
                [2, 2],
                id="should return [2, 2] if pets' age is 24"
            ),
            pytest.param(
                26,
                27,
                [2, 2],
                id="should return [2, 2] if 2 < pets' age in human years < 3"
            ),
            pytest.param(
                28,
                28,
                [3, 2],
                id="should return correct difference between cat's age and "
                   "dog's age after age of 2 years"
            ),
            pytest.param(
                100,
                100,
                [21, 17],
                id="should return correct values for old age"
            )
        ]
    )
    def test_get_human_age_correctly(self,
                                     cat_age: int,
                                     dog_age: int,
                                     expected_result: list) -> None:
        assert get_human_age(cat_age, dog_age) == expected_result
