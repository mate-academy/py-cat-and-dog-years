import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, expected_result",
    [
        pytest.param(
            14, 14, [0, 0],
            id="should return [0, 0] when ages are less than first_year"
        ),
        pytest.param(
            15, 15, [1, 1],
            id="should return [1, 1] when ages are equal to first_year"
        ),
        pytest.param(
            23, 23, [1, 1],
            id=("should return [1, 1] when ages are less than \
                first_year + second_year")
        ),
        pytest.param(
            24, 24, [2, 2],
            id="should return [2, 2] when ages are equal to \
                first_year + second_year"
        ),
        pytest.param(
            27, 27, [2, 2],
            id="should return [2, 2] when ages less than \
                first_year + second_year + each_year"
        ),
        pytest.param(
            28, 28, [3, 2],
            id="should return [3, 2] when the cat's age is equal \
                first_year + second_year + each_year \
                and the dog's age is less than \
                first_year + second_year + each_year"
        ),
        pytest.param(
            29, 29, [3, 3],
            id="should return [3, 3] when ages are greater or equal to \
                first_year + second_year + each_year"
        ),
        pytest.param(
            80, 80, [16, 13],
            id="should return [16, 13] when ages are greater than \
                first_year + second_year + each_year"
        )
    ]
)
def test_should_return_correct_result(
    cat_age: int, dog_age: int, expected_result: list[int]
) -> None:
    assert get_human_age(cat_age, dog_age) == expected_result


@pytest.mark.parametrize(
    "cat_age, dog_age, expected_error",
    [
        pytest.param(
            "15", 30, TypeError,
            id="should raise TypeError when age is str"
        ),
        pytest.param(
            27, [12], TypeError,
            id="should raise TypeError when age is list"
        ),
        pytest.param(
            12, {"23": 23}, TypeError,
            id="should raise TypeError when age is dict"
        ),
        pytest.param(
            {34}, 3, TypeError,
            id="should raise TypeError when age is set"
        )
    ]
)
def test_should_raise_correct_exception(
    cat_age: int,
    dog_age: int,
    expected_error: type[Exception]
) -> None:
    with pytest.raises(expected_error):
        get_human_age(cat_age, dog_age)
