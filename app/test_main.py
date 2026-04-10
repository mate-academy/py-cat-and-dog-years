import pytest
from app.main import get_human_age


@pytest.mark.parametrize(
    "cat, dog, expected",
    [
        (23, 23, [1, 1]),
        (24, 24, [2, 2]),
        (27, 27, [2, 2]),
        (28, 28, [3, 2]),
        (-1, 10, [0, 0]),
    ],
)
def test_get_human_age_edges(
    cat: int, dog: int, expected: list[int]
) -> None:
    assert get_human_age(cat, dog) == expected


def test_get_human_age_wrong_type() -> None:
    with pytest.raises(TypeError):
        get_human_age("15", 15)

    with pytest.raises(TypeError):
        get_human_age(15, 15.5)
