import pytest
from typing import Any

from app.main import get_human_age


class TestCheckEdgeCases:
    @pytest.mark.parametrize(
        ("cat_age_input", "dog_age_input", "expected_list"),
        [
            pytest.param(
                0, 0, [0, 0],
                id="test should return 0 when input is 0"
            ),
            pytest.param(
                14, 14, [0, 0],
                id="test should return 0 when input is lower than 15"
            ),
            pytest.param(
                15, 15, [1, 1],
                id="test should return 1 when input is 15"
            ),
            pytest.param(
                23, 23, [1, 1],
                id="test should return 1 when input is between 15 and 24"
            ),
            pytest.param(
                24, 24, [2, 2],
                id="test should return 2 when input is 24"
            ),
            pytest.param(
                27, 27, [2, 2],
                id="test should return 2 when input is lower than 28"
            ),
            pytest.param(
                28, 28, [3, 2],
                id="test should return 3, 2 when input is 28"
            ),
            pytest.param(
                100, 100, [21, 17],
                id="test should return 21, 17 when input is 100"
            ),
        ]
    )
    def test_checking_edge_cases(self,
                                 cat_age_input: Any,
                                 dog_age_input: Any,
                                 expected_list: Any
                                 ) -> None:
        assert get_human_age(cat_age_input, dog_age_input) == expected_list
