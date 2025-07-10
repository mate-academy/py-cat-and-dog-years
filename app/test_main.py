import pytest
from app.main import get_human_age


class TestGetHumanAge:
    @pytest.mark.parametrize(
        "cat_age,dog_age,expected",
        [
            pytest.param(
                0,
                0,
                [0, 0],
                id="both zero age"
            ),
            pytest.param(
                14,
                14,
                [0, 0],
                id="both under the first human_year"
            ),
            pytest.param(
                15,
                15,
                [1, 1],
                id="both at the end of the first human_year"
            ),
            pytest.param(
                23,
                23,
                [1, 1],
                id="both at the second human_year"
            ),
            pytest.param(
                24,
                24,
                [2, 2],
                id="both at the end of the second human_year"
            ),
            pytest.param(
                27,
                27,
                [2, 2],
                id="both at the third human_year"
            ),
            pytest.param(
                28,
                28,
                [3, 2],
                id="cat enters the third human_year"
            ),
            pytest.param(
                100,
                100,
                [21, 17],
                id="large ages"
            )
        ]
    )
    def test_get_human_age_different_ages(
            self,
            cat_age: int,
            dog_age: int,
            expected: list
    ) -> None:

        assert get_human_age(cat_age, dog_age) == expected
