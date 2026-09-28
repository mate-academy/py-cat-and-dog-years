import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age,dog_age,expected_error",
    [
        pytest.param(
            5.5,
            15,
            TypeError,
            id="check if `cat_age` is float"
        ),
        pytest.param(
            15,
            5.5,
            TypeError,
            id="check if `dog_age` is float"
        ),
        pytest.param(
            "50",
            15,
            TypeError,
            id="check if `cat_age` is string"
        ),
        pytest.param(
            15,
            "15",
            TypeError,
            id="check if `dog_age` is string"
        ),
        pytest.param(
            -20,
            15,
            ValueError,
            id="check if `cat_age` is less than 0"
        ),
        pytest.param(
            20,
            -20,
            ValueError,
            id="check if `dog_age` is less than 0"
        )
    ]
)
def test_should_raise_errors_correctly(
        cat_age: int,
        dog_age: int,
        expected_error: BaseException
) -> None:
    with pytest.raises(expected_error):
        get_human_age(cat_age, dog_age)


@pytest.mark.parametrize(
    "cat_age,dog_age,result",
    [
        (0, 0, [0, 0]),
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (23, 23, [1, 1]),
        (24, 24, [2, 2]),
        (27, 27, [2, 2]),
        (28, 28, [3, 2]),
        (100, 100, [21, 17]),
    ]
)
def test_should_return_list_with_correct_cat_and_dog_ages(
        cat_age: int,
        dog_age: int,
        result: list
) -> None:
    assert get_human_age(cat_age, dog_age) == result
