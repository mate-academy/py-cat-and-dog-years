import pytest
from app.main import get_human_age


class TestGetHumanAge:
    @pytest.mark.parametrize(
        "cat_age, dog_age, human_age",
        [
            pytest.param(
                14, 14, [0, 0],
                id="should return 0 when cats and dogs age < 15"
            ),
            pytest.param(
                15, 15, [1, 1],
                id="15/15 cat/dog years should return 1 human year"
            ),
            pytest.param(
                23, 23, [1, 1],
                id="should return 1 when cats and dogs age < 24"
            ),
            pytest.param(
                24, 24, [2, 2],
                id="24/24 cat/dog years should return 2 human years"
            ),
            pytest.param(
                27, 28, [2, 2],
                id="27/28 cat/dog years should return 2 human years"
            ),
            pytest.param(
                27, 27, [2, 2],
                id="27/27 cat/dog years should return 2 human years"
            ),
            pytest.param(
                28, 28, [3, 2],
                id="28/28 cat/dog years should return 3/2 human years"
            ),
            pytest.param(
                28, 29, [3, 3],
                id="28/29 cat/dog years should return 3 human years"
            ),
            pytest.param(
                100, 100, [21, 17],
                id="100/100 cat/dog years should return expected human years"
            )
        ]
    )
    def test_calculate_human_age_correctly(
            self,
            cat_age: int,
            dog_age: int,
            human_age: list[int, int]
    ) -> None:
        assert get_human_age(cat_age, dog_age) == human_age
