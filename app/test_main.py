from app.main import get_human_age


def test_zero_age() -> None:
    assert get_human_age(0, 0) == [0, 0]


def test_just_below_first_threshold() -> None:
    assert get_human_age(14, 14) == [0, 0]


def test_exact_first_threshold() -> None:
    assert get_human_age(15, 15) == [1, 1]


def test_just_below_second_threshold() -> None:
    assert get_human_age(23, 23) == [1, 1]


def test_exact_second_threshold() -> None:
    assert get_human_age(24, 24) == [2, 2]


def test_near_cat_extra_human_year() -> None:
    assert get_human_age(27, 27) == [2, 2]


def test_cat_crosses_extra_human_year() -> None:
    assert get_human_age(28, 28) == [3, 2]


def test_large_ages() -> None:
    assert get_human_age(100, 100) == [21, 17]


def test_asymmetric_ages() -> None:
    assert get_human_age(28, 15) == [3, 1]
    assert get_human_age(15, 28) == [1, 2]


def test_output_format() -> None:
    result = get_human_age(20, 20)
    assert isinstance(result, list)
    assert len(result) == 2
    assert all(isinstance(x, int) for x in result)
