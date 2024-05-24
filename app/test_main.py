import pytest


from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_to_human, dog_to_human, expected",
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
def test_get_human_age_return_result_correctly(
        cat_to_human: int,
        dog_to_human: int,
        expected: list) -> None:
    assert get_human_age(cat_to_human, dog_to_human) == expected


@pytest.mark.parametrize(
    "cat_age, dog_age, expected_exception",
    [
        ("0", "14", TypeError),
        (None, None, TypeError),
        ([1, 1], [2, 3], TypeError),
    ]
)
def test_get_human_age_for_type(
        cat_age: int,
        dog_age: int,
        expected_exception: type[Exception]) -> None:
    with pytest.raises(expected_exception):
        get_human_age(cat_age, dog_age)
