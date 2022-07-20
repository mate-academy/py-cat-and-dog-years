from app.main import get_human_age


def test_of_correctly_type_and_result():
    assert get_human_age(15, 15) == [1, 1]
    assert get_human_age(24, 24) == [2, 2]
    assert get_human_age(28, 29) == [3, 3]
