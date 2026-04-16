from app.main import get_human_age
import pytest


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
        (100, 100, [21, 17])
    ]
)
def test_result_value_must_be_correct(cat_age: int,
                                      dog_age: int, result: list) -> None:
    assert (
        get_human_age(cat_age, dog_age) == result
    ), f"Cat age: {cat_age}, Dog age: {dog_age}, return: \
# {get_human_age(cat_age, dog_age)} should be: {result}"


@pytest.mark.parametrize(
    "cat_age,dog_age",
    [
        ("test", 23),
        (24, "two"),
        ("eight", "ten"),
        (0.5, 1),
        (1, 0.5),
        (0.5, 1.5)
    ]
)
def test_validate_type_value_error(cat_age: int,
                                   dog_age: int) -> None:
    with pytest.raises(ValueError, match="Type Value Error"):
        get_human_age(cat_age, dog_age)


@pytest.mark.parametrize(
    "cat_age,dog_age",
    [
        (-1, 1),
        (1, -5),
        (-6, -6)
    ]
)
def test_validate_range_value_error(cat_age: int,
                                    dog_age: int) -> None:
    with pytest.raises(ValueError, match="Negative Value Error"):
        get_human_age(cat_age, dog_age)
