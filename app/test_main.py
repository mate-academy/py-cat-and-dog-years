from typing import Any
import pytest
from app.main import get_human_age


class TestGetHumanAge:

    @pytest.mark.parametrize(
        "input_values,output_values",
        [
            pytest.param(
                (0, 0),
                [0, 0],
                id="should return 0 when age 0"
            ),
            pytest.param(
                (14, 14),
                [0, 0],
                id="should return 0 when age under 15"
            ),
            pytest.param(
                (15, 15),
                [1, 1],
                id="should return 1 when age equal 15"
            ),
            pytest.param(
                (23, 23),
                [1, 1],
                id="should return 1 when age above 15 and under 24"
            ),
            pytest.param(
                (24, 24),
                [2, 2],
                id="should return 2 when age equal 24"
            ),
            pytest.param(
                (27, 27),
                [2, 2],
                id="should return 2 when age equal to 27 on cat and dogs edges"
            ),
            pytest.param(
                (28, 28),
                [3, 2],
                id="should return different values for threshold values"
            ),
            pytest.param(
                (100, 100),
                [21, 17],
                id="should return correct values for complex input above 24"
            ),
        ]
    )
    def test_should_return_proper_values(
        self,
        input_values: tuple,
        output_values: list
    ) -> None:
        assert get_human_age(*input_values) == output_values

    @pytest.mark.parametrize(
        "input_values,error",
        [
            pytest.param(
                (-4, 0),
                ValueError,
                id="should raise ValueError when value less than 0"
            ),
            pytest.param(
                ([1, 2], 2.3),
                TypeError,
                id="should raise TypeError if input values not int"
            )
        ]
    )
    def test_should_raise_propper_error(
        self,
        input_values: Any,
        error: Exception
    ) -> None:
        with pytest.raises(error):
            get_human_age(*input_values)
