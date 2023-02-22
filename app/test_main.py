from app.main import get_human_age


def test_get_human_age() -> None:

    assert get_human_age(0, 0) == [0, 0]

    assert get_human_age(13, 13) == [0, 0]

    assert get_human_age(15, 15) == [1, 1]

    assert get_human_age(23, 23) == [1, 1]

    assert get_human_age(30, 30) == [2, 2]

    assert get_human_age(27, 27) == [2, 2]

    assert get_human_age(28, 20) == [3, 2]

    assert get_human_age(200, 200) == [21, 17]
