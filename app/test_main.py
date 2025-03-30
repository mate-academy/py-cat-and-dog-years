import pytest
from app.main import get_human_age


class TestHumanAge:
    @pytest.mark.parametrize(
        "cat_age,dog_age,in_humans_age",
        [
            pytest.param(
                0,
                0,
                [0, 0],
                id="returns zero animal age returns zero human age",
            ),
            pytest.param(
                14,
                14,
                [0, 0],
                id="animal age less than first year returns zero",
            ),
            pytest.param(
                15,
                15,
                [1, 1],
                id="animal age equals first year returns one",
            ),
            pytest.param(
                23,
                23,
                [1, 1],
                id="animal age within first and second year returns one",
            ),
            pytest.param(
                24,
                24,
                [2, 2],
                id="animal age after second year returns two",
            ),
            pytest.param(
                27,
                27,
                [2, 2],
                id="should return 2s when years equal 27",
            ),
            pytest.param(
                28,
                28,
                [3, 2],
                id="animal age calculates additional years correctly",
            ),
            pytest.param(
                100,
                100,
                [21, 17],
                id="should return 21 and 17 when years equal 100"),
        ]
    )
    def test_should_work_correctly(
            self,
            cat_age: int,
            dog_age: int,
            in_humans_age: list
    ) -> None:
        assert get_human_age(cat_age, dog_age) == in_humans_age
