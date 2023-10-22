import pytest
from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, human_age",
    [
        pytest.param(
            15, 15, [1, 1],
        ),
        pytest.param(
            21, 26, [1, 2],
        ),
        pytest.param(
            28, 28, [3, 2],
        ),
        pytest.param(
            -2, 0, [0, 0],
        ),
        pytest.param(
            10.5, 23.5, [0, 1],
        )
    ]
)
def test_get_human_age(
        cat_age: int,
        dog_age: int,
        human_age: int
) -> None:
    assert get_human_age(cat_age, dog_age) == human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, error",
    [
        pytest.param(
            (16,), {"age": 24}, TypeError,
        ),
        pytest.param(
            "10", "40", TypeError,
        )
    ]
)
def test_get_human_age_arguments_type(
        cat_age: int,
        dog_age: int,
        error: Exception
) -> None:
    with pytest.raises(error):
        get_human_age(cat_age, dog_age)
