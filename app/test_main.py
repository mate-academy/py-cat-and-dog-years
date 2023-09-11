from app.main import get_human_age


def test_get_human_age_0() -> None:
    assert get_human_age(0, 0) == [0, 0]


def test_get_human_age_15() -> None:
    assert get_human_age(15, 15) == [1, 1]


def test_get_human_age_28() -> None:
    assert get_human_age(28, 28) == [3, 2]


def test_get_human_age_100() -> None:
    assert get_human_age(100, 100) == [21, 17]


def test_no_one_or_all_values() -> None:
    try:
        assert get_human_age() == [0, 0]
    except TypeError:
        print("function take 2 parameters")


def test_another_type() -> None:
    try:
        assert get_human_age("13", "10") == [0, 0]
    except TypeError:
        print("False type")
