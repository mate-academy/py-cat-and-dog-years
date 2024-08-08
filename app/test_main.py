import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, result",
    [
        pytest.param(
            0,
            0,
            [0, 0],
            id="should return zeros when inputs are zeros"
        ),
        pytest.param(
            14,
            14,
            [0, 0],
            id="should return zeros when inputs less then fifteen"
        ),
        pytest.param(
            15,
            15,
            [1, 1],
            id="should return ones when inputs are fifteen"
        ),
        pytest.param(
            23,
            23,
            [1, 1],
            id="should return ones when inputs are less then twenty four"
        ),
        pytest.param(
            24,
            24,
            [2, 2],
            id="should return twos when inputs are equal to twenty four"
        ),
        pytest.param(
            28,
            28,
            [3, 2],
            id="should return three for cat and \
                four for dog when inputs are twenty-eight"
        ),
        pytest.param(
            100,
            100,
            [21, 17],
            id="should return 21 for cat and \
                17 for dog when inputs are one hundred"
        ),
    ]
)
def test_correct_human_year_result(
    cat_age: int,
    dog_age: int,
    result: list[int]
) -> None:
    assert get_human_age(cat_age, dog_age) == result, "Incorrect years convert"
