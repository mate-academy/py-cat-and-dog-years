from app.main import get_human_age


def test_result_should_be_two_integers():
    result = get_human_age(22, 22)
    assert isinstance(result[0], int) and isinstance(result[1], int), \
        "Results should be two integers."


def test_should_be_zero_when_less_then_fifteen():
    result = get_human_age(13, 12)
    assert result == [0, 0], "Result should be 0 when less than fifteen."


def test_should_return_diff_human_age():
    result = get_human_age(28, 28)
    assert result[0] != result[1], "Human ages should be different."
