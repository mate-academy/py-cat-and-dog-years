import pytest
from app.main import get_human_age


class TestGetHumanAge:
    @pytest.mark.parametrize(
        "cat_age,dog_age,expected_result",
        [
            pytest.param(
                0,
                0,
                [0, 0],
                id="zero ages"
            ),
            pytest.param(
                9,
                11,
                [0, 0],
                id="under 15 ages"
            ),
            pytest.param(
                15,
                15,
                [1, 1],
                id="equal 15 ages"
            ),
            pytest.param(
                16,
                20,
                [1, 1],
                id="between 15 and 24 ages"
            ),
            pytest.param(
                24,
                24,
                [2, 2],
                id="equal 24 ages"
            ),
            pytest.param(
                27,
                28,
                [2, 2],
                id="correct convert between 24 and 28 years "
            ),
            pytest.param(
                28,
                34,
                [3, 4],
                id="correct convert after 28 years "
            ),
            pytest.param(
                -28,
                -34,
                [0, 0],
                id="convert negative ages"
            ),
            pytest.param(
                300,
                500,
                [71, 97],
                id="convert large ages"
            ),
        ]
    )
    def test_get_human_ages(
            self,
            cat_age,
            dog_age,
            expected_result
    ):
        assert get_human_age(cat_age, dog_age) == expected_result
