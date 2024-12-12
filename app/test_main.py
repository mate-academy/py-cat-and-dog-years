from app.main import get_human_age
# import pytest


def test_get_human_age_for_zeros_in_years() -> None:
    result = get_human_age(0, 0)
    expexted_result = [0, 0]
    assert result == expexted_result


def test_get_human_age_24_cat_years_2_human() -> None:
    resultt = get_human_age(24, 24)
    expextedd_result = [2, 2]
    assert resultt == expextedd_result


def test_get_human_age_15_cat_years_1_human() -> None:
    resultt = get_human_age(15, 15)
    expextedd_result = [1, 1]
    assert resultt == expextedd_result


def test_get_human_age_23_cat_years_1_human() -> None:
    resultt = get_human_age(23, 23)
    expextedd_result = [1, 1]
    assert resultt == expextedd_result


def test_get_human_age_28_cat_3_human_29_dog_3_human() -> None:
    resultt = get_human_age(28, 29)
    expextedd_result = [3, 3]
    assert resultt == expextedd_result


def test_get_human_age_14_cat_years_1_human() -> None:
    resultt = get_human_age(14, 14)
    expextedd_result = [0, 0]
    assert resultt == expextedd_result


# @pytest.mark.parametrize(
#     "cat_age, dog_age, expected_result",
#     [
#         (0, 0, [0, 0]),
#         (24, 24, [2, 2]),
#         (15, 15, [1, 1]),
#         (23, 23, [1, 1]),
#         (28, 29, [3, 3]),
#         (14, 14, [0, 0])
#     ]
# )
# def test_get_human_age(cat_age, dog_age, expected_result):
#     result = get_human_age(cat_age, dog_age)
#     assert result == expected_result,
#     f"Expected {expected_result}, but got {result}"
