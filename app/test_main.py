import pytest
from app.main import get_human_age


def test_get_human_age() -> None:
    assert get_human_age(0, 0) == [0, 0]
    assert get_human_age(14, 14) == [0, 0]
    assert get_human_age(15, 15) == [1, 1]
    assert get_human_age(23, 23) == [2, 2]
    assert get_human_age(24, 24) == [2, 2]
    assert get_human_age(27, 27) == [2, 2]
    assert get_human_age(28, 28) == [3, 2]
    assert get_human_age(100, 100) == [21, 17]

    assert get_human_age(16, 15) == [1, 1]
    assert get_human_age(25, 25) == [2, 2]
    assert get_human_age(30, 30) == [3, 3]


if __name__ == "__main__":
    pytest.main()
