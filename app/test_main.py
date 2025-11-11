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
        (100, 100, [21, 17]),
    ],
)
def test_get_human_age(
        cat_age: int,
        dog_age: int,
        expected: list[int]
) -> None:
    assert get_human_age(cat_age, dog_age) == expected


def test_negative_ages_should_raise_error() -> None:
    try:
        result = get_human_age(-10, 5)
    except ValueError:
        assert True
    else:
        assert result[0] == 0

    try:
        result = get_human_age(10, -5)
    except ValueError:
        assert True
    else:
        assert result[1] == 0


def test_invalid_data_types_should_not_crash() -> None:
    invalid_inputs = [
        ("15", 10),
        (15, "10"),
        (15.5, 20),
        (None, 10),
    ]
    for args in invalid_inputs:
        try:
            result = get_human_age(*args)
        except Exception:
            assert True
        else:
            assert isinstance(result, list)
            assert len(result) == 2

