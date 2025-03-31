import pytest
from app.main import get_human_age


@pytest.mark.parametrize("cat_age, dog_age, expected", [
    (0, 0, [0, 0]),
    (14, 14, [0, 0]),
    (15, 15, [1, 1]),
    (23, 23, [1, 1]),
    (24, 24, [2, 2]),
    (27, 27, [2, 2]),
    (28, 28, [3, 2]),
    (100, 100, [21, 17])
])
def test_get_human_age(
        cat_age: int,
        dog_age: int,
        expected: list[int]
) -> None:
    assert get_human_age(cat_age, dog_age) == expected


@pytest.mark.parametrize("cat_age, dog_age, expected", [
    ("ten", 15, [0, 1]),
    (15, "fifteen", [1, 0]),
    (10.5, 15, [0, 1]),
    (10, 15.5, [0, 1]),
    (None, 15, [0, 1]),
    (10, None, [0, 0])
])
def test_get_human_age_invalid_types(
        cat_age: int,
        dog_age: int,
        expected: list[int]
) -> None:
    try:
        result = get_human_age(cat_age, dog_age)
        assert result == expected, (
            f"Expected {expected} but got {result} for cat_age={cat_age}"
            f" and dog_age={dog_age}"
        )
    except TypeError:
        pass
    except Exception as e:
        assert False, f"Expected TypeError but got different exception: {e}"


@pytest.mark.parametrize("cat_age, dog_age, expected", [
    (-10, 15, [0, 1]),
    (10, -15, [0, 0]),
    (-10, -15, [0, 0])
])
def test_get_human_age_negative_values(
        cat_age: int,
        dog_age: int,
        expected: list[int]
) -> None:
    result = get_human_age(cat_age, dog_age)
    assert result == expected, (
        f"Expected {expected} but got {result} for cat_age={cat_age}"
        f" and dog_age={dog_age}"
    )


@pytest.mark.parametrize("cat_age, dog_age", [
    (10 ** 6, 10 ** 6),
    (10 ** 12, 10 ** 12)
])
def test_get_human_age_large_values(cat_age: int, dog_age: int) -> None:
    result = get_human_age(cat_age, dog_age)
    assert isinstance(result, list)
    assert len(result) == 2
    assert all(isinstance(x, int) for x in result)
