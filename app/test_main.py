import pytest
from app.main import get_human_age

@pytest.mark.parametrize(
    "cat_age, dog_age, expected_result",
    [
        pytest.param(0, 0, [0, 0], id="should_return_zero_for_ages_below_15"),
        pytest.param(14, 14, [0, 0], id="should_return_zero_for_ages_below_15"),
        pytest.param(15, 15, [1, 1], id="should_return_one_for_ages_15_to_23"),
        pytest.param(23, 23, [1, 1], id="should_return_one_for_ages_15_to_23"),
        pytest.param(24, 24, [2, 2], id="should_return_two_for_exactly_24"),
        pytest.param(28, 28, [3, 2], id="should_calculate_cat_and_dog_differently"),
        pytest.param(100, 100, [21, 17], id="should_handle_large_numbers"),
    ]
)
def test_get_human_age(cat_age, dog_age, expected_result):
    assert get_human_age(cat_age, dog_age) == expected_result


# def test_should_return_zero_for_14_and_below():
#     assert get_human_age(0,0) == [0, 0]
#     assert get_human_age(14,14) == [0, 0]
#
# def test_should_return_one_for_15_to_23():
#     assert get_human_age(15,15) == [1, 1]
#     assert get_human_age(23,23) == [1, 1]
#
#
# def test_should_return_two_for_24_and_above():
#     assert get_human_age(24,24) == [2, 2]
#
#
# def test_should_return_first_difference_in_ages():
#     assert get_human_age(28,28) == [3,2]
#
# def test_should_calculate_animal_ages_right():
#     assert get_human_age(100,100) == [21, 17]