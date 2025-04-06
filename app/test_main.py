from app.main import get_human_age
import pytest


class TestGetHumanAge:
    @pytest.mark.parametrize(
        "cat_age, dog_age, result",
        [
            pytest.param(0, 0, [0, 0],
                         id="returns zeroes for zero ages"),
            pytest.param(14, 14, [0, 0],
                         id="returns zeroes for ages below 15"),
            pytest.param(23, 23, [1, 1],
                         id="returns ones for ages between 15 and 24"),
            pytest.param(27, 27, [2, 2],
                         id="calculates next years correctly"),
            pytest.param(28, 28, [3, 2],
                         id="calculates next years correctly"),
            pytest.param(100, 100, [21, 17],
                         id="returns correct human age for 100"),
        ]
    )
    def test_modify_class_correctly(self,
                                    cat_age: int,
                                    dog_age: int,
                                    result: list) -> None:
        assert get_human_age(cat_age, dog_age) == result
