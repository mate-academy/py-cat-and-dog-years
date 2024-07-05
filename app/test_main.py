import pytest
from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, expected",
    [
        (0, 0, [0, 0]),
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (23, 23, [1, 1]),
        (24, 24, [2, 2]),
        (28, 28, [3, 2]),
    ],
)
def test_get_human_age(cat_age: int, dog_age: int, expected: list) -> bool:
    assert get_human_age(cat_age, dog_age) == expected


@pytest.mark.parametrize(
    "cat_age, dog_age, expected",
    [
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (23, 23, [1, 1]),
        (24, 24, [2, 2]),
        (27, 27, [2, 2]),
        (28, 28, [3, 2]),
        (32, 32, [4, 3]),
        (33, 33, [4, 3]),
    ],
)
def test_edge_cases(cat_age: int, dog_age: int, expected: list) -> bool:
    assert get_human_age(cat_age, dog_age) == expected


def test_large_numbers() -> bool:
    assert get_human_age(1000, 1000) == [246, 197]


@pytest.mark.parametrize(
    "cat_age, dog_age",
    [
        ("15", 15),
        (15, "15"),
        (None, 15),
        (15, None),
        (15.5, 15),
        (15, 15.5),
    ],
)
def test_incorrect_types(cat_age: int, dog_age: int) -> bool:
    try:
        result = get_human_age(cat_age, dog_age)
        if isinstance(cat_age, float):
            assert (
                result[0] == get_human_age(int(cat_age), dog_age)[0]
            ), "Failed on float cat age"
        if isinstance(dog_age, float):
            assert (
                result[1] == get_human_age(cat_age, int(dog_age))[1]
            ), "Failed on float dog age"
    except Exception as e:
        assert isinstance(
            e, (TypeError, ValueError)
        ), f"Unexpected exception type: {type(e)}"
    else:
        if not isinstance(cat_age, (int, float)) or not isinstance(
            dog_age, (int, float)
        ):
            assert False, "Expected exception not raised for non-numeric types"
