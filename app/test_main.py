from app.main import get_human_age
import pytest


@pytest.mark.parametrize(
    "cat_age,dog_age,result",
    [
        (0, 0, [0, 0]),
        (5, 6, [0, 0]),
        (3, 2, [0, 0]),
        (7, 7, [0, 0]),
        (9, 5, [0, 0]),
        (10, 0, [0, 0]),
        (11, 8, [0, 0]),
        (2, 4, [0, 0]),

    ],
)
def test_should_be_add_zero(cat_age: int, dog_age: int, result: list) -> None:
    assert get_human_age(cat_age, dog_age) == result


@pytest.mark.parametrize(
    "cat_age,dog_age,result",
    [
        (65, 24, [12, 2]),
        (87, 6, [17, 0]),
        (90, 15, [18, 1]),
        (54, 74, [9, 12]),
        (61, 65, [11, 10]),
        (28, 28, [3, 2]),
        (21, 29, [1, 3]),
        (27, 27, [2, 2]),

    ],
)
def test_should_convert_age_into_human_age(
        cat_age: int,
        dog_age: int,
        result: list
) -> None:
    assert get_human_age(cat_age, dog_age) == result


@pytest.mark.parametrize(
    "cat_age,dog_age,result",
    [
        (15, 18, [1, 1]),
        (16, 23, [1, 1]),
        (19, 21, [1, 1]),
        (23, 20, [1, 1]),
        (17, 17, [1, 1]),
        (20, 22, [1, 1]),
        (21, 16, [1, 1]),
        (18, 19, [1, 1]),

    ],
)
def test_should_convert_age_into_one_human_age(
        cat_age: int,
        dog_age: int,
        result: list
) -> None:
    assert get_human_age(cat_age, dog_age) == result
