from app.main import get_human_age


def test_get_human_age_basic_cases() -> None:
    assert get_human_age(0, 0) == [0, 0]
    assert get_human_age(14, 14) == [0, 0]
    assert get_human_age(15, 15) == [1, 1]
    assert get_human_age(23, 23) == [1, 1]
    assert get_human_age(24, 24) == [2, 2]
    assert get_human_age(27, 27) == [2, 2]
    assert get_human_age(28, 28) == [3, 2]
    assert get_human_age(100, 100) == [21, 17]


def test_get_human_age_independence() -> None:
    cat_only = get_human_age(28, 0)
    dog_only = get_human_age(0, 28)
    assert cat_only == [3, 0]
    assert dog_only == [0, 2]


def test_get_human_age_large_values() -> None:
    result = get_human_age(400, 400)
    cat_human, dog_human = result
    assert cat_human > 50
    assert dog_human > 50


def test_get_human_age_edge_transitions() -> None:
    assert get_human_age(15, 0)[0] == 1
    assert get_human_age(24, 0)[0] == 2
    assert get_human_age(28, 0)[0] == 3

    assert get_human_age(0, 15)[1] == 1
    assert get_human_age(0, 24)[1] == 2
    assert get_human_age(0, 29)[1] == 3
