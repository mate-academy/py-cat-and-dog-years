from app.main import get_human_age


def test_zero_age() -> None:
    assert get_human_age(0, 0) == [0, 0]


def test_less_than_first_threshold() -> None:
    assert get_human_age(14, 14) == [0, 0]


def test_exact_first_threshold() -> None:
    assert get_human_age(15, 15) == [1, 1]


def test_between_first_and_second_threshold() -> None:
    assert get_human_age(23, 23) == [1, 1]


def test_exact_second_threshold() -> None:
    assert get_human_age(24, 24) == [2, 2]


def test_cat_and_dog_have_different_step_growth() -> None:
    assert get_human_age(28, 28) == [3, 2]


def test_large_age_conversion() -> None:
    assert get_human_age(100, 100) == [21, 17]


def test_only_cat_ages() -> None:
    assert get_human_age(32, 0) == [4, 0]


def test_only_dog_ages() -> None:
    assert get_human_age(0, 29) == [0, 3]


def test_age_just_before_extra_growth() -> None:
    assert get_human_age(27, 28) == [2, 2]


def test_age_just_after_extra_growth() -> None:
    assert get_human_age(28, 29) == [3, 3]


def test_result_length_always_two() -> None:
    assert len(get_human_age(50, 50)) == 2
