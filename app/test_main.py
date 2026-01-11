from app.main import get_human_age
import pytest


@pytest.mark.parametrize(
    "cat_age,dog_age,human_age",
    [
        pytest.param(28, 28, [3, 2], id="default test 28"),
        pytest.param(27, 27, [2, 2], id="default test 27"),
        pytest.param(23, 23, [1, 1], id="default test 23"),
        pytest.param(14, 14, [0, 0], id="default test 14"),
    ]
)
def test_works_correctly(
        cat_age: int,
        dog_age: int,
        human_age: list[int]) -> None:
    assert get_human_age(cat_age, dog_age) == human_age
