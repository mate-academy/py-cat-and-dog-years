import pytest
from app.main import get_human_age


class TestGetHumanAge:

    @pytest.mark.parametrize(
        "cat_age, dog_age, expected_result",
        [
            pytest.param(0, 0, [0, 0], id="zeroes"),
            pytest.param(14, 14, [0, 0], id="checking before first year"),
            pytest.param(15, 15, [1, 1], id="checking first year"),
            pytest.param(23, 23, [1, 1], id="checking before second year"),
            pytest.param(24, 24, [2, 2], id="checking second year"),
            pytest.param(27, 27, [2, 2], id="checking before third year"),
            pytest.param(28, 28, [3, 2], id="checking third cats and "
                                            "second dogs year"),
            pytest.param(100, 100, [21, 17], id="checking very old pensioners")
        ]
    )
    def test_get_human_age(self, cat_age, dog_age, expected_result):
        assert get_human_age(cat_age, dog_age) == expected_result
