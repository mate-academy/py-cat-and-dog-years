import pytest
from app.main import get_human_age
from typing import Any


class TestPetAgeToHuman:
    @pytest.mark.parametrize(
        "cat_age, dog_age, expected",
        [
            pytest.param(
                -1,
                -1,
                [0, 0],
                id="negative pet age"
            ),
            pytest.param(
                0,
                0,
                [0, 0],
                id="pet age is 0"
            ),
            pytest.param(
                14,
                14,
                [0, 0],
                id="pet age is less then 1 human year"
            ),
            pytest.param(
                15,
                15,
                [1, 1],
                id="pet age is 1 human year"
            ),
            pytest.param(
                23,
                23,
                [1, 1],
                id="pet age is more then 1 but less then 2 human years"
            ),
            pytest.param(
                24,
                24,
                [2, 2],
                id="pet age is 2 human years"
            ),
            pytest.param(
                28,
                28,
                [3, 2],
                id="same pet age - different human years"
            ),
            pytest.param(
                28,
                29,
                [3, 3],
                id="same human years - different pet age"
            ),
            pytest.param(
                100,
                100,
                [21, 17],
                id="test for really old pet age"
            ),
        ]
    )
    def test_get_human_age(
            self,
            cat_age: int,
            dog_age: int,
            expected: list
    ) -> None:
        assert get_human_age(cat_age, dog_age) == expected

    @pytest.mark.parametrize(
        "cat_age_1, dog_age_1, expected_1",
        [
            pytest.param(
                None,
                15,
                TypeError,
                id="should return 'TypeError' when pet age is 'None'"
            ),
            pytest.param(
                15,
                "m",
                TypeError,
                id="should return 'TypeError' when pet age isn't 'int'"
            )
        ]
    )
    def test_type_error_cases(
            self,
            cat_age_1: Any,
            dog_age_1: Any,
            expected_1: Any
    ) -> None:
        with pytest.raises(expected_1):
            get_human_age(cat_age_1, dog_age_1)
