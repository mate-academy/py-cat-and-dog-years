import pytest

from app.main import get_human_age


class TestGetHumanAge:
    @pytest.mark.parametrize(
        "cat_age,dog_age,ages",
        [
            pytest.param(
                -5, -15, [0, 0],
                id="negative values"
            ),
            pytest.param(
                0, 0, [0, 0],
                id="zero values"
            ),
            pytest.param(
                14, 14, [0, 0],
                id="less one year"
            ),
            pytest.param(
                15, 15, [1, 1],
                id="one year"
            ),
            pytest.param(
                23, 23, [1, 1],
                id="rounded to one year"
            ),
            pytest.param(
                28, 29, [3, 3],
                id="three years"
            ),
            pytest.param(
                31, 33, [3, 3],
                id="rounded to tree years"
            ),
            pytest.param(
                1765, 1653, [437, 327],
                id="big and not rounded years"
            ),
        ]
    )
    def test_get_human_age_correctly(
            self,
            cat_age: int,
            dog_age: int,
            ages: list[int]
    ) -> None:
        assert get_human_age(cat_age, dog_age) == ages
