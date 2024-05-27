import pytest
from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age,dog_age,human_age",
    [
        pytest.param(
            14,
            10,
            [0, 0],
            id="return zeros if age less than 15"),
        pytest.param(
            23,
            23,
            [1, 1],
            id="add 1 for 15 years"),
        pytest.param(
            27,
            28,
            [2, 2],
            id="add 1 for 24 years"),
        pytest.param(
            28,
            0,
            [3, 0],
            id="add 1 for next 4 cat years"),
        pytest.param(
            0,
            29,
            [0, 3],
            id="add 1 for next 5 dog years"),
        pytest.param(
            100,
            100,
            [21, 17],
            id="100 cat years should not be equal 100 dog years"),
    ]
)
def test_convert_to_human_age(
        cat_age: int,
        dog_age: int,
        human_age: list) -> None:
    assert get_human_age(cat_age, dog_age) == human_age
