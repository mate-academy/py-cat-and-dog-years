import pytest


from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age,dog_age,result",
    [
        pytest.param(
            0,
            0,
            [0, 0],
            id="should return zeros if value is 0"
        ),
        pytest.param(
            14,
            14,
            [0, 0],
            id="should return zeros if value is less than 15"
        ),
        pytest.param(
            15,
            15,
            [1, 1],
            id="should return 1 if age is equal to 15"
        ),
        pytest.param(
            16,
            16,
            [1, 1],
            id="should return whole number of age"
        ),
        pytest.param(
            1000,
            1000,
            [246, 197],
            id="should return correct age for big numbers"
        )
    ]
)
def test_should_correctly_konvert_age(
        cat_age: int,
        dog_age: int,
        result: list
) -> None:
    assert get_human_age(cat_age, dog_age) == result


@pytest.mark.parametrize(
    "cat_age,dog_age,expected_error",
    [
        pytest.param(
            -1,
            -2,
            ValueError,
            id="should raise 'ValueError' if age is less then 0"
        ),
        pytest.param(
            "cat",
            1.3,
            AttributeError,
            id="should raise 'AttributeError' if age's type is wrong"
        )
    ]
)
def test_should_correctly_raising_errors(
        cat_age: int,
        dog_age: int,
        expected_error: Exception
) -> None:
    with pytest.raises(expected_error):
        get_human_age(cat_age, dog_age)
