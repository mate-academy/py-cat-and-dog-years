import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat, dog, result",
    [
        (pytest.param(23, 23, [1, 1], id="should convert into 1 human age")),
        (pytest.param(24, 24, [2, 2], id="should convert into 2 human age")),
        (0, 0, [0, 0]),
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (27, 27, [2, 2]),
        (28, 28, [3, 2]),
        (100, 100, [21, 17]),
        (30, 120, [3, 21])

    ]
)
def test_should_convert_into_human_age(
        cat: int,
        dog: int,
        result: list
) -> None:
    assert get_human_age(cat, dog) == result


@pytest.mark.parametrize(
    "cat, dog, expected_error",
    [
        pytest.param(-1, -1, ValueError, id="should not be less then 0"),
    ]
)
def test_less_then_0(
        cat: int,
        dog: int,
        expected_error: str
) -> None:
    with pytest.raises(expected_error):
        get_human_age(cat, dog)
