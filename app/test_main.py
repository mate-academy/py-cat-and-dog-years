from app.main import get_human_age
import pytest


@pytest.mark.parametrize(
    "cat_age,dog_age",
    [
        (None, 10),
        ("1", 10),
    ]
)
def test_raise_error_if_some_value_is_incorrect(
        cat_age: int,
        dog_age: int
) -> None:
    with pytest.raises(TypeError):
        get_human_age(cat_age, dog_age)


@pytest.mark.parametrize(
    "cat_age,dog_age,result",
    [
        (0, 0, [0, 0]),
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (23, 23, [1, 1]),
        (24, 24, [2, 2]),
        (27, 27, [2, 2]),
        (28, 28, [3, 2]),
        (100, 100, [21, 17],)
    ]
)
def test_should_correctly_calculate_correct_inputs(
        cat_age: int,
        dog_age: int,
        result: list
) -> None:
    assert get_human_age(cat_age, dog_age) == result


if __name__ == "__main__":
    pass
