from app.main import get_human_age


def test_if_the_age_is_0() -> None:
    age = get_human_age(0, 0)

    assert age == [0, 0]


def test_if_age_less_then_15_then_convert_to_0() -> None:
    age = get_human_age(14, 14)

    assert age == [0, 0]


def test_if_age_more_then_15_then_convert_to_1() -> None:
    age = get_human_age(15, 15)

    assert age == [1, 1]


def test_if_age_less_then_24_then_convert_to_1() -> None:
    age = get_human_age(23, 23)

    assert age == [1, 1]


def test_if_age_more_then_24_then_convert_to_2() -> None:
    age = get_human_age(24, 24)

    assert age == [2, 2]


def test_if_age_less_then_28_and_29_then_convert_to_2() -> None:
    age = get_human_age(27, 28)

    assert age == [2, 2]


def test_if_age_more_then_28_and_29_then_convert_to_3() -> None:
    age = get_human_age(28, 29)

    assert age == [3, 3]


def test_if_the_age_is_negative() -> None:
    age = get_human_age(-15, -15)

    assert age == [0, 0]
