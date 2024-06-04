from app.main import get_human_age


def test_get_human_age() -> None:
    assert (
        get_human_age(0, 0) == [0, 0]
    ), "get_human_age(0, 0) should return [0, 0]"
    assert (
        get_human_age(14, 14) == [0, 0]
    ), "get_human_age(14, 14) should return [0, 0]"
    assert (
        get_human_age(15, 15) == [1, 1]
    ), "get_human_age(15, 15) should return [1, 1]"
    assert (
        get_human_age(23, 23) == [1, 1]
    ), "get_human_age(23, 23) should return [1, 1]"
    assert (
        get_human_age(24, 24) == [2, 2]
    ), "get_human_age(24, 24) should return [2, 2]"
    assert (
        get_human_age(27, 27) == [2, 2]
    ), "get_human_age(27, 27) should return [2, 2]"
    assert (
        get_human_age(28, 28) == [3, 2]
    ), "get_human_age(28, 28) should return [3, 2]"
    assert (
        get_human_age(100, 100) == [21, 17]
    ), "get_human_age(100, 100) should return [21, 17]"

    try:
        get_human_age(-1, -2)
    except ValueError:
        print("ValueError: get_human_age(-1, -2) should be with correct value")

    try:
        get_human_age("1", "3")
    except TypeError:
        print("TypeError: get_human_age('1', '3') should be int")
