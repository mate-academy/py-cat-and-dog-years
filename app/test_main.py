import pytest


from app.main import get_human_age


def test_should_return_zero_if_age_less_than_15() -> None:
    assert (get_human_age(14, 14) == [0, 0]
            ), "Should return zero if age less than 15"


@pytest.mark.parametrize(
    "cat_age, dog_age, result",
    [
        (15, 15, [1, 1]),
        (23, 23, [1, 1])
    ]
)
def test_should_return_one_if_age_in_15_23(
        cat_age: int, dog_age: int, result: list
) -> None:
    assert (
        get_human_age(cat_age, dog_age) == result
    ), "Should return one if age in (15-23)"


@pytest.mark.parametrize(
    "cat_age, dog_age, result",
    [
        (24, 24, [2, 2]),
        (27, 27, [2, 2])
    ]
)
def test_should_return_two_if_age_in_24_27(
        cat_age: int, dog_age: int, result: list
) -> None:
    assert (
        get_human_age(cat_age, dog_age) == result
    ), "Should return two if age in (24-27)"


@pytest.mark.parametrize(
    "cat_age, dog_age, result",
    [
        (100, 100, [21, 17]),
    ]
)
def test_should_correctly_work_with_large_numbers(
        cat_age: int, dog_age: int, result: list
) -> None:
    assert (
        get_human_age(cat_age, dog_age) == result
    ), "Should correctly work with large numbers"


@pytest.mark.parametrize(
    "cat_age, dog_age, result",
    [
        (-1, -1, [0, 0])
    ]
)
def test_should_return_zeros_if_age_is_less_than_zero(
        cat_age: int, dog_age: int, result: list
) -> None:
    assert (
        get_human_age(cat_age, dog_age) == result
    ), "Should return zero if age < 0"


@pytest.mark.parametrize(
    "cat_age,dog_age",
    [
        ([1], [1]),
        ((1,), (1,)),
        ({1}, {1}),
        ("1", "1"),
        (None, None)
    ]
)
def test_raise_errors_for_incorrect_type_of_age(
        cat_age: int, dog_age: int
) -> None:
    with pytest.raises(TypeError):
        get_human_age(cat_age, dog_age)
