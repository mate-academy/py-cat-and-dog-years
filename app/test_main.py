import pytest

from app.main import get_human_age


def test_should_return_list_with_two_values() -> None:
    assert (
        isinstance(get_human_age(1, 1), list)
        and len(get_human_age(1, 1)) == 2
    ), f"must return list but was {type(get_human_age(1, 1))}"


def test_should_return_integers_numbers_in_list() -> None:
    assert (
        isinstance(num, int) for num in get_human_age(30, 30)
    ), "human age must be integer"


@pytest.mark.parametrize(
    "cat_years,dog_years,expected_result",
    [
        (14, 14, [0, 0]),
        (23, 23, [1, 1]),
        (25, 27, [2, 2]),
        (44, 51, [7, 7]),
        (521, 1077, [126, 212])
    ],
    ids=[
        "14 cats and 14 dogs years must convert to 0, 0 humans years",
        "23 cats and 23 dogs years must convert to 1, 1 humans years",
        "25 cats and 27 dogs years must convert to 2, 2 humans years",
        "44 cats and 51 dogs years must convert to 7, 7 humans years",
        "521 cats and 1077 dogs years must convert to 126, 212 humans years"
    ]
)
def test_should_return_expected_result_for_each_param(
    cat_years: int,
    dog_years: int,
    expected_result: list[int]
) -> None:
    assert (
        get_human_age(cat_years, dog_years) == expected_result
    ), f"must return {expected_result} when years is {cat_years, dog_years}"
