from app.main import get_human_age,convert_to_human


def test_should_check_arguments_function_less_than_15():
    assert get_human_age(0,0) == [0, 0]


def test_should_check_arguments_function_between_15_and_24():
    assert get_human_age(15, 17) == [1, 1]


def test_should_check_arguments_function_more_24():
    assert get_human_age(28, 28) == [3, 2]
