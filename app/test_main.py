from app.main import get_human_age
from pytest import mark


@mark.parametrize(
    "cat_age, dog_age, expected_list",
    [
        (0, 0, [0, 0]),
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (23, 23, [1, 1]),
        (24, 24, [2, 2]),
        (27, 27, [2, 2]),
        (28, 28, [3, 2]),
        (100, 100, [21, 17]),
        (-1, -1, [0, 0]),
    ]
)
def test_should_return_correct_list(
    cat_age: int,
    dog_age: int,
    expected_list: list
) -> None:
    assert get_human_age(cat_age, dog_age) == expected_list
