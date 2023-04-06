import pytest
from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age,dog_age,result",
    [
        (14, 14, [0, 0]),
        (23, 23, [1, 1]),
        (24, 24, [2, 2]),
        pytest.param(
            0,
            0,
            [0, 0],
            id="must work with 0"
        ),
        pytest.param(
            -1,
            -4,
            [0, 0],
            id="must work with negative"
        ),
        pytest.param(
            15,
            4355,
            [1, 868],
            id="must work with large"
        ),
        pytest.param(
            10.0,
            15.0,
            [0, 1],
            id="must work with float"
        )
    ]
)
def test_checking_the_right_age(cat_age: int,
                                dog_age: int,
                                result: list[int]) -> None:
    assert get_human_age(cat_age, dog_age) == result
