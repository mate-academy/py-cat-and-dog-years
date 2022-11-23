from app.main import get_human_age


def test_years_should_be_integers() -> None:
    result = get_human_age(50, 50)
    assert isinstance(result[0], int) and isinstance(result[1], int)


def test_if_result_values_are_correct() -> None:
    assert get_human_age(88, 88) == [18, 14]
