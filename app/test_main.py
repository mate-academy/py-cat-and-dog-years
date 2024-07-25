import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, ages",
    [
        pytest.param(
            -14, -14, [0, 0],
            id="negative values"
        ),
        pytest.param(
            14, 14, [0, 0],
            id="less one year"
        ),
        pytest.param(
            15, 15, [1, 1],
            id="one year"
        ),
        pytest.param(
            23, 23, [1, 1],
            id="rounded to one year"
        ),
        pytest.param(
            24, 24, [2, 2],
            id="two years"
        ),
        pytest.param(
            27, 28, [2, 2],
            id="rounded to two years"
        ),
        pytest.param(
            28, 29, [3, 3],
            id="three years"
        ),
        pytest.param(
            31, 33, [3, 3],
            id="rounded to tree years"
        ),
        pytest.param(
            100, 100, [21, 17],
            id="large numbers"
        ),
    ]
)
def test_get_human_age(
    cat_age: int, dog_age: int, ages: list[int]

) -> None:
    assert get_human_age(cat_age, dog_age) == ages


@pytest.mark.parametrize(
    "cat_age, dog_age",
    [
        pytest.param(
            "cat", "dog",
            id="invalid type of params"
        ),
        pytest.param(
            None, 3,
            id="invalid type of params2"
        ),
        pytest.param(
            [4], 5,
            id="invalid type of params3"
        )
    ]
)
def test_should_raise_type_error_when_argument_is_not_integer(
    cat_age: int, dog_age: int
) -> None:
    with pytest.raises(TypeError):
        get_human_age(cat_age, dog_age)
