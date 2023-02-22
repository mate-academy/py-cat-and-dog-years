from app.main import get_human_age

import pytest


class TestGetHumanAge:
    @pytest.mark.parametrize(
        "cat_age, dog_age, expected_result", [
            pytest.param(
                14,
                14,
                [0, 0],
                id="under lower boundary condition"
            ),
            pytest.param(
                15,
                23,
                [1, 1],
                id="function should return 1 for 15 >= arguments <= 23"
            ),
            pytest.param(
                24,
                29,
                [2, 3],
                id="upper boundary condition"
            ),
            pytest.param(
                -15,
                -14,
                [0, 0],
                id="negative data"
            ),
            pytest.param(
                35.01,
                30.0,
                [4.0, 3.0],
                id="float data"
            )
        ]
    )
    def test_data_boundary_conditions(
            self,
            cat_age: int,
            dog_age: int,
            expected_result: list
    ) -> None:
        assert get_human_age(cat_age, dog_age) == expected_result
