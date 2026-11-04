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
        (27, 27, [2, 2]),
        (28, 28, [3, 2]),
        (29, 29, [3, 3]),
        (32, 33, [4, 3]),
        (36, 39, [5, 5]),
        (100, 100, [21, 17]),
        (28, 24, [3, 2]),
        (24, 29, [2, 3]),
    ],
)
def test_get_human_age_returns_correct_result(
    cat_age: int,
    dog_age: int,
    expected: list[int],
) -> None:
    result = get_human_age(cat_age, dog_age)

    assert result == expected
    assert len(result) == 2
    assert all(isinstance(age, int) for age in result)


@pytest.mark.parametrize(
    "cat_age, dog_age",
    [
        (-1, 0),
        (0, -1),
        (-1, -1),
        (-15, 20),
        (20, -15),
    ],
)
def test_get_human_age_rejects_negative_values(
    cat_age: int,
    dog_age: int,
) -> None:
    with pytest.raises(ValueError):
        get_human_age(cat_age, dog_age)


@pytest.mark.parametrize(
    "cat_age, dog_age",
    [
        ("15", 15),
        (15, "15"),
        ("cat", 15),
        (15, "dog"),
        (None, 15),
        (15, None),
        (15.5, 20),
        (20, 15.5),
    ],
)
def test_get_human_age_rejects_invalid_types(
    cat_age: object,
    dog_age: object,
) -> None:
    with pytest.raises(TypeError):
        get_human_age(cat_age, dog_age)
