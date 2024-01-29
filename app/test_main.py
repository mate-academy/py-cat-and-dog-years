from app.main import get_human_age


def test_get_human_age() -> None:
    assert get_human_age(1, 1) == [0, 0], "test failed for input 1"
    assert get_human_age(14, 14) == [0, 0], "test failed for input 14"
    assert get_human_age(15, 15) == [1, 1], "test failed for input 15"
    assert get_human_age(24, 24) == [2, 2], "test failed for input 24"
    assert get_human_age(27, 27) == [2, 2], "test failed for input 27"
    assert get_human_age(28, 28) == [3, 2], "test failed for input 28"
    assert get_human_age(100, 100) == [21, 17], "test failed for input 100"
