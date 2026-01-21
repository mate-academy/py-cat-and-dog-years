from app.main import get_human_age
import pytest


@pytest.mark.parametrize(
    "cat_age, dog_age, real_result",
    [
        (0, 0, [0, 0]),
        (14, 14, [0 ,0]),
        (15, 15, [1, 1]),
        (23, 23, [1, 1]),
        (24, 24, [2, 2]),
        (27, 27, [2, 2]),
        (28, 28, [3, 2]),
        (100, 100, [21, 17]),
    ],
    ids=[
        "test_zero_years",
        "test_years_post_first_animal_first_year",
        "test_years_first_animal_year",
        "test_years_post_first_animal_second_year",
        "test_years_second_year",
        "test_years_last_time_together_two_years",
        "test_years_firs_only_cat_third_year"
        "test_years_100_years_old",
    ]
)
def test_get_human_age(cat_age: int, dog_age, real_result: int) -> None:
    assert get_human_age(cat_age, dog_age) == real_result
#
# def test_zero_years() -> None:
#     assert get_human_age(0, 0) == [0, 0]
#
#
# def test_years_post_first_animal_first_year() -> None:
#     assert get_human_age(14, 14) == [0, 0]
#
#
# def test_years_first_animal_year() -> None:
#     assert get_human_age(15, 15) == [1, 1]
#
#
# def test_years_post_first_animal_second_year() -> None:
#     assert get_human_age(23, 23) == [1, 1]
#
#
# def test_years_second_year() -> None:
#     assert get_human_age(24, 24) == [2, 2]
#
#
# def test_years_last_time_together_two_years() -> None:
#     assert get_human_age(27, 27) == [2, 2]
#
#
# def test_years_firs_only_cat_third_year() -> None:
#     assert get_human_age(28, 28) == [3, 2]
#
#
# def test_years_100_years_old() -> None:
#     assert get_human_age(100, 100) == [21, 17]
