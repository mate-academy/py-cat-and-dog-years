import pytest
from app.main import get_human_age


class TestGetHumanAge:
    @pytest.mark.parametrize(
        "cat_age,dog_age,human_ages",
        [
            pytest.param(
                -1,
                -15,
                [0, 0],
                id="negative numbers should return zero human year"
            ),
            pytest.param(
                0,
                0,
                [0, 0],
                id="zero years should return zero human year"
            ),
            pytest.param(
                14,
                14,
                [0, 0],
                id="4 years should return zero human years"
            ),
            pytest.param(
                15,
                15,
                [1, 1],
                id="zero years should return zero human year"
            ),
            pytest.param(
                23,
                23,
                [1, 1],
                id="under second milestone discards remainder"
            ),
            pytest.param(
                24,
                24, [2, 2],
                id="twenty four years should return two human years"
            ),
            pytest.param(27, 0, [2, 0], id="cat remainder handling"),
            pytest.param(
                27,
                27,
                [2, 2],
                id="27 years should return 2 human year"
            ),
            pytest.param(
                28,
                27,
                [3, 2],
                id="28 and 27 years should return 3 and 3 human years"
            ),
            pytest.param(0, 28, [0, 2], id="dog remainder handling"),
            pytest.param(28, 0, [3, 0], id="cat scaling after 24"),
            pytest.param(0, 29, [0, 3], id="dog scaling after 24"),
            pytest.param(
                40,
                44,
                [6, 6],
                id="both animals scaling simultaneously"
            ),
            pytest.param(
                100,
                100,
                [21, 17],
                id="100 years should return 21 and 17 human years"
            ),
        ]
    )
    def test_returns_correct_age(
            self,
            cat_age: int,
            dog_age: int,
            human_ages: list[int]
    ) -> None:
        assert get_human_age(cat_age, dog_age) == human_ages
