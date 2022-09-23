import pytest

from app.main import get_human_age


class TestMain:
    @pytest.mark.parametrize(
        "cat_age,dog_age,expected_result",
        [
            pytest.param(
                0, 0, [0, 0],
                id="should return zeroes when we input zeroes"
            ),
            pytest.param(
                14, 14, [0, 0],
                id="should return zeroes when parameters less then 15"
            ),
            pytest.param(
                15, 15, [1, 1],
                id="should return [1, 1]"
            ),
            pytest.param(
                23, 23, [1, 1],
                id="should return [1, 1]"
            ),
            pytest.param(
                24, 24, [2, 2],
                id="should return [2, 2]"
            ),
            pytest.param(
                27, 27, [2, 2],
                id="should return [2, 2]"
            ),
            pytest.param(
                28, 28, [3, 2],
                id="should return [3, 2]"
            ),
            pytest.param(
                100, 100, [21, 17],
                id="should return [21, 17]"
            ),
        ]
    )
    def test_convert_age_correctly(
            self,
            cat_age,
            dog_age,
            expected_result
            ):
        assert get_human_age(cat_age, dog_age) == expected_result
