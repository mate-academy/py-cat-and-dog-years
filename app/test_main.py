from app.main import get_human_age
import pytest


class TestCatandDogYear:
    @pytest.mark.parametrize(
        "cat_age, dog_age, human_age",
        [
            pytest.param(0, 0, [0, 0]),
            pytest.param(14, 14, [0, 0]),
            pytest.param(15, 15, [1, 1]),
            pytest.param(23, 23, [1, 1]),
            pytest.param(24, 24, [2, 2]),
            pytest.param(27, 27, [2, 2]),
            pytest.param(28, 28, [3, 2]),
            pytest.param(100, 100, [21, 17]),
        ]
    )
    def test_prime(self, cat_age: int, dog_age: int, human_age: int) -> None:
        assert get_human_age(cat_age, dog_age) == human_age
