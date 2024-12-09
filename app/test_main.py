from app.main import get_human_age


def test_should_return_correct_human_age_for_cat_and_dog() -> None:
    assert get_human_age(15, 15) == [1, 1]

    assert get_human_age(24, 24) == [2, 2]

    assert get_human_age(28, 15) == [3, 1]

    assert get_human_age(15, 29) == [1, 3]

    assert get_human_age(36, 35) == [5, 4]

    assert get_human_age(10, 10) == [0, 0]


def test_should_handle_edge_cases_for_cat_and_dog() -> None:
    assert get_human_age(0, 0) == [0, 0]

    assert get_human_age(15, 0) == [1, 0]

    assert get_human_age(0, 24) == [0, 2]

    assert get_human_age(-5, -10) == [0, 0]
