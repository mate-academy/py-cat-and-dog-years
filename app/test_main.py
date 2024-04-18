import pytest
from app.main import get_human_age


class TestForGetHumanAge:
    @pytest.mark.parametrize(
        "cat_age, dog_age, human_age",
        [
            pytest.param(-1, -2, [0, 0], id="-1, -2 should [0, 0]"),
            pytest.param(0, 0, [0, 0], id="0, 0 should [0, 0]"),
            pytest.param(14, 14, [0, 0], id="14, 14 should [0, 0]"),
            pytest.param(15, 15, [1, 1], id="15, 15 should [1, 1]"),
            pytest.param(23, 23, [1, 1], id="23, 23 should [1, 1]"),
            pytest.param(24, 24, [2, 2], id="24, 24 should [2, 2]"),
            pytest.param(27, 27, [2, 2], id="27, 27 should [2, 2]"),
            pytest.param(28, 28, [3, 2], id="28, 28 should [3, 2]"),
            pytest.param(100, 100, [21, 17], id="100, 100 should [21, 17]"),
        ]
    )
    def test_args(self, cat_age: any, dog_age: any, human_age: any) -> None:
        assert get_human_age(cat_age, dog_age) == human_age
