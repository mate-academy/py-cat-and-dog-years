import pytest
from app.main import get_human_age

class TestGetHumanAge:
    @pytest.mark.parametrize(
        "cat_age, dog_age, expected",
        [
            pytest.param(
                0,
                0,
                [0, 0],
                id="zeros return zeros"
            ),
            pytest.param(
                14,
                14,
                [0, 0],
                id="14 cat/dog years should convert into 0 human age."
            ),
            pytest.param(
                15,
                15,
                [1, 1],
                id="[15 cat/dog years should convert into 1 human age."
            ),
            pytest.param(
                23,
                23,
                [1, 1],
                id="23 cat/dog years should convert into 1 human age."
            ),
            pytest.param(
                24,
                24,
                [2, 2],
                id="24 cat/dog years should convert into 2 human age."
            ),
            pytest.param(
                27,
                27,
                [2, 2],
                id="27 returns 2"
            ),
            pytest.param(
                28,
                28,
                [3, 2],
                id="28 returns 3 cat and 2 dog"
            ),
            pytest.param(
                28,
                28,
                [3, 2],
                id="any large number returns"
                   " cat and dog correctly"
            )
        ]
    )
    def test_get_human_age(self, cat_age, dog_age, expected):
        assert get_human_age(cat_age, dog_age) == expected