import pytest
from app.main import get_human_age


@pytest.mark.parametrize(
    "cat, dog, expected",
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
)
def test_get_human_age_valid_cases(cat: int, dog: int, expected: list[int]) -> None:
    assert get_human_age(cat, dog) == expected


def test_return_type_and_structure() -> None:
    result = get_human_age(24, 24)
    assert isinstance(result, list)
    assert len(result) == 2
    assert all(isinstance(x, int) for x in result)


@pytest.mark.parametrize(
    "cat, dog",
    [
        (-1, 5),       # negativo gato
        (5, -1),       # negativo cachorro
        (-3, -3),      # ambos negativos
        (3.5, 5),      # float
        ("5", 5),      # string
        (None, 5),     # None
    ],
)
def test_invalid_inputs(cat, dog) -> None:
    with pytest.raises((TypeError, ValueError)):
        get_human_age(cat, dog)
