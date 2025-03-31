import pytest
from app.main import get_human_age


@pytest.mark.parametrize(
    "cat, dog, result",
    [
        (0, 0, [0, 0]),
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (23, 23, [1, 1]),
        (24, 24, [2, 2]),
        (27, 27, [2, 2]),
        (28, 28, [3, 2]),
        (100, 100, [21, 17]),
    ],
    ids=[
        "1",
        "2",
        "3",
        "4",
        "5",
        "6",
        "7",
        "8",
    ],
)
def test_get_human_age(cat: int, dog: int, result: list) -> None:
    assert get_human_age(cat, dog) == result, (
        f"Human years {cat} and {dog} equal to {result}"
    )
