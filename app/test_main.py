import pytest

from app import main


@pytest.mark.parametrize(
    ("cat_age", "dog_age", "expected", "expected_exception"),
    [
        (0, 0, [0, 0], None),
        (14, 14, [0, 0], None),
        (15, 15, [1, 1], None),
        (23, 23, [1, 1], None),
        (24, 24, [2, 2], None),
        (27, 27, [2, 2], None),
        (28, 28, [3, 2], None),
        (100, 100, [21, 17], None),
        (10_000, 10_000, [2496, 1997], None),
        (-1, -1, [0, 0], None),
        ("1", 1, None, TypeError),
        (1, "1", None, TypeError),
    ],
)
def test_get_human_age(
    cat_age: int | str,
    dog_age: int | str,
    expected: list[int] | None,
    expected_exception: type[Exception] | None,
) -> None:
    if expected_exception is not None:
        with pytest.raises(expected_exception):
            main.get_human_age(cat_age, dog_age)

        return

    assert main.get_human_age(cat_age, dog_age) == expected
