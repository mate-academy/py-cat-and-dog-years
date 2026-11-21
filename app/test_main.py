from app.main import get_human_age

def test_get_human_age():
    assert get_human_age(24, 24) == [2, 2]
