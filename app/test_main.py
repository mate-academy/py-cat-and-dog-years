from app.main import get_human_age
import pytest


@pytest.mark.parametrize(
    "cat_age, dog_age, expected",
    [
        (0, 0, [0, 0]),
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (23, 23, [1, 1]),
        (24, 24, [2, 2]),
        (27, 27, [2, 2]),
        (28, 28, [3, 2]),
        (29, 29, [3, 3]),
        (100, 100, [21, 17]),
    ],
    ids=[
        "zero age",
        "just below first year",
        "exactly first year",
        "just below second year",
        "exactly second year",
        "remainder is discarded",
        "cat gets extra year, dog doesn't",
        "dog gets extra year",
        "big age",
    ],
)
def test_converts_age_correctly(
        cat_age: int, dog_age: int, expected: list[int]
) -> None:
    assert get_human_age(cat_age, dog_age) == expected


def test_negative_age_returns_zero() -> None:
    assert get_human_age(-1, -1) == [0, 0]


def test_very_big_age() -> None:
    assert get_human_age(10**6, 10**6) == [249996, 199997]


@pytest.mark.parametrize(
    "cat_age, dog_age",
    [
        ("14", 4),
        (None, 34),
        ([16], 20)
    ]
)
def test_raises_type_error_for_wrong_types(cat_age: int, dog_age: int) -> None:
    with pytest.raises(TypeError):
        get_human_age(cat_age, dog_age)
