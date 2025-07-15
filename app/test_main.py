from app.main import get_human_age

# write your code here
def test_must_return_list():
    result = get_human_age(1,1)
    assert isinstance(result, list)


def test_convert_age_into_human():
    result = get_human_age(0,0)
    assert result == [0, 0]


def test_convert_first_age():
    result = get_human_age(14,14)
    assert result == [0, 0]


def test_convert_next_age():
    result = get_human_age(23,23)
    assert result == [1, 1]


def test_different_values_in_ages():
    result = get_human_age(0, 15)
    assert result == [0, 1]


def test_different_between_ages():
    result = get_human_age(100,100)
    assert result == [21, 17]