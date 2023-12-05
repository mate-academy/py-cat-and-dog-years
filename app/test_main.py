import pytest
from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, result",
    [
        pytest.param(
            -1,
            -1,
            [0, 0],
            id="should return the wright result 0 and 0"
        ),
        pytest.param(
            0,
            0,
            [0, 0],
            id="should return the wright result: 0 and 0"
        ),
        pytest.param(
            14,
            14,
            [0, 0],
            id="should return 0 human age"
        ),
        pytest.param(
            15,
            15,
            [1, 1],
            id="should return the wright result: human age 1 and 1"
        ),
        pytest.param(
            23,
            23,
            [1, 1],
            id="should return the wright result: human age 1 and 1"
        ),
        pytest.param(
            24,
            24,
            [2, 2],
            id="should return the wright result: human age 2 and 2"
        ),
        pytest.param(
            27,
            28,
            [2, 2],
            id="should return the wright result: human age 2 and 2"
        ),
        pytest.param(
            28,
            29,
            [3, 3],
            id="should return the wright result: human age 3 and 3"
        ),
        pytest.param(
            100000,
            100000,
            [24996, 19997],
            id="should return the wright result: human age "
               "for cat 24996 and 19997 for dog"
        ),
    ]
)
def test_calculation_correctly(
        cat_age: int,
        dog_age: int,
        result: list[int]
) -> None:
    assert get_human_age(cat_age, dog_age) == result


@pytest.mark.parametrize(
    "cat_age, dog_age, expected_error",
    [
        pytest.param(
            "2",
            "3",
            TypeError,
            id="should raise error if cat or dog age is string type"
        ),

    ]
)
def test_raising_error_correctly(
        cat_age: int | str,
        dog_age: int | str,
        expected_error: Exception,
) -> None:
    with pytest.raises(expected_error):
        get_human_age(cat_age, dog_age)
