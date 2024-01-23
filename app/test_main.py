import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, result",
    [
        (-100, -50, [0, 0]),
        (28, 29, [3, 3]),
        (24, 24, [2, 2]),
        (0, 0, [0, 0]),
        (23, 27, [1, 2]),
        (50, 50, [8, 7])
    ]
)
def test_data_input(cat_age: int, dog_age: int, result: list) -> None:
    assert (
        get_human_age(cat_age, dog_age) == result
    ), f"Result of {cat_age} and {dog_age} should be {result}."


def test_wrong_type_of_instance() -> None:
    with pytest.raises(TypeError):
        get_human_age("cat", "dog")
