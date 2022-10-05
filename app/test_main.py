from app.main import get_human_age
import pytest


class TestDogAge:
    @pytest.mark.parametrize(
        "cat, dog, human",
        [
            pytest.param(
                0, 0, [0, 0],
                id="Human must be equal to zero if cat/dog 0 - 14]"
            ),
            pytest.param(
                15, 15, [1, 1],
                id="Human must be equal to [1, 1] if cat/dog 15"
            ),
            pytest.param(
                24, 24, [2, 2],
                id="Human must be to [2, 2] if cat/dog 24"
            ),
            pytest.param(
                28, 28, [3, 2],
                id="Human must be [3, 2] when cat/dog 28"
            ),
            pytest.param(
                100, 100, [21, 17],
                id="Human must be [21, 17] when cat/dog 100"
            ),
        ]
    )
    def test_dog_age(self, cat: int, dog: int, human: list[int]) -> None:
        assert get_human_age(cat, dog) == human