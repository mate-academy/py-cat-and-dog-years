import pytest

from app.main import get_human_age


def test_type_of_output_should_be_a_list() -> None:
    assert isinstance(get_human_age(0, 0), list)


@pytest.mark.parametrize(
    "cat_age,dog_age,exception",
    [
        (10, "10", TypeError),
        ("10", 10, TypeError),
        (-1, 1, ValueError),
        (1, -1, ValueError),
    ],
)
def test_incorrect_values_raises_correcr_exception(
    cat_age: int | str,
    dog_age: int | str,
    exception: Exception
) -> None:
    with pytest.raises(exception):
        get_human_age(cat_age, dog_age)


@pytest.mark.parametrize(
    "cat_age,dog_age,expected_result",
    [
        (0, 0, [0, 0]),
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (23, 23, [1, 1]),
        (24, 24, [2, 2]),
        (27, 27, [2, 2]),
        (28, 28, [3, 2]),
        (100, 100, [21, 17]),
    ]
)
def test_get_human_age_mapping(
    cat_age: int,
    dog_age: int,
    expected_result: list[int]
) -> None:
    assert get_human_age(cat_age, dog_age) == expected_result
