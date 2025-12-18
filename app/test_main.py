from app.main import get_human_age


def test_should_return_list():
    goals = get_human_age(0, 0)
    assert type(goals) == list


def test_should_return_list_of_given_length():
    goals = get_human_age(0, 0)
    assert len(goals) == 3

def test_should_return_list_of_integers():
    goals = get_human_age(0, 0)
    assert isinstance(goals[0], int) and isinstance(goals[1], int)