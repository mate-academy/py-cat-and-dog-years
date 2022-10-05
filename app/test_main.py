from app.main import get_human_age
import pytest


@pytest.mark.parametrize(
    "cat, dog, human",
    [
        pytest.param(
            0, 0, [0, 0],
            id="Human age should be [0, 0] when cat and dog ages is 0"
        ),
        pytest.param(
            15, 15, [1, 1],
            id="Human age should be [1, 1] when cat and dog ages is 0"
        ),
        pytest.param(
            23, 23, [1, 1],
            id="Human age should be [1, 1] when cat and dog ages is 23"
        ),
        pytest.param(
            28, 28, [3, 2],
            id="Human age should be [3, 2] when cat and dog ages is 28"
        ),
        pytest.param(
            100, 100, [21, 17],
            id="Human age should be [21, 17] when cat and dog ages is 100",
        ),
    ],
)
def test_dog_age(cat: int, dog: int, human: list[int]) -> None:
    assert get_human_age(cat, dog) == human
