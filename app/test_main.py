from app.main import get_human_age
import pytest


@pytest.mark.parametrize(
    "cat_age, dog_age, result",
    [
        pytest.param(0, 0, [0, 0],
                     id="age boundaries equal to 0 if 0 year old"),
        pytest.param(14, 14, [0, 0],
                     id="age boundaries equal to 0 if 14 years old"),
        pytest.param(15, 15, [1, 1],
                     id="age boundaries equal to 1 if 15 years old"),
        pytest.param(23, 23, [1, 1],
                     id="age boundaries equal to 1 if 23 years old"),
        pytest.param(24, 24, [2, 2],
                     id="age boundaries equal to 2 if 24 years old"),
        pytest.param(27, 27, [2, 2],
                     id="age boundaries equal to 2 if 27 years old"),
        pytest.param(28, 28, [3, 2],
                     id="age boundaries equal to 3 and 2 dog years if 28"),
        pytest.param(100, 100, [21, 17],
                     id="age boundaries equal to [21, 17] if 100 years old")
    ]
)
def test_get_human_age(
        cat_age: int,
        dog_age: int,
        result: list
) -> None:
    assert get_human_age(cat_age, dog_age) == result


def test_rejects_negative_age() -> None:
    with pytest.raises(ValueError):
        get_human_age(-1, -1)


def test_rejects_invalid_types() -> None:
    with pytest.raises(TypeError):
        get_human_age("15", "15")
