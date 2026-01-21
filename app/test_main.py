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
        (100, 100, [21, 17]),
        (15, 0, [1, 0]),
        (0, 15, [0, 1]),
    ]
)
def test_get_human_age_param(cat_age: int,
                             dog_age: int,
                             expected: list[int]) -> None:
    result = get_human_age(cat_age, dog_age)

    assert result == expected, (
        f"Expected get_human_age({cat_age}, "
        f"{dog_age}) to return {expected}, got {result}"
    )


def test_below_first_threshold() -> None:
    cat_human, _ = get_human_age(14, 0)
    assert cat_human == 0,\
        (f"For cat_age=14 (below first threshold), "
         f"expected human age 0, got {cat_human}")


def test_at_first_threshold() -> None:
    cat_human, _ = get_human_age(15, 0)
    assert cat_human == 1, (f"For cat_age=15 (at first threshold), "
                            f"expected human age 1, got {cat_human}")


def test_between_first_and_second_threshold() -> None:
    age = 15 + 9 - 1
    cat_human, _ = get_human_age(age, 0)
    assert cat_human == 1, (
        f"For cat_age={age} (just below second threshold), "
        f"expected human age 1, got {cat_human}"
    )


def test_at_second_threshold() -> None:
    age = 15 + 9
    cat_human, _ = get_human_age(age, 0)
    assert cat_human == 2,\
        (f"For cat_age={age} (at second threshold), "
         f"expected human age 2, got {cat_human}")


def test_return_type_and_length() -> None:
    result = get_human_age(10, 20)

    assert isinstance(result, list),\
        f"Return type should be list, got {type(result)}"
    assert len(result) == 2,\
        f"Return list should have length 2, got {len(result)}"
    assert all(isinstance(x, int) for x in result), (
        f"All elements in return list should be int, got "
        f"{[type(x) for x in result]}"
    )
