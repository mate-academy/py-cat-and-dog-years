import pytest
from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age,dog_age,result",
    [
        (0, 0, [0, 0]),
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
    ],
    ids=["two zeroes", "14, 14", "15, 15"]
)
def test_if_value_returned_is_int(
        cat_age: int, dog_age: int, result: list[int, int]) -> None:
    assert get_human_age(cat_age, dog_age) == result


@pytest.mark.parametrize(
    "cat_age,dog_age,result",
    [
        (-50, -50, [0, 0]),
        (0, 0, [0, 0]),
        (23, 23, [1, 1]),
        (24, 24, [2, 2]),
        (27, 27, [2, 2]),
        (28, 28, [3, 2]),
        (1000, 1000, [246, 197])
    ],
    ids=["-50, -50", "0, 0",
         "23, 23", "24, 24", "27, 27", "28, 28", "1000, 1000"]
)
def test_if_result_changes_at_edge_values(
        cat_age: int, dog_age: int, result: list[int, int]) -> None:
    assert get_human_age(cat_age, dog_age) == result


def test_if_function_raises_type_error_with_incorrect_type_data() -> None:
    cat_age = "10"
    dog_age = "20"
    with pytest.raises(TypeError):
        get_human_age(cat_age, dog_age)
