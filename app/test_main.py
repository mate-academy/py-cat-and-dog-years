import pytest
from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, result",
    [
        (-1, -7, [0, 0]),
        (0, 0, [0, 0]),
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (23, 23, [1, 1]),
        (24, 24, [2, 2]),
        (27, 27, [2, 2]),
        (28, 28, [3, 2]),
        (100, 100, [21, 17])
    ],
    ids=[
        "negative age",
        "cat, dog age are 0",
        "cat, dog age are less than 1 human year",
        "cat, dog age are exactly 1 human year",
        "cat, dog are 1 pet year away from 2 human years",
        "cat, dog age are exactly 2 human years",
        "cat is 1 pet year from 3 human years",
        "cat, dog age are same, but different human age",
        "cat, dog age are same, very old, more difference in human age"
    ]
)
def test_function_outputs_correct_result(
        cat_age: int,
        dog_age: int,
        result: list
) -> None:
    assert get_human_age(cat_age, dog_age) == result


def test_function_input_correct_type() -> None:
    with pytest.raises(TypeError):
        get_human_age("42", 42)
    with pytest.raises(TypeError):
        get_human_age(42, "42")
