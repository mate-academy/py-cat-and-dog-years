import pytest

from app.main import get_human_age


class TestGetHumanAge:
    @pytest.mark.parametrize(
        "cat_age,dog_age,result",
        [
            pytest.param(
                0, 0, [0, 0],
                id="should return zeroes when ages are 0"
            ),
            pytest.param(
                14, 14, [0, 0],
                id="should return zeroes when ages are 14"
            ),
            pytest.param(
                15, 15, [1, 1],
                id="should return [1, 1] when ages are 15"
            ),
            pytest.param(
                23, 23, [1, 1],
                id="should return [1, 1] when ages are 23"
            ),
            pytest.param(
                28, 28, [3, 2],
                id="should return [3, 2] when ages are 28"
            ),
            pytest.param(
                28, 29, [3, 3],
                id="should return [3, 3] when ages are 28 and 29"
            ),
        ]
    )
    def test_counts_ages_correctly(
            self,
            cat_age: int,
            dog_age: int,
            result: list
    ) -> None:
        assert get_human_age(cat_age, dog_age) == result
