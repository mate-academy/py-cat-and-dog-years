from app.main import get_human_age
import pytest


@pytest.mark.parametrize("animal_age, human_age", [
    ((14, 14), [0, 0]),
    ((15, 15), [1, 1]),
    ((23, 23), [1, 1]),
    ((24, 24), [2, 2]),
    ((27, 28), [2, 2]),
    ((28, 29), [3, 3]),
    ((100, 100), [21, 17]),
    ((0, 0), [0, 0])
])
def test_specific_animal_ages(animal_age: int, human_age: list) -> None:
    assert get_human_age(*animal_age) == human_age


def test_if_input_is_correct() -> None:
    with pytest.raises(TypeError):
        get_human_age("9", [11])
