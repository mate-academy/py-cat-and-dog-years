from app.main import get_human_age


def test_zero_years() -> None:
    assert get_human_age(0, 0) == [0, 0], \
        ("Cat and dog ages should be 0 in human years "
         "when they are 0 in their own years")


def test_fourteen_years() -> None:
    assert get_human_age(14, 14) == [0, 0], \
        ("Cat and dog ages should be 0 in human years "
         "when they are 14 in their own years")


def test_fifteen_years() -> None:
    assert get_human_age(15, 15) == [1, 1], \
        ("Cat and dog ages should be 1 in human years "
         "when they are 15 in their own years")


def test_twenty_three_years() -> None:
    assert get_human_age(23, 23) == [1, 1], \
        ("Cat and dog ages should be 1 in human years "
         "when they are 23 in their own years")


def test_twenty_four_years() -> None:
    assert get_human_age(24, 24) == [2, 2], \
        ("Cat and dog ages should be 2 in human years "
         "when they are 24 in their own years")


def test_twenty_seven_years() -> None:
    assert get_human_age(27, 27) == [2, 2], \
        ("Cat and dog age should be 2 in human years "
         "when they are 27 in their own years")


def test_twenty_eight_years() -> None:
    assert get_human_age(28, 28) == [3, 2], \
        ("Cat age should be 3 and dog age should be 2 "
         "in human years when they are 28")


def test_one_hundred_years() -> None:
    assert get_human_age(100, 100) == [21, 17], \
        ("Cat age should be 21 and dog age should be 17 "
         "in human years")
