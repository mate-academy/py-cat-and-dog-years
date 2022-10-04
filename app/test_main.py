from app.main import get_human_age
import pytest


class TestDogAge:
    @pytest.mark.parametrize(
        "cat, dog, human",
        [
            (0, 0, [0, 0]),
            (15, 15, [1, 1]),
            (24, 24, [2, 2]),
            (28, 28, [3, 2]),
            (100, 100, [21, 17]),
        ]
    )
    def test_dog_age(self, cat, dog, human):
        assert get_human_age(cat, dog) == human
