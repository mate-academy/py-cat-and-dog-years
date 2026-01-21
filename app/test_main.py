from app.main import get_human_age

def test_get_human_age():
    assert get_human_age(12, 13) == [0, 0]
    assert get_human_age(15, 15) == [1, 1]
    assert get_human_age(24, 24) == [2, 2]
    assert get_human_age(28, 28) == [3, 2]
    assert get_human_age(100, 100) == [21, 17]
