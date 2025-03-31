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
                15,
                [1, 1],
                id="function should return 1 for 15 >= arguments"
            ),
            pytest.param(
                23,
                23,
                [1, 1],
                id="function should return 1 for arguments <= 23"
            ),
            pytest.param(
                24,
                24,
                [2, 2],
                id="boundary condition"
            ),
            pytest.param(
                29,
                29,
                [3, 3],
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
            ),
            pytest.param(
                0,
                0,
                [0, 0]
            ),
            pytest.param(
                1000,
                1000,
                [246, 197],
                id="large values"
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

    @pytest.mark.parametrize(
        "value, expected_result",
        [
            pytest.param(
                ("string", list, [], tuple, (), {}, dict, frozenset),
                TypeError,
                id="Inappropriate type of data"
            ),
        ],
    )
    def test_inappropriate_data_type(
            self,
            value: list,
            expected_result: Exception
    ) -> None:
        with pytest.raises(TypeError):
            get_human_age(3, value)
            get_human_age(value, 4)
