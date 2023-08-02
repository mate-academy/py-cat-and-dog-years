from app.main import get_human_age


def test_should_return_list():
    goals = get_human_age(0, 0)
    assert (
            isinstance(goals, list)
            or isinstance(goals[0], int)
            or isinstance(goals[1], int)
    )


def test_should_return_list_of_given_length():
    goals = get_human_age(0, 0)
    assert len(goals) == 2


def test_should_return_expected_goals():
    goals = get_human_age(28, 28)
    assert goals == [3, 2]


def test_should_return_full_year():
    goals = get_human_age(28, 28)
    assert goals[0] % 1 == 0 or goals[1] % 1 == 0
