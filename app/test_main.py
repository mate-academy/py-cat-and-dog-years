from app.main import get_human_age


def test_zero_age() -> None:
    result = get_human_age(0, 0)

    assert result == [0, 0]


def test_fourteen_age() -> None:
    result = get_human_age(14, 14)

    assert result == [0, 0]


def test_fifteen_age() -> None:
    result = get_human_age(15, 15)

    assert result == [1, 1]


def test_twentythree_age() -> None:
    result = get_human_age(23, 23)

    assert result == [1, 1]


def test_twentyfour_age() -> None:
    result = get_human_age(24, 24)

    assert result == [2, 2]


def test_twentyeight_age() -> None:
    result = get_human_age(28, 28)

    assert result == [3, 2]


def test_twentynine_age() -> None:
    result = get_human_age(29, 29)

    assert result == [3, 3]


def test_hundred_age() -> None:
    result = get_human_age(100, 100)

    assert result == [21, 17]
