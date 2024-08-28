import pytest
from app.main import get_human_age


class TestHumanAgeFunction:
    @pytest.mark.parametrize(
        "cat_age, dog_age, result",
        [
            pytest.param(14, 14, [0, 0], id="function should return 0"),
            pytest.param(15, 15, [1, 1], id="function should return 1"),
            pytest.param(28, 29, [3, 3], id="function should return 3"),
            pytest.param(23, 23, [1, 1], id="function should return 1"),
            pytest.param(24, 24, [2, 2], id="function should return 2"),
            pytest.param(27, 28, [2, 2], id="function should return 2")
        ]
    )
    def test_is_human_age_right(self,
                                cat_age: int,
                                dog_age: int,
                                result: list) -> None:
        assert get_human_age(cat_age, dog_age) == result
