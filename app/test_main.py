import pytest
from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_ages,dog_ages,result",
    [
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (23, 23, [1, 1]),
        (24, 24, [2, 2]),
        (27, 27, [2, 2]),
        (28, 28, [3, 2]),
        (100, 100, [21, 17])

    ]
)
def test_should_return_correct_data(
        cat_ages,
        dog_ages,
        result
) -> None:
    assert (
        get_human_age(cat_ages, dog_ages) == result
    )


@pytest.mark.parametrize(
    "cat_ages,dog_ages,expected_error",
    [
        ("21", 23, TypeError),
        (23, "23", TypeError),
        ([45, 67], {25}, TypeError),
        ({"23": 24}, "", TypeError),
    ]
)
def test_raising_errors(
        cat_ages,
        dog_ages,
        expected_error
) -> None:
    with pytest.raises(expected_error):
        get_human_age(cat_ages, dog_ages)
