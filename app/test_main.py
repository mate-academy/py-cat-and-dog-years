from app.main import get_human_age

# write your code here
def test_return_a_list_and_correct_len_and_data_is_int() -> None:
    result = get_human_age(0 , 0)
    assert result == [0, 0]

def test_limit_age_more_15_years() -> None:
    result = get_human_age(15, 15)
    assert result == [1, 1]

def test_if_not_more_than_23() -> None:
    result = get_human_age(23, 23)
    assert result == [1, 1]

def test_limit_age_over_24_years() -> None:
    result = get_human_age(24, 24)
    assert result == [2, 2]

def test_count_the_right_step() -> None:
    result = get_human_age(28, 28)
    assert result == [3, 2]