import pytest
from app.main import get_human_age


class TestCatAndDogYears:
    @pytest.mark.parametrize(
        "cat_age, dog_age, result",
        [
            pytest.param(
                0,
                0,
                [0, 0],
                id="should return list with list [0, 0]"
            ),
            pytest.param(
                14,
                14,
                [0, 0],
                id="should return list with list [0, 0]"
            ),
            pytest.param(
                15,
                15,
                [1, 1],
                id="should return list with list [1, 1]"
            ),
            pytest.param(
                23,
                23,
                [1, 1],
                id="should return list with list [1, 1]"
            ),
            pytest.param(
                24,
                24,
                [2, 2],
                id="should return list with list [2, 2]"
            ),
            pytest.param(
                27,
                27,
                [2, 2],
                id="should return list with list [2, 2]"
            ),
            pytest.param(
                28,
                28,
                [3, 2],
                id="should return list with list [2, 2]"
            ),
            pytest.param(
                100,
                100,
                [21, 17],
                id="should return list with list [21, 17]"
            )
        ]
    )
    def test_get_human_age_result(
            self,
            cat_age: int,
            dog_age: int,
            result: list
    ) -> None:
        assert get_human_age(cat_age, dog_age) == result
