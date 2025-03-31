import pytest
from app.main import get_human_age


@pytest.mark.parametrize(
    "cat, dog, expected_result",
    [
        (0, 0, [0, 0]),
        (14, 14, [0, 0]),
        (24, 24, [2, 2]),
        (28, 28, [3, 2]),
        (-15, -15, [0, 0]),
        (1000, 2000, [246, 397]),
    ]
)
def test_get_human_age(cat: int, dog: int, expected_result: list) -> None:
    assert get_human_age(cat, dog) == expected_result


def test_non_integer_input() -> None:
    with pytest.raises(TypeError):
        get_human_age("c", "d")
