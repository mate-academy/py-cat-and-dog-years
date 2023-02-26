import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age,dog_age",
    [
        (0, 0),
        (14, 14)
    ]
)
def test_first_15_years_give_1_human_year(
        cat_age: int, dog_age: int
) -> None:
    assert get_human_age(cat_age, dog_age) == [0, 0]


@pytest.mark.parametrize(
    "cat_age,dog_age",
    [
        (15, 15),
        (23, 23)
    ]
)
def test_next_9_years_give_1_more_human_year(
        cat_age: int, dog_age: int
) -> None:
    assert get_human_age(cat_age, dog_age) == [1, 1]


@pytest.mark.parametrize(
    "cat_age,dog_age,result",
    [
        (24, 24, [2, 2]),
        (27, 27, [2, 2]),
        (28, 28, [3, 2]),
        (100, 100, [21, 17])
    ]
)
def test_every_4_and_5_years_give_an_extra_human_year(
        cat_age: int, dog_age: int, result: list[int]
) -> None:
    assert get_human_age(cat_age, dog_age) == result


@pytest.mark.parametrize(
    "cat_age,dog_age,result",
    [
        (0, 0, [0, 0]),
        (-1, -1, [0, 0]),
        (1000, 10000, [246, 1997])
    ]
)
def test_input_out_of_range(
        cat_age: int, dog_age: int, result: list[int]
) -> None:
    assert get_human_age(cat_age, dog_age) == result


@pytest.mark.parametrize(
    "cat_age,dog_age",
    [
        pytest.param("string", 0, id="string"),
        pytest.param([1], 0, id="list"),
        pytest.param({1}, 0, id="dict")
    ]
)
def test_type_error_exception(cat_age: int, dog_age: int) -> None:
    with pytest.raises(TypeError):
        get_human_age(cat_age, dog_age)
