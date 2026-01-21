from app.main import get_human_age


def test_check_zero_years():
    goal = get_human_age(14, 1)

    assert goal == [0, 0]


def test_check_one_years():
    goal = get_human_age(23, 15)

    assert goal == [1, 1]


def test_check_three_years():
    goal = get_human_age(28, 29)

    assert goal == [3, 3]


def test_check_other_values():
    goal_1 = get_human_age(24, 24)
    goal_2 = get_human_age(100, 100)

    assert goal_1 == [2, 2]
    assert goal_2 == [21, 17]
