from app.main import get_human_age


def test_get_human_age() -> None:
    # Test cases

    # Both cat and dog ages are 0
    assert get_human_age(0, 0) == [0, 0]

    # Both cat and dog ages are 14
    assert get_human_age(14, 14) == [0, 0]

    # Cat age is 15 and dog age is 15
    assert get_human_age(15, 15) == [1, 1]

    # Cat age is 23 and dog age is 23
    assert get_human_age(23, 23) == [1, 1]

    # Cat age is 24 and dog age is 24
    assert get_human_age(24, 24) == [2, 2]

    # Cat age is 27 and dog age is 27
    assert get_human_age(27, 27) == [2, 2]

    # Cat age is 28 and dog age is 28
    assert get_human_age(28, 28) == [3, 2]

    # Cat age is 100 and dog age is 100
    assert get_human_age(100, 100) == [21, 17]
