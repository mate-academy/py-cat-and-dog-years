from app.main import get_human_age


def test_function_should_return_list() -> None:
    assert isinstance(get_human_age(0, 0), list)


def test_should_return_list_size_2() -> None:
    assert len(get_human_age(0, 0)) == 2


def test_should_return_correct_parametrize() -> None:
    assert get_human_age(0, 0) == [0, 0]
    assert get_human_age(14, 14) == [0, 0]
    assert get_human_age(15, 15) == [1, 1]
    assert get_human_age(23, 23) == [1, 1]
    assert get_human_age(24, 24) == [2, 2]
    assert get_human_age(27, 27) == [2, 2]
    assert get_human_age(28, 28) == [3, 2]
    assert get_human_age(100, 100) == [21, 17]
