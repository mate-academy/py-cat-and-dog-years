from app.main import get_human_age


def test_get_human_age() -> None:
    assert get_human_age(28, 28) == [3, 2]
