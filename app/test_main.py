import pytest
from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, human_age",
    [
        pytest.param(
            -1, -1, [0, 0],
            id="negative should be zeros"
        ),
        pytest.param(
            0, 0, [0, 0],
            id="zeros should be zeros"
        ),
        pytest.param(
            14, 14, [0, 0],
            id="less than 14 should be zeros"
        ),
        pytest.param(
            15, 15, [1, 1],
            id="between 15 and 23 ages should be equal 1"
        ),
        pytest.param(
            23, 23, [1, 1],
            id="between 15 and 23 ages should be equal 1"
        ),
        pytest.param(
            24, 24, [2, 2],
            id="between 24 and 28 ages should be equal 2"
        ),
        pytest.param(
            27, 27, [2, 2],
            id="between 24 and 28 ages should be equal 2"
        ),
        pytest.param(
            28, 28, [3, 2],
            id="28 human age should be 3 and 2 for dog and cat"
        ),
        pytest.param(
            100, 100, [21, 17],
            id="100 human years should be 21 and 17 years for dog and cat"
        )
    ]
)
def test_human_ages(
        cat_age: int,
        dog_age: int,
        human_age: list[int]
) -> None:
    assert get_human_age(cat_age=cat_age, dog_age=dog_age) == human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, error",
    [
        pytest.param(
            "0", 0, TypeError,
            id="str should create TypeError"
        ),
        pytest.param(
            None, None, TypeError,
            id="None should create TypeError"
        )
    ]
)
def test_ages_types_exceptions(cat_age: int, dog_age: int, error: type(TypeError)) -> None:
    with pytest.raises(error):
        get_human_age(cat_age, dog_age)
