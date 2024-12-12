from app.main import get_human_age
import pytest


# def test_get_human_age_for_zeros_in_years() -> None:
#     result = get_human_age(0, 0)
#     expected_result = [0, 0]
#     assert result == expected_result
#
#
# def test_get_human_age_24_cat_years_2_human() -> None:
#     result = get_human_age(24, 24)
#     expected_result = [2, 2]
#     assert result == expected_result
#
#
# def test_get_human_age_15_cat_years_1_human() -> None:
#     result = get_human_age(15, 15)
#     expected_result = [1, 1]
#     assert result == expected_result
#
#
# def test_get_human_age_23_cat_years_1_human() -> None:
#     result = get_human_age(23, 23)
#     expected_result = [1, 1]
#     assert result == expected_result
#
#
# def test_get_human_age_28_cat_3_human_29_dog_3_human() -> None:
#     resultt = get_human_age(28, 29)
#     expected_result = [3, 3]
#     assert resultt == expected_result
#
#
# def test_get_human_age_14_cat_years_1_human() -> None:
#     result = get_human_age(14, 14)
#     expected_result = [0, 0]
#     assert result == expected_result


@pytest.mark.parametrize(
    "cat_age, dog_age, expected_result",
    [
        (0, 0, [0, 0]),
        (24, 24, [2, 2]),
        (15, 15, [1, 1]),
        (23, 23, [1, 1]),
        (28, 29, [3, 3]),
        (14, 14, [0, 0])
    ]
)
def test_get_human_age(cat_age: int,
                       dog_age: int,
                       expected_result: int) -> None:
    result = get_human_age(cat_age, dog_age)
    assert result == expected_result
    f"Expected {expected_result}, but got {result}"
