import pytest
from app.main import get_human_age


class TestPetAgeToHuman:
    @pytest.mark.parametrize(
        "cat_age, dog_age, expected"
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
            cat_age,
            dog_age,
            expected
    ) -> None:
        assert get_human_age(cat_age, dog_age) == expected
