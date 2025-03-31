import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age,dog_age,result",
    [
        pytest.param(
            13,
            13,
            [0, 0],
            id="should return zero if age less than first year"
        ),
        pytest.param(
            23,
            23,
            [1, 1],
            id="should return one if age less than first and second year"
        ),
        pytest.param(
            27,
            27,
            [2, 2],
            id="should return two if cat age more than twenty four but less than twenty eight"
        ),
        pytest.param(
            28,
            28,
            [3, 2],
            id="should return two if dog age more than twenty four but less than twenty nine"
        ),
        pytest.param(
            100,
            100,
            [21, 17],
            id="should return result according to formulas for cat and dog"
        ),
    ]
)
def test_return_relevant_value(cat_age: int, dog_age: int, result: list) -> None:
    assert get_human_age(cat_age, dog_age) == result


@pytest.mark.parametrize(
    "cat_age,dog_age,expected_error",
    [
        pytest.param(
            -1,
            -1,
            ValueError,
            id="should raise error if negative value"
        ),
        pytest.param(
            150,
            150,
            ValueError,
            id="should raise error if extremely large values"
        ),
    ]

)
def test_raising_errors_properly(
    cat_age: int,
    dog_age: int,
    expected_error
) -> None:
    with pytest.register_assert_rewrite(expected_error):
        get_human_age(cat_age, dog_age)

# def test_should_return_zero_if_age_less_than_first_year() -> None:
#     assert get_human_age(13, 13) == [0, 0]
#
#
# def test_should_return_one_if_age_less_than_first_and_second_year() -> None:
#     assert get_human_age(23, 23) == [1, 1]
#
#
# def test_should_return_two_if_cat_age_more_than_twentyfour_but_less_than_twenty_eight() -> None:
#     assert get_human_age(27, 27) == [2, 2]
#
#
# def test_should_return_two_if_dog_age_more_than_twentyfour_but_less_than_twenty_nine() -> None:
#     assert get_human_age(28, 28) == [3, 2]
#
#
# def test_should_return_result_according_to_formulas_for_cat_and_dog() -> None:
#     assert get_human_age(100, 100) == [21, 17]
