import pytest

from app.main import get_human_age


class TestGetHumanAge:
    @pytest.mark.parametrize(
        "cat_age, dog_age, result",
        [
            pytest.param(
                0,
                0,
                [0, 0],
                id="initial conditions"
            ),
            pytest.param(
                14,
                14,
                [0, 0],
                id="ages before first threshold"
            ),
            pytest.param(
                15,
                15,
                [1, 1],
                id="first threshold"
            ),
            pytest.param(
                24,
                24,
                [2, 2],
                id="second threshold"
            ),
            pytest.param(
                28,
                28,
                [3, 2],
                id="third threshold"
            ),
            pytest.param(
                100,
                100,
                [21, 17],
                id="larger ages"
            ),

        ]
    )
    def test_get_human_age(
            self,
            cat_age: int,
            dog_age: int,
            result: list
    ) -> None:
        assert get_human_age(cat_age, dog_age) == result
