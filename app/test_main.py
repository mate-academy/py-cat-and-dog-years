import pytest
from typing import Any
from app.main import get_human_age


class TestConvertHuman:
    @pytest.mark.parametrize(
        "cat_age, dog_age, expected_result",
        [
            pytest.param(
                0, 0, [0, 0],
                id="output 0 when input cat dog age are zeros"
            ),
            pytest.param(
                14, 13, [0, 0],
                id="output 0 when input cat dog age less than 15"
            ),
            pytest.param(
                15, 15, [1, 1],
                id="output 1 when input cat dog age 15"
            ),
            pytest.param(
                23, 23, [1, 1],
                id="output 1 when input cat dog age less than 24"
            ),
            pytest.param(
                24, 24, [2, 2],
                id="output 2 when input cat dog age 24"
            ),
            pytest.param(
                28, 29, [3, 3],
                id="every 4 next cat and 5 next dog years 1 extra human year"
            ),
            pytest.param(
                100, 100, [21, 17],
                id="large_input"
            ),
            pytest.param(
                -18, -6, [0, 0],
                id="output 0 when input cat dog age is negative"
            )
        ]
    )
    def test_get_human_age(self,
                           cat_age: int,
                           dog_age: int,
                           expected_result: list) -> None:
        assert get_human_age(cat_age, dog_age) == expected_result


class TestException:
    @pytest.mark.parametrize(
        "cat_age, dog_age, expected_error",
        [
            pytest.param(
                "one", "one", TypeError,
                id="should raise error when input is string"
            ),
            pytest.param(
                [28], [28], TypeError,
                id="should raise error when input is list"
            ),
        ]
    )
    def test_raising_errors(self,
                            cat_age: Any,
                            dog_age: Any,
                            expected_error: Any) -> None:
        with pytest.raises(expected_error):
            get_human_age(cat_age, dog_age)
