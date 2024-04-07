from typing import Any

import pytest

from app.main import get_human_age


# write your code here
class TestGetHumanAge:
    @pytest.mark.parametrize(
        "cat_age,dog_age,human_age",
        [
            pytest.param(
                0, 0, [0, 0], id="0, 0 must be [0, 0]"
            ),
            pytest.param(
                14, 14, [0, 0], id="14, 14 must be [0, 0]"
            ),
            pytest.param(
                15, 15, [1, 1], id="15, 15 must be [1, 1]"
            ),
            pytest.param(
                23, 23, [1, 1], id="23, 23 must be [1, 1]"
            ),
            pytest.param(
                24, 24, [2, 2], id="24, 24 must be [2, 2]"
            ),
            pytest.param(
                27, 27, [2, 2], id="27, 27 must be [2, 2]"
            ),
            pytest.param(
                28, 28, [3, 2], id="28, 28 must be [3, 2]"
            ),
            pytest.param(
                100, 100, [21, 17], id="100, 100 must be [21, 17]"
            ),
            pytest.param(
                -1, -1, [0, 0], id="negative number check"
            ),
            pytest.param(
                10000000000000000000000000000000000000000000,
                10000000000000000000000000000000000000000000,
                [
                    2499999999999999999999999999999999999999996,
                    1999999999999999999999999999999999999999997
                ],
                id="big number check"
            )
        ]
    )
    def test_get_human_age_with_correct_parameters(
            self,
            cat_age: int,
            dog_age: int,
            human_age: list[int]
    ) -> None:
        assert get_human_age(cat_age, dog_age) == human_age

    @pytest.mark.parametrize(
        "cat_age,dog_age,expected_error",
        [
            pytest.param("1", "0", TypeError,
                         id="not integer params must raise ValueError"),
            pytest.param([1], ["0"], TypeError,
                         id="not integer params must raise ValueError"),
            pytest.param({"1": 1}, 0, TypeError,
                         id="not integer params must raise ValueError")
        ]
    )
    def test_get_human_age_with_incorrect_parameters(
            self,
            cat_age: Any,
            dog_age: Any,
            expected_error: Exception
    ) -> None:
        with pytest.raises(expected_error):
            raise get_human_age(cat_age, dog_age)
