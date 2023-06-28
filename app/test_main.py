import pytest
from app.main import get_human_age


class TestRightValue:
    @pytest.mark.parametrize(
        "cat_age, dog_age, expected_list",
        [
            pytest.param(
                0, 0, [0, 0], id="test should return zero"
            ),
            pytest.param(
                10, 10, [0, 0], id="ages below 15 years"
            ),
            pytest.param(
                15, 15, [1, 1], id="cat and dog minimum age for firs year"
            ),
            pytest.param(
                23, 23, [1, 1], id="cat and dog age are equal for second year"
            )
        ]
    )
    def test_check_value_result(self, cat_age, dog_age, expected_list):
        assert get_human_age(cat_age, dog_age) == expected_list



