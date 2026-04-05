import pytest


from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, human_age",
    [
        pytest.param(
            0, 0, [0, 0],
            id="test should return zeroes"
        ),
        pytest.param(
            14, 14, [0, 0],
            id="test should return zeroes if 14"
        ),
        pytest.param(
            15, 15, [1, 1],
            id="test should return ones"
        ),
        pytest.param(
            23, 23, [1, 1],
            id="test should return ones if 23"
        ),
        pytest.param(
            24, 24, [2, 2],
            id="nine year increment"
        ),
        pytest.param(
            27, 27, [2, 2],
            id="test should return ones if 27"
        ),
        pytest.param(
            28, 28, [3, 2],
            id="test different increment"
        ),
        pytest.param(
            100, 100, [21, 17],
            id="test 100 year"
        )

    ]
)
def test_get_human_age(
        cat_age: int,
        dog_age: int,
        human_age: list[int]
) -> None:
    assert get_human_age(cat_age, dog_age) == human_age
