from app.main import get_human_age


def test_for_return_type() -> None:
    result = get_human_age(15, 15)
    assert isinstance(result, list)


def test_for_zero_values() -> None:
    result = get_human_age(0, 0)
    assert result == [0, 0]


def test_for_results() -> None:
    result = get_human_age(28, 28)
    assert result == [3, 2]
