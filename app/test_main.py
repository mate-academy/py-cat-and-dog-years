import pytest


from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age ,dog_age, result",
    [
        (0, 0, [0, 0]),
        (14, 14, [0, 0])
    ]
)
def test_under_fourteen_should_be_zero(
        cat_age: int,
        dog_age: int,
        result: list[int]
) -> None:
    assert get_human_age(cat_age, dog_age) == result


@pytest.mark.parametrize(
    "cat_age ,dog_age ,result",
    [
        (15, 15, [1, 1]),
        (23, 23, [1, 1])
    ]
)
def test_over_fourteen_under_tw_five_should_be_zero(
        cat_age: int,
        dog_age: int,
        result: list[int]
) -> None:
    assert get_human_age(cat_age, dog_age) == result


@pytest.mark.parametrize(
    "cat_age ,dog_age ,result",
    [
        (28, 28, [3, 2]),
        (29, 29, [3, 3]),
        (33, 33, [4, 3])
    ]
)
def test_over_tw_eight_cats_and_dogs_may_differ(
        cat_age: int,
        dog_age: int,
        result: list[int]
) -> None:
    assert get_human_age(cat_age, dog_age) == result
