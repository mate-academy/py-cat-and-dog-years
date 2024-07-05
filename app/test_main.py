
from app.main import get_human_age


def test_get_human_age() -> None:
    assert get_human_age(0, 0) == [0, 0], "Failed on (0, 0)"
    assert get_human_age(14, 14) == [0, 0], "Failed on (14, 14)"
    assert get_human_age(15, 15) == [1, 1], "Failed on (15, 15)"
    assert get_human_age(23, 23) == [1, 1], "Failed on (23, 23)"
    assert get_human_age(24, 24) == [2, 2], "Failed on (24, 24)"
    assert get_human_age(27, 27) == [2, 2], "Failed on (27, 27)"
    assert get_human_age(28, 28) == [3, 2], "Failed on (28, 28)"
    assert get_human_age(100, 100) == [21, 17], "Failed on (100, 100)"
