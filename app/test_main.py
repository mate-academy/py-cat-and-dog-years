import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, expected_ages",
    [
        pytest.param(
            14,
            14,
            [0, 0],
            id="get zeros when ages are under 15"
        ),
        pytest.param(
            15,
            15,
            [1, 1],
            id="test when ages are equal 15"
        ),
        pytest.param(
            23,
            17,
            [1, 1],
            id="test when ages are between 15 and 24"
        ),
        pytest.param(
            24,
            24,
            [2, 2],
            id="test when ages are equal 24"
        ),
        pytest.param(
            28,
            28,
            [3, 2],
            id="test when ages are equal 28"
        ),
        pytest.param(
            44,
            44,
            [7, 6],
            id="test if function works for third+ year"
        ),
        pytest.param(
            -10,
            -5,
            [0, 0],
            id="test function with negative numbers"
        ),
        pytest.param(
            0,
            0,
            [0, 0],
            id="test function with zero numbers"
        ),
        pytest.param(
            100,
            150,
            [21, 27],
            id="test function with large numbers"
        )
    ]
)
def test_get_correct_answers(
        cat_age: int,
        dog_age: int,
        expected_ages: list[int]
) -> None:
    assert get_human_age(cat_age, dog_age) == expected_ages


@pytest.mark.parametrize(
    "cat_age, dog_age, expected_error",
    [
        pytest.param(
            1.6, "6.0", TypeError,
            id="Throws error if one of ages isn't integer"
        ),
        pytest.param(
            (10, 20), (10, 20), TypeError,
            id="Throws error if takes tuple"
        ),
        pytest.param(
            [10, 20], [10, 20], TypeError,
            id="Throws error if takes list"
        ),
        pytest.param(
            {"cat": 10, "dog": 20}, {"cat": 10, "dog": 20}, TypeError,
            id="Throws error if takes dict"
        )
    ]
)
def test_if_function_throws_errors(
        cat_age: int,
        dog_age: int,
        expected_error: Exception
) -> None:
    with pytest.raises(expected_error):
        get_human_age(cat_age, dog_age)
