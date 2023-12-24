import pytest
from app.main import get_human_age


class TestGetHumanAge:
    @pytest.mark.parametrize(
        "cat_age, dog_age, human_age",
        [
            pytest.param(
                0,
                0,
                [0, 0],
                id="0 cat/dog years should convert into 0 human age"
            ),
            pytest.param(
                14,
                14,
                [0, 0],
                id="14 cat/dog years should convert into 0 human age"
            ),
            pytest.param(
                15,
                15,
                [1, 1],
                id="15 cat/dog years should convert into 1 human age"
            ),
            pytest.param(
                23,
                23,
                [1, 1],
                id="23 cat/dog years should convert into 1 human ages"
            ),
            pytest.param(
                24,
                24,
                [2, 2],
                id="24 cat/dog years should convert into 2 human ages"
            ),
            pytest.param(
                27,
                28,
                [2, 2],
                id="27 cat years and 28 dog years"
                   " should convert into 2 human ages"
            ),
            pytest.param(
                28,
                29,
                [3, 3],
                id="28 cat years and 29 dog years"
                   " should convert into 3 human ages"
            ),
            pytest.param(
                96,
                114,
                [20, 20],
                id="96 cat years and 114 dog years"
                   " should convert into 20 human ages"
            )
        ]

    )
    def test_calculating_ages_correctly(
            self,
            cat_age,
            dog_age,
            human_age
    ):
        assert get_human_age(cat_age, dog_age) == human_age
