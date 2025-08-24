from app.main import get_human_age
import pytest


def test_should_return_list_with_len_equel_two() -> None:
    cat_age = 15
    dog_age = 15
    result = get_human_age(cat_age=cat_age, dog_age=dog_age)
    assert isinstance(result, list) and len(result) == 2


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
        (28, 29, [3, 3]),
        (32, 34, [4, 4]),
        (100, 100, [21, 17]),
        (1000, 1000, [246, 197])
    ]
)
def test_func_correct_translate_years(cat_age: int,
                                      dog_age: int,
                                      result: list[int]) -> None:
    assert get_human_age(cat_age=cat_age, dog_age=dog_age) == result


def test_input_negative_value() -> None:
    cat_age = -1
    dog_age = -5
    with pytest.raises(ValueError):
        get_human_age(cat_age=cat_age, dog_age=dog_age)


def test_input_incorrect_type_value() -> None:
    cat_age = "-1"
    dog_age = -5.8
    with pytest.raises(TypeError):
        get_human_age(cat_age=cat_age, dog_age=dog_age)
