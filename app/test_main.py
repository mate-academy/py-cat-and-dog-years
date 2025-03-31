from app.main import get_human_age
import pytest


@pytest.mark.parametrize(
    "cat_age, dog_age, expected_result",
    [
        (0, 0, [0, 0]),
        (-1, 0, [0, 0]),
        (0, -1, [0, 0]),
        (1_000_018, 1, [250_000, 0]),
        (1, 1_000_018, [0, 200_000]),
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (23, 23, [1, 1]),
        (24, 24, [2, 2]),
        (27, 27, [2, 2]),
        (28, 28, [3, 2]),
        (29, 29, [3, 3]),
        (100, 100, [21, 17])
    ]
)
def test_get_human_age(cat_age: int, dog_age: int,
                       expected_result: list[int]) -> None:
    assert get_human_age(cat_age, dog_age) == expected_result


@pytest.mark.parametrize(
    "cat_age, dog_age, exception",
    [
        ("0", 3, TypeError),
        (1, "3", TypeError)
    ]
)
def test_get_human_age_raises_exceptions(
        cat_age: int, dog_age: int,
        exception: type(BaseException)) -> None:
    with pytest.raises(exception):
        get_human_age(cat_age, dog_age)
