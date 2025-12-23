from app.main import get_human_age


def test_must_return_list() -> None:
    result = get_human_age(1, 1)
    assert isinstance(result, list)


def test_convert_age_into_human() -> None:
    result = get_human_age(0, 0)
    assert result == [0, 0]


def test_convert_first_age() -> None:
    result = get_human_age(14, 14)
    assert result == [0, 0]


def test_convert_next_age() -> None:
    result = get_human_age(23, 23)
    assert result == [1, 1]


def test_different_values_in_ages() -> None:
    result = get_human_age(0, 15)
    assert result == [0, 1]


def test_different_between_ages() -> None:
    result = get_human_age(100, 100)
    assert result == [21, 17]
