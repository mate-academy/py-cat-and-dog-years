import pytest

from app.main import get_human_age


test_cases = [
    (-1, -2, [0, 0]),
    (0, 0, [0, 0]),
    (14, 14, [0, 0]),
    (15, 15, [1, 1]),
    (23, 23, [1, 1]),
    (24, 24, [2, 2]),
    (27, 27, [2, 2]),
    (28, 28, [3, 2]),
    (100, 100, [21, 17])
]


@pytest.mark.parametrize("cat_age, dog_age, expected_result", test_cases)
def test_get_human_age(
        cat_age: int,
        dog_age: int,
        expected_result: list
) -> None:
    assert get_human_age(cat_age, dog_age) == expected_result


@pytest.mark.parametrize(
    "cat_age, dog_age,"
    "result",
    [
        pytest.param(
            1,
            None,
            TypeError,
            id="should return `TypeError` when parameter is empty"
        ),
        pytest.param(
            "2",
            2,
            TypeError,
            id="should return `TypeError` when parameter is not int"
        )
    ]
)
def test_no_one_or_all_values(
        cat_age: int,
        dog_age: int,
        result: Exception
) -> None:
    with pytest.raises(result):
        get_human_age(cat_age, dog_age)
