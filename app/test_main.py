import pytest
from app.main import get_human_age


class TestMainModule:
    @pytest.mark.parametrize(
        "cat_age, dog_age, result",
        [
            pytest.param(
                0,
                0,
                [0, 0],
                id="Test"
            ),
            pytest.param(
                14,
                14,
                [0, 0],
                id="Test"
            ),
            pytest.param(
                15,
                15,
                [1, 1],
                id="Test"
            ),
            pytest.param(
                23,
                23,
                [1, 1],
                id="Test"
            ),
            pytest.param(
                24,
                24,
                [2, 2],
                id="Test"
            ),
            pytest.param(
                27,
                27,
                [2, 2],
                id="Test"
            ),
            pytest.param(
                28,
                28,
                [3, 2],
                id="Test"
            ),
            pytest.param(
                100,
                100,
                [21, 17],
                id="Test"
            ),
        ]
    )
    def test_module(self, cat_age: int, dog_age: int, result: list) -> None:
        assert get_human_age(cat_age, dog_age) == result
