import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age,dog_age,expected_result",
    [
        pytest.param(
            0,
            0,
            [0, 0],
            id="test should return zeros when arguments are 0"
        ),
        pytest.param(
            14,
            14,
            [0, 0],
            id="test should return zeros when arguments are under 15"
        ),
        pytest.param(
            15,
            15,
            [1, 1],
            id="test should return 1 when arguments are 15"
        ),
        pytest.param(
            23,
            23,
            [1, 1],
            id="test should return 1 when arguments are 23"
        ),
        pytest.param(
            24,
            24,
            [2, 2],
            id="test should return 2 when arguments are 24"
        ),
        pytest.param(
            100,
            100,
            [21, 17],
            id="test should return result with large arguments"
        )
    ]
)
def test_of_get_human_age(
        cat_age: int,
        dog_age: int,
        expected_result: list) -> None:
    assert get_human_age(cat_age, dog_age) == expected_result


def test_should_return_error_when_arguments_are_nan() -> None:
    with pytest.raises(TypeError):
        get_human_age([4], "4")
