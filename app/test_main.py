from app.main import get_human_age
import pytest


@pytest.mark.parametrize(
    "cat_age,dog_age,human_age",
    [
        pytest.param(
            0,
            0,
            [0, 0],
            id="cat age and dot age equals 0"
        ),
        pytest.param(
            14,
            14,
            [0, 0],
            id="cat age and dot age less than 15"

        ),
        pytest.param(
            15,
            15,
            [1, 1],
            id="cat age and dot age equals 15"
        ),
        pytest.param(
            27,
            27,
            [2, 2],
            id="cat age and dot age equals 27"
        ),
        pytest.param(
            100,
            100,
            [21, 17],
            id="cat age and dot age equals 100"
        ),
    ]
)
def test_ages(
        cat_age: int,
        dog_age: int,
        human_age: int
) -> None:
    assert get_human_age(cat_age, dog_age) == human_age


@pytest.mark.parametrize(
    "cat_age,dog_age,expected_error",
    [
        pytest.param(
            -1,
            -1,
            ValueError,
            id="cat age and dot age less than -1",
        ),
        pytest.param(
            0.1,
            "hello",
            TypeError,
            id="cat age and dot age should be only int",
        ),
    ]
)
def test_ages_error(
        cat_age: int,
        dog_age: int,
        expected_error: Exception
) -> None:
    with pytest.raises(expected_error):
        get_human_age(cat_age, dog_age)
